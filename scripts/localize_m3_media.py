#!/usr/bin/env python3
"""Download remote images embedded in m3-content Markdown and rewrite them locally."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import mimetypes
import os
import re
import shutil
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


IMAGE_RE = re.compile(
    r"!\[[^\]]*\]\(\s*<?(?P<url>https?://(?:\\.|[^\s)>])+)>?"
    r"(?:\s+[\"'][^\"']*[\"'])?\s*\)"
)

CONTENT_TYPE_EXTENSIONS = {
    "image/avif": ".avif",
    "image/bmp": ".bmp",
    "image/gif": ".gif",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)


def remote_images(markdown: str) -> set[str]:
    return {match.group("url") for match in IMAGE_RE.finditer(markdown)}


def extension_for(url: str, content_type: str) -> str:
    suffix = Path(urllib.parse.unquote(urllib.parse.urlsplit(url).path)).suffix.lower()
    if suffix in {".avif", ".bmp", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    media_type = content_type.partition(";")[0].strip().lower()
    return CONTENT_TYPE_EXTENSIONS.get(media_type) or mimetypes.guess_extension(media_type) or ".bin"


def filename_for(url: str, extension: str) -> str:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:20]
    basename = Path(urllib.parse.unquote(urllib.parse.urlsplit(url).path)).stem
    basename = re.sub(r"[^A-Za-z0-9._-]+", "-", basename).strip("-._")[:80]
    if not basename:
        basename = "image"
    return f"{basename}-{digest}{extension}"


def download_one(url: str, asset_dir: Path, attempts: int = 4) -> tuple[str, str, int]:
    last_error: Exception | None = None
    request_url = url.replace(r"\(", "(").replace(r"\)", ")")
    for attempt in range(1, attempts + 1):
        temp_path: Path | None = None
        try:
            request = urllib.request.Request(
                request_url,
                headers={"User-Agent": USER_AGENT, "Accept": "image/avif,image/webp,image/*,*/*;q=0.8"},
            )
            with urllib.request.urlopen(request, timeout=60) as response:
                content_type = response.headers.get("Content-Type", "")
                if not content_type.lower().startswith("image/"):
                    raise ValueError(f"expected image response, received {content_type or 'unknown content type'}")
                extension = extension_for(url, content_type)
                destination = asset_dir / filename_for(url, extension)
                if destination.exists() and destination.stat().st_size:
                    return url, destination.name, destination.stat().st_size
                with tempfile.NamedTemporaryFile(dir=asset_dir, delete=False) as temporary:
                    temp_path = Path(temporary.name)
                    shutil.copyfileobj(response, temporary)
                if not temp_path.stat().st_size:
                    raise ValueError("empty response body")
                temp_path.replace(destination)
                return url, destination.name, destination.stat().st_size
        except (OSError, urllib.error.URLError, ValueError) as error:
            last_error = error
            if temp_path and temp_path.exists():
                temp_path.unlink()
            if attempt < attempts:
                time.sleep(min(2 ** (attempt - 1), 8))
    raise RuntimeError(f"{url}: {last_error}")


def relative_asset_link(markdown_path: Path, asset_path: Path) -> str:
    return Path(os.path.relpath(asset_path, markdown_path.parent)).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("references/m3-content"))
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()

    root = args.root.resolve()
    asset_dir = root / "_assets"
    asset_dir.mkdir(parents=True, exist_ok=True)
    markdown_files = sorted(root.rglob("*.md"))
    file_text = {path: path.read_text(encoding="utf-8") for path in markdown_files}
    urls = sorted({url for text in file_text.values() for url in remote_images(text)})

    print(f"Found {len(urls)} unique remote images in {len(markdown_files)} Markdown files.")
    downloaded: dict[str, str] = {}
    failures: list[str] = []
    total_bytes = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(download_one, url, asset_dir): url for url in urls}
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            try:
                url, filename, byte_count = future.result()
                downloaded[url] = filename
                total_bytes += byte_count
            except Exception as error:  # report every failed URL before exiting
                failures.append(str(error))
            if completed % 100 == 0 or completed == len(futures):
                print(f"Downloaded {completed}/{len(futures)} ({len(failures)} failures).", flush=True)

    if failures:
        failure_path = root / "_asset-download-failures.txt"
        failure_path.write_text("\n".join(failures) + "\n", encoding="utf-8")
        print(f"Download failed for {len(failures)} images; details: {failure_path}")
        return 1

    changed_files = 0
    replaced_occurrences = 0
    for path, original in file_text.items():
        def replace(match: re.Match[str]) -> str:
            nonlocal replaced_occurrences
            url = match.group("url")
            filename = downloaded.get(url)
            if not filename:
                return match.group(0)
            replacement = relative_asset_link(path, asset_dir / filename)
            replaced_occurrences += 1
            return match.group(0).replace(url, replacement, 1)

        updated = IMAGE_RE.sub(replace, original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="")
            changed_files += 1

    manifest = {
        "asset_count": len(downloaded),
        "bytes": total_bytes,
        "files_changed": changed_files,
        "image_references_replaced": replaced_occurrences,
        "assets": dict(sorted(downloaded.items())),
    }
    (asset_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    remaining = sum(len(remote_images(path.read_text(encoding="utf-8"))) for path in markdown_files)
    if remaining:
        print(f"Verification failed: {remaining} remote image references remain.")
        return 2

    print(
        f"Localized {replaced_occurrences} references across {changed_files} files; "
        f"stored {len(downloaded)} assets ({total_bytes / 1024 / 1024:.1f} MiB)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
