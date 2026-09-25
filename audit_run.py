#!/usr/bin/env python3
"""Read-only structural audit for the design skill and an optional release archive."""

import argparse
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required for maintenance: python -m pip install PyYAML")

ROOT = Path(__file__).resolve().parent
CORE = [
    "SKILL.md", "README.md", "README.zh-CN.md", "CONTRIBUTING.md",
    "PUBLISH.md", "CHANGELOG.md", "LICENSE", "audit_run.py",
    "references/design-tokens.md", "references/components-catalog.md",
    "references/design-research.md", "references/expressive-design-tactics.md",
    "references/m3-vs-m3e-diff.md", "references/version-baseline.md",
    "references/compose-api-full.md",
]
NOTES = ("design-system", "color-typography-shape", "motion-physics", "components", "compose-api")
# The original navigation/developer pages use inline origins without capture dates.
# Preserve that provenance format instead of inventing dates or rewriting sources.
LEGACY_SOURCES = {
    "components.md": "https://m3.material.io/components",
    "develop/android/jetpack-compose.md": "https://m3.material.io/develop/android/jetpack-compose",
    "develop.md": "https://m3.material.io/develop",
    "foundations.md": "https://m3.material.io/foundations",
    "get-started.md": "https://m3.material.io/get-started",
    "index.md": "https://m3.material.io/",
    "styles.md": "https://m3.material.io/styles",
}
REQUIRED = CORE + [f"references/m3e/{name}{suffix}.md" for name in NOTES for suffix in ("", ".en")]
RETIRED = (
    "scripts/generate_theme.py", "assets/templates/MD3ETheme.kt",
    "assets/templates/Color.kt", "assets/templates/Type.kt", "assets/templates/Shape.kt",
)


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing or malformed YAML frontmatter")
    result = yaml.safe_load(match.group(1))
    if not isinstance(result, dict):
        raise ValueError("Frontmatter must be a mapping")
    return result


def local_links(path, text):
    for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
        target = match.group(1).strip()
        if not target:
            continue
        target = target[1:target.index(">")] if target.startswith("<") and ">" in target else target.split()[0]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield (path.parent / unquote(parsed.path)).resolve()


def unclosed_fence(text):
    active = None
    marker = chr(96)
    for line in text.splitlines():
        match = re.match(r"^\s*(" + marker + r"{3,}|~{3,})(.*)$", line)
        if not match:
            continue
        fence, tail = match.groups()
        if active is None:
            active = (fence[0], len(fence))
        elif fence[0] == active[0] and len(fence) >= active[1] and not tail.strip():
            active = None
    return active is not None


