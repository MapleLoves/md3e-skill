#!/usr/bin/env python3
"""
generate_theme.py - Generate Compose Color.kt + Theme.kt from a seed color.

Uses the Material Color Utilities HCT color space algorithm to derive a complete
M3E color scheme (48 roles, light + dark) from a single seed color.

Usage:
    python generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/
    python generate_theme.py --seed 0xFF6750A4 --output ./theme/

Requirements:
    pip install material-color-utilities
    (falls back to built-in approximation if not installed)
"""

import argparse
import re
from pathlib import Path


def parse_seed(seed_str: str) -> int:
    s = seed_str.strip().lstrip('#')
    if s.startswith('0x') or s.startswith('0X'):
        s = s[2:]
    if len(s) == 6:
        s = 'FF' + s
    return int(s, 16)


def argb_to_compose(argb: int) -> str:
    return f'Color(0x{argb:08X})'


try:
    from material_color_utilities.python.scheme.scheme_tonal_spot import SchemeTonalSpot
    from material_color_utilities.python.dynamiccolor.material_dynamic_colors import \
        material_dynamic_colors
    HAS_MCU = True
except ImportError:
    HAS_MCU = False


def gen_mcu(seed_argb, dark):
    scheme = SchemeTonalSpot(seed_argb, dark=dark)
    out = {}
    for dc in material_dynamic_colors():
        out[re.sub(r'(?<!^)(?=[A-Z])', '_', dc.name).lower()] = dc.get_hct(scheme).to_argb()
    return out


def rgb_to_hct(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    if d == 0: h = 0
    elif mx == r: h = 60 * (((g - b) / d) % 6)
    elif mx == g: h = 60 * (((b - r) / d) + 2)
    else: h = 60 * (((r - g) / d) + 4)
    return h, d * 100, (mx + mn) / 2 * 100


def hct_to_rgb(h, c, t):
    h = h % 360
    s = min(c / 100, 1) if t > 0 else 0
    l = t / 100
    cv = (1 - abs(2 * l - 1)) * s
    x = cv * (1 - abs((h / 60) % 2 - 1))
    m = l - cv / 2
    if h < 60: r, g, b = cv, x, 0
    elif h < 120: r, g, b = x, cv, 0
    elif h < 180: r, g, b = 0, cv, x
    elif h < 240: r, g, b = 0, x, cv
    elif h < 300: r, g, b = x, 0, cv
    else: r, g, b = cv, 0, x
    return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)


def tone_argb(hue, chroma, tone):
    r, g, b = hct_to_rgb(hue, chroma, tone)
    return (0xFF << 24) | (r << 16) | (g << 8) | b


