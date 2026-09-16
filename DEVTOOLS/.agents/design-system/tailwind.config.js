// Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta
/**
 * DESIGN SYSTEM — TAILWIND CSS PRESET
 * Mapping Design Tokens ke Tailwind utility classes
 * 
 * CARA PAKAI:
 *   1. Salin file ini ke frontend/tailwind.config.js
 *   2. Pastikan tokens/*.css sudah diimport di main CSS
 *   3. Semua class Tailwind di bawah akan mengacu ke CSS variables
 *      sehingga otomatis mendukung light/dark mode via [data-theme]
 *
 * Kompatibel dengan: Tailwind CSS v3.x
 */

/** @type {import('tailwindcss').Config} */
module.exports = {
  // Scan semua file komponen
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue}",
  ],

  // Dark mode dikendalikan via [data-theme="dark"] di <html>
  // Bukan via class 'dark' — sesuai design system kita
  darkMode: ['selector', '[data-theme="dark"]'],

  theme: {
    extend: {

      // ─── COLORS ───────────────────────────────────────
      // Semua warna mengacu ke CSS variables dari tokens/colors.css
      // Sehingga otomatis ganti saat dark mode aktif
      colors: {
        // Backgrounds
        bg: {
          primary:   'var(--color-bg-primary)',
          secondary: 'var(--color-bg-secondary)',
          tertiary:  'var(--color-bg-tertiary)',
          grouped:   'var(--color-bg-grouped)',
          elevated:  'var(--color-bg-elevated)',
          overlay:   'var(--color-bg-overlay)',
        },
        // Labels / Text
        label: {
          primary:    'var(--color-label-primary)',
          secondary:  'var(--color-label-secondary)',
          tertiary:   'var(--color-label-tertiary)',
          quaternary: 'var(--color-label-quaternary)',
          inverted:   'var(--color-label-inverted)',
        },
        // Fills
        fill: {
          primary:    'var(--color-fill-primary)',
          secondary:  'var(--color-fill-secondary)',
          tertiary:   'var(--color-fill-tertiary)',
          quaternary: 'var(--color-fill-quaternary)',
        },
        // Separators
        separator: {
          DEFAULT: 'var(--color-separator)',
          opaque:  'var(--color-separator-opaque)',
        },
        // Tint / Brand
        tint: {
          DEFAULT:    'var(--color-tint)',
          hover:      'var(--color-tint-hover)',
          active:     'var(--color-tint-active)',
          subtle:     'var(--color-tint-subtle)',
          foreground: 'var(--color-tint-foreground)',
        },
        // System Colors
        system: {
          green:  'var(--color-system-green)',
          red:    'var(--color-system-red)',
          orange: 'var(--color-system-orange)',
          yellow: 'var(--color-system-yellow)',
          purple: 'var(--color-system-purple)',
          teal:   'var(--color-system-teal)',
          indigo: 'var(--color-system-indigo)',
          pink:   'var(--color-system-pink)',
        },
        // Status
        success: {
          DEFAULT: 'var(--color-success)',
          bg:      'var(--color-success-bg)',
        },
        error: {
          DEFAULT: 'var(--color-error)',
          bg:      'var(--color-error-bg)',
        },
        warning: {
          DEFAULT: 'var(--color-warning)',
          bg:      'var(--color-warning-bg)',
        },
        info: {
          DEFAULT: 'var(--color-info)',
          bg:      'var(--color-info-bg)',
        },
        // Input
        input: {
          bg:           'var(--color-input-bg)',
          border:       'var(--color-input-border)',
          borderFocus:  'var(--color-input-border-focus)',
          placeholder:  'var(--color-input-placeholder)',
        },
        // Nav
        nav: {
          bg:     'var(--color-nav-bg)',
          border: 'var(--color-nav-border)',
        },
        // Table
        table: {
          headerBg:   'var(--color-table-header-bg)',
          rowHover:   'var(--color-table-row-hover)',
          rowSelected:'var(--color-table-row-selected)',
          border:     'var(--color-table-border)',
        },
      },

      // ─── FONT FAMILY ────────────────────────────────────
      fontFamily: {
        sans:    ['var(--font-sans)'],
        mono:    ['var(--font-mono)'],
        rounded: ['var(--font-rounded)'],
      },

      // ─── FONT SIZE ──────────────────────────────────────
      fontSize: {
        'xs':   ['var(--text-xs)',   { lineHeight: 'var(--leading-normal)' }],
        'sm':   ['var(--text-sm)',   { lineHeight: 'var(--leading-normal)' }],
        'base': ['var(--text-base)', { lineHeight: 'var(--leading-normal)' }],
        'md':   ['var(--text-md)',   { lineHeight: 'var(--leading-normal)' }],
        'lg':   ['var(--text-lg)',   { lineHeight: 'var(--leading-normal)' }],
        'xl':   ['var(--text-xl)',   { lineHeight: 'var(--leading-normal)' }],
        '2xl':  ['var(--text-2xl)',  { lineHeight: 'var(--leading-snug)' }],
        '3xl':  ['var(--text-3xl)',  { lineHeight: 'var(--leading-tight)' }],
        '4xl':  ['var(--text-4xl)',  { lineHeight: 'var(--leading-tight)' }],
        '5xl':  ['var(--text-5xl)',  { lineHeight: 'var(--leading-tight)' }],
        '6xl':  ['var(--text-6xl)',  { lineHeight: 'var(--leading-tight)' }],
      },

      // ─── SPACING ────────────────────────────────────────
      spacing: {
        '0':  'var(--space-0)',
        '1':  'var(--space-1)',
        '2':  'var(--space-2)',
        '3':  'var(--space-3)',
        '4':  'var(--space-4)',
        '5':  'var(--space-5)',
        '6':  'var(--space-6)',
        '8':  'var(--space-8)',
        '10': 'var(--space-10)',
        '12': 'var(--space-12)',
        '14': 'var(--space-14)',
        '16': 'var(--space-16)',
        '20': 'var(--space-20)',
        '24': 'var(--space-24)',
        '32': 'var(--space-32)',
        '40': 'var(--space-40)',
        '48': 'var(--space-48)',
        '64': 'var(--space-64)',
      },

      // ─── BORDER RADIUS ──────────────────────────────────
      borderRadius: {
        'xs':   'var(--radius-xs)',
        'sm':   'var(--radius-sm)',
        'md':   'var(--radius-md)',
        'DEFAULT': 'var(--radius-md)',
        'lg':   'var(--radius-lg)',
        'xl':   'var(--radius-xl)',
        '2xl':  'var(--radius-2xl)',
        'full': 'var(--radius-full)',
      },

      // ─── BOX SHADOW ─────────────────────────────────────
      boxShadow: {
        'xs':    'var(--shadow-xs)',
        'sm':    'var(--shadow-sm)',
        'md':    'var(--shadow-md)',
        'lg':    'var(--shadow-lg)',
        'xl':    'var(--shadow-xl)',
        'none':  'none',
        // Semantic
        'card':    'var(--elevation-card)',
        'popover': 'var(--elevation-popover)',
        'modal':   'var(--elevation-modal)',
        'navbar':  'var(--elevation-navbar)',
        'input-focus': 'var(--elevation-input-focus)',
      },

      // ─── HEIGHT & MIN SIZES (HIG & A11Y) ───────────────
      height: {
        'navbar':     'var(--height-navbar)',
        'tabbar':     'var(--height-tabbar)',
        'input':      'var(--height-input)',
        'input-lg':   'var(--height-input-lg)',
        'btn-sm':     'var(--height-button-sm)',
        'btn-md':     'var(--height-button-md)',
        'btn-lg':     'var(--height-button-lg)',
        'touch-min':  'var(--target-touch-min)',  // 44px
        'click-min':  'var(--target-click-min)',  // 24px
      },
      minHeight: {
        'touch':      'var(--target-touch-min)',  // 44px
        'click':      'var(--target-click-min)',  // 24px
      },
      minWidth: {
        'touch':      'var(--target-touch-min)',  // 44px
        'click':      'var(--target-click-min)',  // 24px
      },

      // ─── TRANSITION / ANIMATION ─────────────────────────
      transitionDuration: {
        'instant':    'var(--duration-instant)',
        'fast':       'var(--duration-fast)',
        'normal':     'var(--duration-normal)',
        'moderate':   'var(--duration-moderate)',
        'slow':       'var(--duration-slow)',
        'deliberate': 'var(--duration-deliberate)',
      },
      transitionTimingFunction: {
        'standard':   'var(--ease-standard)',
        'enter':      'var(--ease-enter)',
        'exit':       'var(--ease-exit)',
        'emphasized': 'var(--ease-emphasized)',
        'spring':     'var(--ease-spring)',
      },
      animation: {
        'fade-in':      'fade-in var(--duration-normal) var(--ease-enter)',
        'slide-up':     'slide-in-up var(--duration-moderate) var(--ease-enter)',
        'slide-down':   'slide-in-down var(--duration-moderate) var(--ease-enter)',
        'scale-in':     'scale-in var(--duration-moderate) var(--ease-spring)',
        'shimmer':      'shimmer 1.5s var(--ease-linear) infinite',
        'spin':         'spin 1s var(--ease-linear) infinite',
        'pulse':        'pulse 2s var(--ease-standard) infinite',
      },

      // ─── BACKDROP BLUR & LIQUID GLASS ───────────────────
      backdropBlur: {
        'navbar': '20px',
        'sheet':  '16px',
        'card':   '8px',
      },
      backgroundColor: {
        'glass-regular': 'var(--glass-regular-bg)',
        'glass-clear':   'var(--glass-clear-bg)',
        'glass-dim':     'var(--glass-dimming-layer)',
      },
      borderColor: {
        'glass':         'var(--glass-border)',
      },
    },
  },

  plugins: [],
};
