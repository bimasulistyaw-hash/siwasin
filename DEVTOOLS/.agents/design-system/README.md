<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->
# 🎨 Design System — Diskominfo Kota Yogyakarta
> Berbasis **Apple Human Interface Guidelines (HIG)** — diadaptasi untuk aplikasi web (React/Vue + Tailwind CSS).
> Prinsip: **Clarity · Deference · Depth** | Mode: **Light (default) / Dark**

---

## Struktur Folder

```
.agents/design-system/
├── README.md                  # Panduan ini
├── assets/                    # Aset visual master & logo resmi
│   └── logo-jogja.svg         # Logo Resmi Vektor Pemkot Yogyakarta (Master SVG)
├── tokens/
│   ├── colors.css             # Palet warna + semantic tokens (light & dark)
│   ├── typography.css         # Typeface, size scale, weight, line-height
│   ├── spacing.css            # Spacing scale (8pt grid), radius, shadow
│   └── motion.css             # Durasi & easing animasi
├── tailwind.config.js         # Tailwind preset — mapping token ke utility class
└── components.md              # Spesifikasi komponen HIG-inspired untuk web (termasuk Brand Unit)
```

---

## Cara Pakai di Proyek Baru

### 1. Salin token CSS & Aset Logo Resmi ke proyek frontend
```bash
# Salin token styles
cp .agents/design-system/tokens/*.css frontend/src/assets/styles/tokens/

# Salin logo resmi vektor (logo-jogja.svg)
cp .agents/design-system/assets/logo-jogja.svg frontend/src/assets/logo-jogja.svg
```

Import di `main.css` / `index.css`:
```css
@import './tokens/colors.css';
@import './tokens/typography.css';
@import './tokens/spacing.css';
@import './tokens/motion.css';
```

### 2. Salin Tailwind config
```bash
cp .agents/design-system/tailwind.config.js frontend/tailwind.config.js
```

### 3. Pilihan 8 Tema Terstandarisasi (4 Light & 4 Dark) & Anti-Color Clash

Setiap tema dikurasi dengan rasio kontras tinggi (**WCAG AA/AAA Ratio ≥ 4.5:1**) untuk mencegah tumpang tindih warna (seperti teks putih di atas abu-abu terang, teks coklat/gelap di atas latar hitam, atau elemen dengan kemiripan warna rendah).

| Mode | ID Tema (`data-theme`) | Karakteristik Visual & Palet Utama | Rasio Kontras Teks |
| :--- | :--- | :--- | :---: |
| **Light 1** | `light-yogyakarta` *(Default)* | Classic Pemkot Navy (`#1E3A8A`) + Pure White (`#FFFFFF`) + Slate (`#0F172A`) | 14.5 : 1 |
| **Light 2** | `light-emerald` | Layanan Publik Teal (`#0D9488`) + Mint Surface (`#F0FDFA`) + Deep Emerald | 13.8 : 1 |
| **Light 3** | `light-royal` | Inovasi Digital Royal Blue (`#2563EB`) + Slate Soft (`#F8FAFC`) + Deep Indigo | 15.1 : 1 |
| **Light 4** | `light-amber` | Kraton Heritage Gold (`#B45309`) + Warm Cream (`#FFFBEB`) + Deep Stone | 14.2 : 1 |
| **Dark 1** | `dark-midnight` *(Default Dark)* | Midnight Slate Charcoal (`#0B0F19`) + Sky Blue Tint (`#60A5FA`) + Crisp Gray 50 | 16.2 : 1 |
| **Dark 2** | `dark-emerald` | Deep Forest Black (`#022C22`) + Emerald Vivid (`#34D399`) + Mint White | 15.5 : 1 |
| **Dark 3** | `dark-obsidian` | Pure Pitch Black (`#000000`) + Material Surface (`#121212`) + Pure White | 21.0 : 1 |
| **Dark 4** | `dark-heritage` | Warm Bronze Dark (`#1C1917`) + Gold Amber (`#FBBF24`) + Warm Cream Text | 14.8 : 1 |

Penerapan tema diatur via atribut `data-theme` pada tag `<html>`:
```html
<!-- Contoh pemakaian salah satu tema -->
<html data-theme="light-yogyakarta">
```

Fungsi Switcher Tema via JavaScript:
```js
// Ganti tema dinamis
const setTheme = (themeName) => {
  document.documentElement.setAttribute('data-theme', themeName);
  localStorage.setItem('app-theme', themeName);
};

// Inisialisasi saat load aplikasi
const savedTheme = localStorage.getItem('app-theme') || 'light-yogyakarta';
document.documentElement.setAttribute('data-theme', savedTheme);
```

### 4. Update Design System
Untuk mengubah palet / typography / spacing — **cukup edit file di folder ini** saja, lalu salin ulang ke proyek. Satu sumber kebenaran, semua proyek konsisten.

---

## Prinsip Apple HIG yang Diadopsi

| Prinsip | Implementasi di Web & Platform |
|---|---|
| **Clarity** | Teks selalu readable, hierarki tipografi jelas, ikon bermakna tanpa label tambahan |
| **Deference** | UI tidak mendominasi konten — background subtle, elemen UI "mundur" |
| **Depth** | Layered surfaces, shadow halus, blur (liquid glass & dimming layer), animasi natural |
| **Consistency** | Komponen & pola interaksi seragam di seluruh modul |
| **Feedback** | Setiap aksi pengguna mendapat respons visual (loading, sukses, dialog konfirmasi aksi destruktif) |
| **Accessibility (a11y)** | Rasio kontras $\ge 4.5:1$, touch target $\ge 44\text{px}$, desktop pointer $\ge 24\text{px}$, bebas status berbasis warna semata |
| **Microcopy & Writing** | Wajib menggunakan *Sentence case* pada judul/tombol/label, `<label>` eksplisit tanpa diganti placeholder |

---

## Rubrik Audit Desain (Design Review Rubric)

Setiap implementasi UI wajib diaudit menggunakan 4 tingkat keparahan:
1. **Critical**: Kontras $< 4.5:1$, touch target $< 44\text{px}$/desktop $< 24\text{px}$, input tanpa label, aksi destruktif tanpa konfirmasi.
2. **High**: Navigasi menyimpang (misal mobile tanpa bottom nav/drawer), ALL CAPS di seluruh UI, status warna tanpa teks/ikon.
3. **Medium**: Spacing di luar 8pt grid, loading state tanpa indikator, blur bertumpuk tanpa kontras layer.
4. **Low**: Polish visual micro-spacing dan kerning.

---

## Referensi
- [Apple HIG — Foundations](https://developer.apple.com/design/human-interface-guidelines/foundations)
- [Apple HIG — Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [Apple HIG — Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Apple HIG — Components](https://developer.apple.com/design/human-interface-guidelines/components)
- [Apple HIG — Materials & Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials)
- [W3C Web Content Accessibility Guidelines (WCAG 2.1 AA)](https://www.w3.org/WAI/standards-guidelines/wcag/)