def gen_fallback(seed_argb, dark):
    r = (seed_argb >> 16) & 0xFF
    g = (seed_argb >> 8) & 0xFF
    b = seed_argb & 0xFF
    h, c, t = rgb_to_hct(r, g, b)
    sec_h = (h + 30) % 360
    tert_h = (h + 60) % 360
    err_h = 25

    roles = {
        'primary': (h, c, 40 if not dark else 80),
        'on_primary': (h, c, 100 if not dark else 20),
        'primary_container': (h, c, 90 if not dark else 30),
        'on_primary_container': (h, c, 10 if not dark else 90),
        'inverse_primary': (h, c, 80 if not dark else 40),
        'secondary': (sec_h, min(c, 24), 40 if not dark else 80),
        'on_secondary': (sec_h, min(c, 24), 100 if not dark else 20),
        'secondary_container': (sec_h, min(c, 24), 90 if not dark else 30),
        'on_secondary_container': (sec_h, min(c, 24), 10 if not dark else 90),
        'tertiary': (tert_h, min(c, 48), 40 if not dark else 80),
        'on_tertiary': (tert_h, min(c, 48), 100 if not dark else 20),
        'tertiary_container': (tert_h, min(c, 48), 90 if not dark else 30),
        'on_tertiary_container': (tert_h, min(c, 48), 10 if not dark else 90),
        'background': (h, 4, 99 if not dark else 10),
        'on_background': (h, 4, 10 if not dark else 90),
        'surface': (h, 4, 99 if not dark else 10),
        'on_surface': (h, 4, 10 if not dark else 90),
        'surface_variant': (h, 4, 90 if not dark else 30),
        'on_surface_variant': (h, 4, 30 if not dark else 80),
        'surface_tint': (h, c, 40 if not dark else 80),
        'inverse_surface': (h, 0, 20 if not dark else 90),
        'inverse_on_surface': (h, 0, 95 if not dark else 20),
        'error': (err_h, 60, 40 if not dark else 80),
        'on_error': (err_h, 60, 100 if not dark else 20),
        'error_container': (err_h, 60, 90 if not dark else 30),
        'on_error_container': (err_h, 60, 10 if not dark else 90),
        'outline': (h, c * 0.3, 50 if not dark else 60),
        'outline_variant': (h, c * 0.3, 80 if not dark else 30),
        'scrim': (0, 0, 0),
        'surface_bright': (h, 4, 98 if not dark else 24),
        'surface_container': (h, 4, 94 if not dark else 12),
        'surface_container_high': (h, 4, 92 if not dark else 17),
        'surface_container_highest': (h, 4, 90 if not dark else 22),
        'surface_container_low': (h, 4, 96 if not dark else 10),
        'surface_container_lowest': (h, 4, 100 if not dark else 4),
        'surface_dim': (h, 4, 87 if not dark else 6),
    }
    fixed = {
        'primary_fixed': (h, c, 90),
        'primary_fixed_dim': (h, c, 80),
        'on_primary_fixed': (h, c, 10),
        'on_primary_fixed_variant': (h, c, 30),
        'secondary_fixed': (sec_h, min(c, 24), 90),
        'secondary_fixed_dim': (sec_h, min(c, 24), 80),
        'on_secondary_fixed': (sec_h, min(c, 24), 10),
        'on_secondary_fixed_variant': (sec_h, min(c, 24), 30),
        'tertiary_fixed': (tert_h, min(c, 48), 90),
        'tertiary_fixed_dim': (tert_h, min(c, 48), 80),
        'on_tertiary_fixed': (tert_h, min(c, 48), 10),
        'on_tertiary_fixed_variant': (tert_h, min(c, 48), 30),
    }
    out = {k: tone_argb(*v) for k, v in {**roles, **fixed}.items()}
    return out


def gen_scheme(seed_argb, dark):
    return gen_mcu(seed_argb, dark) if HAS_MCU else gen_fallback(seed_argb, dark)


PARAMS = [
    ('primary', 'primary'), ('on_primary', 'onPrimary'),
    ('primary_container', 'primaryContainer'), ('on_primary_container', 'onPrimaryContainer'),
    ('inverse_primary', 'inversePrimary'),
    ('primary_fixed', 'primaryFixed'), ('primary_fixed_dim', 'primaryFixedDim'),
    ('on_primary_fixed', 'onPrimaryFixed'), ('on_primary_fixed_variant', 'onPrimaryFixedVariant'),
    ('secondary', 'secondary'), ('on_secondary', 'onSecondary'),
    ('secondary_container', 'secondaryContainer'), ('on_secondary_container', 'onSecondaryContainer'),
    ('secondary_fixed', 'secondaryFixed'), ('secondary_fixed_dim', 'secondaryFixedDim'),
    ('on_secondary_fixed', 'onSecondaryFixed'), ('on_secondary_fixed_variant', 'onSecondaryFixedVariant'),
    ('tertiary', 'tertiary'), ('on_tertiary', 'onTertiary'),
    ('tertiary_container', 'tertiaryContainer'), ('on_tertiary_container', 'onTertiaryContainer'),
    ('tertiary_fixed', 'tertiaryFixed'), ('tertiary_fixed_dim', 'tertiaryFixedDim'),
    ('on_tertiary_fixed', 'onTertiaryFixed'), ('on_tertiary_fixed_variant', 'onTertiaryFixedVariant'),
    ('background', 'background'), ('on_background', 'onBackground'),
    ('surface', 'surface'), ('on_surface', 'onSurface'),
    ('surface_variant', 'surfaceVariant'), ('on_surface_variant', 'onSurfaceVariant'),
    ('surface_tint', 'surfaceTint'), ('inverse_surface', 'inverseSurface'),
    ('inverse_on_surface', 'inverseOnSurface'),
    ('error', 'error'), ('on_error', 'onError'),
    ('error_container', 'errorContainer'), ('on_error_container', 'onErrorContainer'),
    ('outline', 'outline'), ('outline_variant', 'outlineVariant'), ('scrim', 'scrim'),
    ('surface_bright', 'surfaceBright'), ('surface_container', 'surfaceContainer'),
    ('surface_container_high', 'surfaceContainerHigh'), ('surface_container_highest', 'surfaceContainerHighest'),
    ('surface_container_low', 'surfaceContainerLow'), ('surface_container_lowest', 'surfaceContainerLowest'),
    ('surface_dim', 'surfaceDim'),
]