def audit(root, archive=None):
    root = Path(root).resolve()
    checks = []

    def check(label, ok, detail=""):
        checks.append((label, bool(ok), str(detail)))

    missing = [name for name in REQUIRED if not (root / name).is_file()]
    check("Required resources and bilingual notes exist", not missing, missing)
    present_retired = [name for name in RETIRED if (root / name).exists()]
    check("Retired generator and four templates are absent", not present_retired, present_retired)

    skill_path = root / "SKILL.md"
    skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
    metadata = {}
    try:
        metadata = frontmatter(skill)
        check("SKILL.md YAML parses", True)
    except (ValueError, yaml.YAMLError) as error:
        check("SKILL.md YAML parses", False, error)
    check("Skill name is md3e", metadata.get("name") == "md3e")
    description = metadata.get("description")
    check("Description is a nonempty string of at most 1024 characters",
          isinstance(description, str) and 0 < len(description) <= 1024)
    extra = set(metadata) - {"name", "description", "license", "allowed-tools", "metadata"}
    check("Frontmatter uses supported fields", not extra, sorted(extra))
    details = metadata.get("metadata", {})
    version = details.get("version", "") if isinstance(details, dict) else ""
    check("Version is stored as metadata.version", isinstance(version, str)
          and bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), version)
    check("Entry point stays within 200 lines", len(skill.splitlines()) <= 200, len(skill.splitlines()))
    changelog_path = root / "CHANGELOG.md"
    changelog = changelog_path.read_text(encoding="utf-8") if changelog_path.exists() else ""
    check("Changelog records the skill version", bool(version) and f"## [{version}]" in changelog)

    # Imported source pages and historical changelog entries contain upstream/retired links.
    # Validate the local navigation maintained by this repository rather than rewriting sources.
    maintained = sorted(set(root.glob("*.md")) - {changelog_path})
    maintained += sorted(p for p in (root / "references").glob("*.md") if p.name != "compose-api-full.md")
    maintained += sorted((root / "references/m3e").glob("*.md"))
    text_map, bad_encoding, broken, retired_refs, fences = {}, [], [], [], []
    for path in maintained:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError as error:
            bad_encoding.append(f"{path.relative_to(root)}: {error}")
            continue
        text_map[path.resolve()] = text
        if unclosed_fence(text):
            fences.append(str(path.relative_to(root)))
        for target in local_links(path, text):
            if not target.exists():
                broken.append(f"{path.relative_to(root)} -> {target}")
        for retired in RETIRED:
            if retired in text.replace("\\", "/"):
                retired_refs.append(f"{path.relative_to(root)} -> {retired}")
    check("Maintained Markdown is valid UTF-8", not bad_encoding, bad_encoding)
    check("Maintained Markdown fences close", not fences, fences)
    check("Maintained local links resolve", not broken, broken)
    check("Live guidance has no retired file references", not retired_refs, retired_refs)

    reachable, pending = set(), [skill_path.resolve()]
    while pending:
        path = pending.pop()
        if path in reachable:
            continue
        reachable.add(path)
        if path in text_map:
            pending.extend(local_links(path, text_map[path]))
    unrouted = [name for name in REQUIRED if name.startswith("references/") and (root / name).resolve() not in reachable]
    check("Curated references are reachable from SKILL.md", not unrouted, unrouted)

    snapshot_root = root / "references/m3-content"
    snapshots = sorted(snapshot_root.rglob("*.md"))
    bad_sources = []
    legacy_errors = [name for name in LEGACY_SOURCES if not (snapshot_root / name).is_file()]
    dated_count = 0
    for path in snapshots:
        try:
            source_text = path.read_text(encoding="utf-8")
            relative = path.relative_to(snapshot_root).as_posix()
            if relative in LEGACY_SOURCES:
                expected = "> 来源: " + LEGACY_SOURCES[relative]
                if expected not in [line.strip() for line in source_text.splitlines()]:
                    legacy_errors.append(relative)
                continue
            dated_count += 1
            fm = frontmatter(source_text)
            if not fm.get("source") or not fm.get("captured"):
                bad_sources.append(str(path.relative_to(root)))
        except (ValueError, UnicodeError, yaml.YAMLError):
            bad_sources.append(str(path.relative_to(root)))
    check("Dated official snapshots retain source and capture metadata", dated_count > 0 and not bad_sources,
          bad_sources or f"{dated_count} dated snapshots")
    check("Legacy navigation pages retain inline source headers", not legacy_errors, legacy_errors)
    catalog = text_map.get((root / "references/components-catalog.md").resolve(), "")
    families = sorted(p for p in (snapshot_root / "components").iterdir() if p.is_dir()) if (snapshot_root / "components").is_dir() else []
    omitted = [p.name for p in families if f"m3-content/components/{p.name}/guidelines.md" not in catalog]
    check("Catalog links every bundled component family", bool(families) and not omitted,
          omitted or f"{len(families)} families")

    if archive is not None:
        try:
            with zipfile.ZipFile(archive) as package:
                names = package.namelist()
                candidates = [name for name in names if name == "SKILL.md" or name.endswith("/SKILL.md")]
                check("Archive has one skill root", len(candidates) == 1, candidates)
                if len(candidates) == 1:
                    prefix = candidates[0][:-len("SKILL.md")]
                    expected = REQUIRED + [str(p.relative_to(root)).replace("\\", "/") for p in snapshots]
                    stale = [name for name in expected if prefix + name not in names
                             or not (root / name).is_file()
                             or package.read(prefix + name) != (root / name).read_bytes()]
                    check("Archive matches current skill, docs, and source snapshots", not stale, stale[:10])
                    retired_in_zip = [name for name in RETIRED if prefix + name in names]
                    check("Archive excludes retired generator and templates", not retired_in_zip, retired_in_zip)
                    duplicates = sorted({name for name in names if names.count(name) > 1})
                    check("Archive has no duplicate entries", not duplicates, duplicates[:10])
        except (OSError, zipfile.BadZipFile) as error:
            check("Requested archive can be read", False, error)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Optional release zip to compare with this source tree")
    args = parser.parse_args()
    checks = audit(ROOT, args.archive)
    for label, ok, detail in checks:
        extra = f"  {detail}" if not ok and detail else ""
        print(f"{'PASS' if ok else 'FAIL'}  {label}{extra}")
    failures = sum(not ok for _, ok, _ in checks)
    print(f"SUMMARY: {len(checks) - failures}/{len(checks)} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
