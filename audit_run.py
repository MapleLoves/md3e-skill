#!/usr/bin/env python3
import re, os, sys, zipfile, datetime, yaml

ROOT = os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else os.getcwd()
# We will pass root as cwd
ROOT = os.getcwd()

checks = []
def check(label, ok, detail=None):
    checks.append((label, ok, detail))

# --- frontmatter ---
skill = open('SKILL.md', encoding='utf-8').read()
m = re.match(r'^---\n(.*?)\n---', skill, re.S)
check('SKILL.md has frontmatter', bool(m))
if m:
    fm = yaml.safe_load(m.group(1))
    check('frontmatter name=md3e', fm.get('name')=='md3e', fm.get('name'))
    check('frontmatter version present', 'version' in fm, fm.get('version'))
    check('description length <= 1024', len(fm.get('description',''))<=1024, len(fm.get('description','')))
    desc = fm.get('description','')
    for t in ['Material 3 Expressive','MD3E','MaterialExpressiveTheme','Material Design 3']:
        check(f'description contains {t!r}', t in desc)

lines = skill.splitlines()
check('SKILL.md line count <= 200', len(lines)<=200, len(lines))

# --- required paths ---
required = [
    'SKILL.md','README.md','README.zh-CN.md','CHANGELOG.md','LICENSE','PUBLISH.md','CONTRIBUTING.md',
    'references/version-baseline.md','references/design-tokens.md','references/components-catalog.md',
    'references/m3-vs-m3e-diff.md','references/compose-api-full.md','references/expressive-design-tactics.md',
    'references/design-research.md',
    'references/m3e/design-system.md','references/m3e/color-typography-shape.md','references/m3e/motion-physics.md',
    'references/m3e/components.md','references/m3e/compose-api.md',
    'references/m3e/design-system.en.md','references/m3e/color-typography-shape.en.md',
    'references/m3e/motion-physics.en.md','references/m3e/components.en.md','references/m3e/compose-api.en.md',
    'assets/templates/MD3ETheme.kt','assets/templates/Color.kt','assets/templates/Type.kt','assets/templates/Shape.kt',
    'scripts/generate_theme.py',
]
for p in required:
    check(f'exists: {p}', os.path.exists(p))

# --- content fixes ---
for fn, label in [('references/design-tokens.md','design-tokens'), ('references/m3-vs-m3e-diff.md','m3-vs-m3e-diff')]:
    ls = open(fn, encoding='utf-8').readlines()
    bad = [i+1 for i,l in enumerate(ls) if 'Typography now supports' in l]
    check(f'{label}: no false defaultFontFamily claim', len(bad)==0, bad)

ls = open('references/design-tokens.md', encoding='utf-8').readlines()
dp = [i+1 for i in range(128,144) if 'dp' in ls[i]]
check('design-tokens: letterSpacing units are sp not dp', len(dp)==0, dp)

# --- m3-content ---
mc = [f for f in os.listdir('references/m3-content')] if os.path.isdir('references/m3-content') else []
check('m3-content dir exists', os.path.isdir('references/m3-content'))
if os.path.isdir('references/m3-content'):
    md_files = []
    for r,d,fs in os.walk('references/m3-content'):
        for f in fs:
            if f.endswith('.md'): md_files.append(os.path.join(r,f))
    check('m3-content has >= 200 md files', len(md_files)>=200, len(md_files))

# --- zip ---
zp = '../dist/md3e.zip'
check('dist/md3e.zip exists', os.path.exists(zp))
if os.path.exists(zp):
    st = os.stat(zp)
    mt = datetime.datetime.fromtimestamp(st.st_mtime)
    check('dist/md3e.zip rebuilt today', mt.date()==datetime.date(2026,9,22), str(mt))
    z = zipfile.ZipFile(zp)
    names = z.namelist()
    check('zip has SKILL.md', any(n.endswith('SKILL.md') for n in names))
    check('zip has design-tokens.md', 'references/design-tokens.md' in names)
    # verify zip content is fresh
    with z.open('references/design-tokens.md') as f:
        zl = f.read().decode('utf-8').splitlines()
    check('zip design-tokens L149 has no false claim', 'now supports' not in zl[148], zl[148][:70])
    with z.open('references/m3-vs-m3e-diff.md') as f:
        zl2 = f.read().decode('utf-8').splitlines()
    check('zip m3-vs-m3e-diff L84 has no false claim', 'now supports' not in zl2[83], zl2[83][:70])
    for en in ['references/m3e/design-system.en.md','references/m3e/color-typography-shape.en.md',
               'references/m3e/motion-physics.en.md','references/m3e/components.en.md',
               'references/m3e/compose-api.en.md']:
        check(f'zip has {os.path.basename(en)}', en in names)

# --- PUBLISH.md ---
pub = open('PUBLISH.md', encoding='utf-8').read()
check('PUBLISH.md no git tag v1.0.0', 'git tag v1.0.0' not in pub)

# --- output ---
fails = [(l,d) for l,o,d in checks if not o]
passes = sum(1 for _,o,_ in checks if o)
for l,o,d in checks:
    mark = 'PASS' if o else 'FAIL'
    extra = f'  detail={d}' if (d is not None and not o) else ''
    print(f'{mark}  {l}{extra}')
print()
print(f'SUMMARY: {passes}/{len(checks)} passed, {len(fails)} failed')
sys.exit(1 if fails else 0)