def gen_color_kt(cl, cd, pkg, name):
    L = [f'package {pkg}', '', 'import androidx.compose.material3.ColorScheme',
         'import androidx.compose.material3.darkColorScheme', 'import androidx.compose.material3.lightColorScheme',
         'import androidx.compose.ui.graphics.Color', '',
         f'// Auto-generated M3E color scheme for {name} (48 roles x 2 schemes)', '']
    L.append('val LightColorScheme: ColorScheme = lightColorScheme(')
    for sn, pn in PARAMS:
        L.append(f'    {pn} = {argb_to_compose(cl.get(sn, 0xFF000000))},')
    L.append(')')
    L.append('')
    L.append('val DarkColorScheme: ColorScheme = darkColorScheme(')
    for sn, pn in PARAMS:
        L.append(f'    {pn} = {argb_to_compose(cd.get(sn, 0xFF000000))},')
    L.append(')')
    L.append('')
    return '\n'.join(L)


def gen_theme_kt(pkg, name):
    fn = re.sub(r'[^a-zA-Z0-9]', '', name) + 'Theme'
    return f'''package {pkg}

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialExpressiveTheme
import androidx.compose.material3.MotionScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext

@Composable
fun {fn}(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {{
    val context = LocalContext.current
    val colorScheme = when {{
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }}
    MaterialExpressiveTheme(
        colorScheme = colorScheme,
        motionScheme = MotionScheme.expressive(),
        content = content
    )
}}
'''


def main():
    p = argparse.ArgumentParser(description='Generate Compose M3E color scheme from seed color.')
    p.add_argument('--seed', required=True, help='Seed color (e.g. #6750A4)')
    p.add_argument('--package', default='com.example.app')
    p.add_argument('--name', default='App')
    p.add_argument('--output', default='./theme')
    a = p.parse_args()

    seed = parse_seed(a.seed)
    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)

    if not HAS_MCU:
        print('Warning: material-color-utilities not installed, using approximation.')
        print('For accurate HCT colors: pip install material-color-utilities\n')

    cl = gen_scheme(seed, False)
    cd = gen_scheme(seed, True)

    (out / 'Color.kt').write_text(gen_color_kt(cl, cd, a.package, a.name), encoding='utf-8')
    (out / 'Theme.kt').write_text(gen_theme_kt(a.package, a.name), encoding='utf-8')

    print(f'Seed: 0x{seed:08X}')
    print(f'Output: {out.resolve()}')
    print(f'  Color.kt ({len(PARAMS)} roles x 2 schemes)')
    print(f'  Theme.kt (MaterialExpressiveTheme + MotionScheme.expressive)')


if __name__ == '__main__':
    main()
