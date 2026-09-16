<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->
# Design System — Panduan Komponen HIG untuk Web
> Berbasis **Apple Human Interface Guidelines** — diadaptasi untuk aplikasi web React/Vue.
> Setiap komponen di bawah mengacu pada token di folder `tokens/`.

---

## Daftar Isi

1. [Button](#1-button)
2. [Input & Form](#2-input--form)
3. [Card](#3-card)
4. [Badge & Chip](#4-badge--chip)
5. [Alert / Callout](#5-alert--callout)
6. [Navigation Bar](#6-navigation-bar)
7. [Sidebar / Nav Menu](#7-sidebar--nav-menu)
8. [Table / List](#8-table--list)
9. [Modal / Dialog](#9-modal--dialog)
10. [Toast / Notification](#10-toast--notification)
11. [Empty State](#11-empty-state)
12. [Loading State](#12-loading-state)
13. [Avatar](#13-avatar)
14. [Dark/Light Toggle](#14-darklight-toggle)

---

## 1. Button

**Prinsip HIG**: Setiap tombol harus jelas tujuannya. Gunakan satu tombol primer per konteks. Minimum touch target 44×44px.

### Variants

| Variant | Kapan Dipakai | Style |
|---|---|---|
| `primary` | Aksi utama 1 per halaman | `bg-tint` + `text-tint-foreground` |
| `secondary` | Aksi sekunder / alternatif | `bg-fill-primary` + `text-label-primary` |
| `ghost` | Aksi ringan dalam toolbar | `bg-transparent` + `text-tint` |
| `destructive` | Hapus / aksi tidak bisa dibatalkan | `bg-error` + `text-white` |
| `outline` | Aksi form / filter | `border-separator` + `text-label-primary` |

### CSS Pattern (Tailwind)

```html
<!-- Primary -->
<button class="
  inline-flex items-center justify-center gap-2
  h-btn-md px-6
  bg-tint hover:bg-tint-hover active:bg-tint-active
  text-tint-foreground font-semibold text-md
  rounded-md
  shadow-xs
  transition-all duration-fast ease-standard
  focus-visible:outline-none focus-visible:shadow-input-focus
  disabled:opacity-40 disabled:cursor-not-allowed
">
  Label
</button>

<!-- Secondary -->
<button class="
  inline-flex items-center justify-center gap-2
  h-btn-md px-6
  bg-fill-primary hover:bg-fill-secondary
  text-label-primary font-medium text-md
  rounded-md border border-separator
  transition-all duration-fast ease-standard
  focus-visible:outline-none focus-visible:shadow-input-focus
  disabled:opacity-40 disabled:cursor-not-allowed
">
  Label
</button>

<!-- Destructive -->
<button class="
  inline-flex items-center justify-center gap-2
  h-btn-md px-6
  bg-error hover:opacity-90 active:opacity-80
  text-white font-semibold text-md
  rounded-md shadow-xs
  transition-all duration-fast ease-standard
">
  Hapus
</button>
```

### Ukuran

| Size | Height | Padding X | Font | Class |
|---|---|---|---|---|
| `sm` | `h-btn-sm` (28px) | `px-4` | `text-sm` | Compact toolbar |
| `md` | `h-btn-md` (36px) | `px-6` | `text-md` | Default |
| `lg` | `h-btn-lg` (44px) | `px-8` | `text-lg` | Primary CTA |

---

## 2. Input & Form

**Prinsip HIG**: Input harus memiliki label yang jelas, placeholder hanya sebagai petunjuk tambahan (bukan pengganti label). Selalu tampilkan pesan error di bawah field.

### Text Input

```html
<div class="flex flex-col gap-2">
  <!-- Label -->
  <label class="text-sm font-medium text-label-primary" for="nama">
    Nama Lengkap
  </label>

  <!-- Input -->
  <input
    id="nama"
    type="text"
    placeholder="Masukkan nama lengkap"
    class="
      h-input px-4
      bg-input-bg
      border border-input-border
      text-label-primary text-xl placeholder:text-label-tertiary
      rounded-md
      transition-all duration-fast ease-standard
      focus:outline-none focus:border-input-borderFocus focus:shadow-input-focus
      disabled:opacity-40 disabled:cursor-not-allowed
    "
  />

  <!-- Pesan bantu (opsional) -->
  <p class="text-xs text-label-secondary">
    Gunakan nama sesuai KTP.
  </p>

  <!-- Pesan error (tampilkan bila ada error) -->
  <p class="text-xs text-error flex items-center gap-1">
    <svg>...</svg> Nama tidak boleh kosong.
  </p>
</div>
```

### Select / Dropdown

```html
<select class="
  h-input w-full px-4
  bg-input-bg
  border border-input-border
  text-label-primary text-xl
  rounded-md
  appearance-none
  focus:outline-none focus:border-input-borderFocus focus:shadow-input-focus
">
  <option value="">Pilih opsi...</option>
  <option value="1">Opsi 1</option>
</select>
```

### Textarea

```html
<textarea
  rows="4"
  class="
    w-full px-4 py-3
    bg-input-bg border border-input-border
    text-label-primary text-xl placeholder:text-label-tertiary
    rounded-md resize-y
    focus:outline-none focus:border-input-borderFocus focus:shadow-input-focus
  "
  placeholder="Masukkan keterangan..."
></textarea>
```

---

## 3. Card

**Prinsip HIG**: Card adalah "permukaan" yang mengangkat konten dari background. Gunakan shadow minimal, radius konsisten.

```html
<!-- Card Standar -->
<div class="
  bg-bg-elevated rounded-lg
  shadow-card
  border border-separator
  p-6
">
  <!-- Header -->
  <div class="flex items-center justify-between mb-4">
    <h3 class="text-headline font-semibold text-label-primary">Judul Card</h3>
    <button class="text-tint text-sm font-medium">Lihat Semua</button>
  </div>

  <!-- Content -->
  <div>...</div>
</div>

<!-- Card Interaktif (klik) -->
<div class="
  bg-bg-elevated rounded-lg shadow-card border border-separator p-6
  cursor-pointer
  hover:shadow-md hover:border-tint/30
  active:scale-[0.99]
  transition-all duration-fast ease-standard
">
  ...
</div>
```

---

## 4. Badge & Chip

**Prinsip HIG**: Badge menyampaikan status atau kategori secara visual. Gunakan warna sistem, bukan warna acak.

```html
<!-- Status Badge -->
<span class="
  inline-flex items-center gap-1
  px-2 py-0.5
  bg-success/15 text-system-green
  text-caption-2 font-semibold tracking-wide uppercase
  rounded-full
">
  <span class="w-1.5 h-1.5 rounded-full bg-system-green"></span>
  Aktif
</span>

<!-- Chip Filter -->
<button class="
  inline-flex items-center gap-2
  px-3 py-1
  bg-tint-subtle text-tint
  text-sm font-medium
  rounded-full border border-tint/20
  hover:bg-tint hover:text-tint-foreground
  transition-all duration-fast ease-standard
">
  Semua
  <svg>...</svg>
</button>
```

### Warna Status Standar

| Status | Color Token | Bg Token |
|---|---|---|
| Aktif / Sukses | `text-system-green` | `bg-success/15` |
| Error / Bahaya | `text-error` | `bg-error/15` |
| Peringatan | `text-system-orange` | `bg-warning/15` |
| Info | `text-info` | `bg-info/15` |
| Nonaktif | `text-label-tertiary` | `bg-fill-tertiary` |

---

## 5. Alert / Callout

**Prinsip HIG**: Alert menyampaikan informasi penting yang tidak bisa diabaikan. Gunakan ikon + warna sistem.

```html
<!-- Info Alert -->
<div class="
  flex gap-3 p-4
  bg-info-bg border border-info/20
  rounded-lg
">
  <svg class="w-5 h-5 text-info flex-shrink-0 mt-0.5">...</svg>
  <div>
    <p class="text-md font-semibold text-info">Judul Pesan</p>
    <p class="text-base text-label-secondary mt-1">Deskripsi detail pesan informasi di sini.</p>
  </div>
</div>

<!-- Error Alert -->
<div class="flex gap-3 p-4 bg-error-bg border border-error/20 rounded-lg">
  <svg class="w-5 h-5 text-error flex-shrink-0 mt-0.5">...</svg>
  <div>
    <p class="text-md font-semibold text-error">Terjadi Kesalahan</p>
    <p class="text-base text-label-secondary mt-1">Pesan error detail.</p>
  </div>
</div>
```

---

## 6. Navigation Bar

**Prinsip HIG**: Navbar selalu terlihat, transparan dengan efek blur (vibrancy), dan tidak mendominasi konten.

```html
<nav class="
  fixed top-0 left-0 right-0 z-navbar
  h-navbar px-8
  flex items-center justify-between
  bg-nav-bg backdrop-blur-navbar
  border-b border-nav-border
  shadow-navbar
">
  <!-- Brand Unit Resmi: Logo Jogja + Nama Aplikasi -->
  <a href="/dashboard" class="flex items-center gap-3 group focus:outline-none">
    <img 
      src="/assets/logo-jogja.svg" 
      alt="Logo Pemerintah Kota Yogyakarta" 
      class="h-10 w-auto aspect-[183.97/255.19] transition-transform duration-fast group-hover:scale-105" 
    />
    <div class="flex flex-col">
      <span class="text-headline font-semibold text-label-primary tracking-tight leading-tight">
        Nama Aplikasi
      </span>
      <span class="text-[11px] font-medium text-label-tertiary leading-none">
        Pemerintah Kota Yogyakarta
      </span>
    </div>
  </a>

  <!-- Actions -->
  <div class="flex items-center gap-2">
    <!-- Dark/Light Toggle -->
    <button id="theme-toggle" class="
      w-9 h-9 flex items-center justify-center rounded-full
      bg-fill-primary hover:bg-fill-secondary
      text-label-secondary
      transition-all duration-fast ease-standard
    ">
      <svg class="w-5 h-5">...</svg>
    </button>

    <!-- Avatar -->
    <button class="w-9 h-9 rounded-full overflow-hidden border-2 border-separator">
      <img src="/avatar.jpg" alt="User" />
    </button>
  </div>
</nav>
```

---

## 6.1 Brand Unit Resmi Pemkot Yogyakarta (`AppBrand`)

Komponen brand terstandarisasi menggabungkan **Logo Resmi Vektor Kota Yogyakarta (`logo-jogja.svg`)** dan **Nama Aplikasi** (plus subtitle OPD). Wajib digunakan pada **Sidebar Header**, **Navbar Publik**, dan **Halaman Login SSO**.

### Implementasi React / TypeScript (`AppBrand.tsx`):
```tsx
import React from 'react';
import logoJogja from '@/assets/logo-jogja.svg';

interface AppBrandProps {
  appName?: string;
  subTitle?: string;
  compact?: boolean;
  className?: string;
}

export const AppBrand: React.FC<AppBrandProps> = ({
  appName = "Nama Aplikasi",
  subTitle = "Pemerintah Kota Yogyakarta",
  compact = false,
  className = ""
}) => {
  return (
    <div className={`flex items-center gap-3 ${className}`}>
      <img 
        src={logoJogja} 
        alt="Logo Pemkot Yogyakarta" 
        className={`${compact ? 'h-8' : 'h-10'} w-auto aspect-[183.97/255.19] drop-shadow-sm`}
      />
      {!compact && (
        <div className="flex flex-col">
          <span className="text-headline font-semibold text-label-primary tracking-tight leading-tight">
            {appName}
          </span>
          <span className="text-[11px] font-medium text-label-tertiary leading-none">
            {subTitle}
          </span>
        </div>
      )}
    </div>
  );
};
```

### Implementasi Vue 3 (`AppBrand.vue`):
```vue
<template>
  <div class="flex items-center gap-3" :class="className">
    <img 
      :src="logoJogja" 
      alt="Logo Pemkot Yogyakarta" 
      :class="[compact ? 'h-8' : 'h-10', 'w-auto aspect-[183.97/255.19] drop-shadow-sm']"
    />
    <div v-if="!compact" class="flex flex-col">
      <span class="text-headline font-semibold text-label-primary tracking-tight leading-tight">
        {{ appName }}
      </span>
      <span class="text-[11px] font-medium text-label-tertiary leading-none">
        {{ subTitle }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import logoJogja from '@/assets/logo-jogja.svg';

withDefaults(defineProps<{
  appName?: string;
  subTitle?: string;
  compact?: boolean;
  className?: string;
}>(), {
  appName: 'Nama Aplikasi',
  subTitle: 'Pemerintah Kota Yogyakarta',
  compact: false,
  className: ''
});
</script>
```

---

## 7. Sidebar / Nav Menu

```html
<aside class="
  w-64 h-full
  bg-bg-secondary
  border-r border-separator
  flex flex-col
  p-4 gap-1
">
  <!-- Nav Item Aktif -->
  <a href="/dashboard" class="
    flex items-center gap-3 px-3 py-2
    bg-tint-subtle text-tint
    rounded-md
    text-md font-semibold
    transition-all duration-fast ease-standard
  ">
    <svg class="w-5 h-5">...</svg>
    Dashboard
  </a>

  <!-- Nav Item Normal -->
  <a href="/data" class="
    flex items-center gap-3 px-3 py-2
    text-label-secondary hover:bg-fill-primary hover:text-label-primary
    rounded-md
    text-md font-medium
    transition-all duration-fast ease-standard
  ">
    <svg class="w-5 h-5">...</svg>
    Data
  </a>

  <!-- Separator -->
  <div class="my-2 border-t border-separator"></div>

  <!-- Section Label -->
  <p class="px-3 py-1 text-caption-2 font-semibold tracking-wider uppercase text-label-tertiary">
    Pengaturan
  </p>
</aside>
```

---

## 8. Table / List

**Prinsip HIG**: Tabel harus mudah di-scan. Gunakan alternating row color tipis atau hover state. Sticky header.

```html
<div class="border border-table-border rounded-lg overflow-hidden shadow-card">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-table-headerBg border-b border-table-border">
        <th class="px-4 py-3 text-caption-2 font-semibold tracking-wide uppercase text-label-secondary">
          Nama
        </th>
        <th class="px-4 py-3 text-caption-2 font-semibold tracking-wide uppercase text-label-secondary">
          Status
        </th>
        <th class="px-4 py-3 text-caption-2 font-semibold tracking-wide uppercase text-label-secondary">
          Aksi
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-table-border">
      <tr class="
        bg-bg-elevated
        hover:bg-table-rowHover
        transition-colors duration-fast ease-standard
      ">
        <td class="px-4 py-3 text-xl text-label-primary font-medium">Nama Data</td>
        <td class="px-4 py-3">
          <span class="badge badge-success">Aktif</span>
        </td>
        <td class="px-4 py-3">
          <button class="btn btn-ghost btn-sm">Edit</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 9. Modal / Dialog

**Prinsip HIG**: Modal memblokir konten — gunakan hanya untuk aksi yang memerlukan keputusan. Selalu ada tombol tutup. Animasi masuk dari bawah (sheet) atau scale-in (alert).

```html
<!-- Overlay -->
<div class="fixed inset-0 z-modal bg-bg-overlay backdrop-blur-sm animate-fade-in">

  <!-- Dialog -->
  <div class="
    fixed inset-x-4 top-1/2 -translate-y-1/2
    max-w-md mx-auto
    bg-bg-elevated rounded-xl shadow-modal
    border border-separator
    animate-scale-in
  ">
    <!-- Header -->
    <div class="flex items-center justify-between px-6 pt-5 pb-4 border-b border-separator">
      <h2 class="text-headline font-semibold text-label-primary">Judul Dialog</h2>
      <button class="w-8 h-8 flex items-center justify-center rounded-full bg-fill-primary text-label-secondary">
        ✕
      </button>
    </div>

    <!-- Body -->
    <div class="px-6 py-4">
      <p class="text-xl text-label-secondary">Isi konten modal di sini.</p>
    </div>

    <!-- Footer -->
    <div class="flex gap-3 justify-end px-6 pb-5 pt-4 border-t border-separator">
      <button class="btn btn-secondary">Batal</button>
      <button class="btn btn-primary">Konfirmasi</button>
    </div>
  </div>
</div>
```

---

## 10. Toast / Notification

**Prinsip HIG**: Toast tampil sebentar lalu menghilang. Posisi kanan bawah. Jangan tumpuk lebih dari 3.

```html
<!-- Toast Container -->
<div class="fixed bottom-6 right-6 z-toast flex flex-col gap-3">

  <!-- Toast Item -->
  <div class="
    flex items-start gap-3 p-4
    bg-bg-elevated border border-separator
    rounded-lg shadow-lg
    min-w-72 max-w-sm
    animate-slide-up
  ">
    <svg class="w-5 h-5 text-system-green flex-shrink-0 mt-0.5">...</svg>
    <div class="flex-1">
      <p class="text-md font-semibold text-label-primary">Data berhasil disimpan</p>
      <p class="text-sm text-label-secondary mt-0.5">Perubahan telah tersimpan.</p>
    </div>
    <button class="text-label-tertiary hover:text-label-primary">✕</button>
  </div>

</div>
```

---

## 11. Empty State

**Prinsip HIG**: Tampilkan empty state yang informatif + satu aksi yang jelas. Jangan biarkan halaman kosong.

```html
<div class="flex flex-col items-center justify-center py-20 text-center gap-4">
  <!-- Ilustrasi / Icon -->
  <div class="w-16 h-16 rounded-2xl bg-fill-tertiary flex items-center justify-center">
    <svg class="w-8 h-8 text-label-tertiary">...</svg>
  </div>

  <div class="max-w-xs">
    <h3 class="text-headline font-semibold text-label-primary">Belum Ada Data</h3>
    <p class="text-base text-label-secondary mt-2">
      Data yang Anda cari belum tersedia. Tambahkan data pertama Anda untuk memulai.
    </p>
  </div>

  <button class="btn btn-primary">+ Tambah Data</button>
</div>
```

---

## 12. Loading State

### Skeleton Loading (HIG: prefer skeleton over spinner untuk konten)

```html
<div class="animate-shimmer bg-gradient-to-r from-fill-tertiary via-fill-secondary to-fill-tertiary
            bg-[length:200%_100%] rounded-md h-4 w-3/4">
</div>
```

### Spinner (untuk aksi tombol)

```html
<button class="btn btn-primary" disabled>
  <svg class="w-4 h-4 animate-spin text-current">...</svg>
  Menyimpan...
</button>
```

---

## 13. Avatar

```html
<!-- Avatar dengan inisial -->
<div class="
  w-10 h-10 rounded-full
  bg-tint-subtle text-tint
  flex items-center justify-center
  text-md font-semibold
  flex-shrink-0
">
  AS
</div>

<!-- Avatar dengan foto -->
<img
  src="/foto.jpg"
  alt="Nama Pengguna"
  class="w-10 h-10 rounded-full object-cover border-2 border-separator"
/>
```

---

## 14. Dark/Light Toggle

```html
<!-- Toggle Button di Navbar -->
<button
  id="theme-toggle"
  onclick="toggleTheme()"
  class="
    w-9 h-9 flex items-center justify-center
    rounded-full bg-fill-primary hover:bg-fill-secondary
    text-label-secondary hover:text-label-primary
    transition-all duration-fast ease-standard
    focus-visible:outline-none focus-visible:shadow-input-focus
  "
  aria-label="Ganti tema"
>
  <!-- Ikon Matahari (light mode) -->
  <svg data-icon="sun" class="w-5 h-5">...</svg>

  <!-- Ikon Bulan (dark mode, hidden by default) -->
  <svg data-icon="moon" class="w-5 h-5 hidden">...</svg>
</button>
```

```javascript
// theme.js — letakkan di main.js / App.vue / _app.jsx
function initTheme() {
  const saved = localStorage.getItem('theme') || 'light'; // default: light
  document.documentElement.setAttribute('data-theme', saved);
  updateIcon(saved);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateIcon(next);
}

function updateIcon(theme) {
  document.querySelector('[data-icon="sun"]').classList.toggle('hidden', theme === 'dark');
  document.querySelector('[data-icon="moon"]').classList.toggle('hidden', theme === 'light');
}

initTheme();
```

---

---

## 15. Komponen 5 Modul Pengaturan Sistem (System Settings)

### 15.1 Form Tambah / Edit Pengguna (User Management Form)
Sesuai standar antarmuka sinkronisasi SSO JSS:

```html
<!-- Modal Form Tambah Pengguna -->
<div class="fixed inset-0 z-modal bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
  <div class="bg-bg-primary rounded-2xl shadow-modal w-full max-w-lg border border-separator overflow-hidden animate-scale-in">
    <!-- Header Modal -->
    <div class="px-8 pt-8 pb-4 text-center">
      <h3 class="text-xl font-bold text-label-primary tracking-tight">Form Tambah Pengguna</h3>
    </div>

    <!-- Body Form -->
    <form class="px-8 pb-8 space-y-5">
      <!-- ID JSS Input (Wajib) -->
      <div>
        <label class="block text-sm font-semibold text-label-primary mb-2">
          ID JSS <span class="text-danger">*</span>
        </label>
        <input 
          type="text" 
          placeholder="ID JSS" 
          required 
          class="w-full px-4 py-3 bg-bg-secondary border border-separator rounded-xl text-label-primary placeholder-label-tertiary focus:outline-none focus:border-tint focus:ring-2 focus:ring-tint/20 transition-all text-sm"
        />
      </div>

      <!-- Nama Lengkap (Terisi Otomatis) -->
      <div>
        <label class="block text-sm font-semibold text-label-primary mb-2">
          Nama Lengkap
        </label>
        <input 
          type="text" 
          placeholder="Nama lengkap (terisi otomatis)" 
          readonly 
          class="w-full px-4 py-3 bg-fill-tertiary border border-separator rounded-xl text-label-secondary placeholder-label-tertiary cursor-not-allowed text-sm"
        />
      </div>

      <!-- Role Pengguna Dropdown (Wajib) -->
      <div>
        <label class="block text-sm font-semibold text-label-primary mb-2">
          Role Pengguna <span class="text-danger">*</span>
        </label>
        <div class="relative">
          <select 
            required 
            class="w-full px-4 py-3 bg-bg-secondary border border-separator rounded-xl text-label-primary appearance-none focus:outline-none focus:border-tint focus:ring-2 focus:ring-tint/20 transition-all text-sm pr-10"
          >
            <option value="" disabled selected>-- Pilih Role Pengguna --</option>
            <option value="superadmin">Super Admin</option>
            <option value="admin">Admin</option>
            <option value="operator">Operator</option>
            <option value="pengawas">Pengawas (Read-Only)</option>
          </select>
          <div class="absolute inset-y-0 right-0 flex items-center px-4 pointer-events-none text-label-tertiary">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center justify-end gap-3 pt-4">
        <button 
          type="button" 
          class="px-6 py-2.5 rounded-xl bg-fill-secondary hover:bg-fill-primary text-label-secondary font-medium transition-all text-sm"
        >
          Batal
        </button>
        <button 
          type="submit" 
          class="px-6 py-2.5 rounded-xl bg-tint hover:bg-tint-hover text-white font-medium shadow-sm transition-all flex items-center gap-2 text-sm"
        >
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l6-6a1 1 0 00-1.414-1.414L11 12.586l-3.293-3.293z"></path></svg>
          Simpan
        </button>
      </div>
    </form>
  </div>
</div>
```

---

### 15.2 Matriks Hak Akses Modul (Module Permission Matrix Grid)
Menyediakan pengaturan izin berjenjang per role (Lihat, Tambah, Ubah, Hapus) dengan switch toggle per-baris dan master kategori:

```html
<div class="bg-bg-primary rounded-2xl border border-separator shadow-card p-6 space-y-6">
  <!-- Toolbar Pemilihan Role -->
  <div class="flex items-center justify-between gap-4 pb-4 border-b border-separator">
    <div class="w-72">
      <label class="block text-xs font-semibold text-label-tertiary uppercase tracking-wider mb-1.5">Pilih Role Target</label>
      <select class="w-full px-4 py-2.5 bg-bg-secondary border border-separator rounded-xl text-label-primary text-sm font-medium focus:outline-none focus:border-tint">
        <option value="superadmin">Super Admin</option>
        <option value="admin" selected>Admin</option>
        <option value="operator">Operator</option>
        <option value="pengawas">Pengawas (Read-Only)</option>
      </select>
    </div>
    <button class="px-6 py-2.5 bg-tint hover:bg-tint-hover text-white rounded-xl text-sm font-semibold shadow-sm transition-all flex items-center gap-2">
      <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"></path></svg>
      Simpan Perubahan
    </button>
  </div>

  <!-- Header Matriks Kolom -->
  <div class="overflow-x-auto">
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="border-b border-separator text-xs uppercase text-label-tertiary font-semibold tracking-wider">
          <th class="py-3 px-4 w-2/5">Menu & Submenu</th>
          <th class="py-3 px-4 text-center">Lihat</th>
          <th class="py-3 px-4 text-center">Tambah</th>
          <th class="py-3 px-4 text-center">Ubah</th>
          <th class="py-3 px-4 text-center">Hapus</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-separator text-sm">
        <!-- Kategori Group Header 1 -->
        <tr class="bg-fill-tertiary/60 font-semibold text-label-primary">
          <td class="py-3 px-4 flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-tint"></span>
            DASHBOARD
          </td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
        </tr>
        <!-- Submenu Item -->
        <tr class="hover:bg-fill-primary/50 transition-colors">
          <td class="py-3 px-4 pl-8 text-label-secondary flex items-center gap-2">
            <svg class="w-4 h-4 text-label-tertiary">...</svg>
            Beranda Utama
          </td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
        </tr>

        <!-- Kategori Group Header 2 -->
        <tr class="bg-fill-tertiary/60 font-semibold text-label-primary">
          <td class="py-3 px-4 flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-secondary"></span>
            SYSTEM CONFIG
          </td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" class="toggle-switch" /></td>
        </tr>
        <!-- Submenu Item -->
        <tr class="hover:bg-fill-primary/50 transition-colors">
          <td class="py-3 px-4 pl-8 text-label-secondary flex items-center gap-2">
            <svg class="w-4 h-4 text-label-tertiary">...</svg>
            Manajemen Pengguna
          </td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" checked class="toggle-switch" /></td>
          <td class="py-3 px-4 text-center"><input type="checkbox" class="toggle-switch" /></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

---

### 15.3 Manajemen Menu Sidebar (Sidebar Navigation Management Tree)
Pengaturan hierarki menu, sub-menu, URL route, icon, badge status, dan toggle:

```html
<div class="space-y-4">
  <!-- Toolbar Atas -->
  <div class="flex items-center justify-between">
    <h3 class="text-lg font-bold text-label-primary">Manajemen Menu Navigasi</h3>
    <div class="flex items-center gap-2">
      <button class="btn btn-secondary text-xs">+ Tambah Kategori</button>
      <button class="btn btn-primary text-xs">+ Tambah Menu</button>
    </div>
  </div>

  <!-- Container Tree Menu -->
  <div class="bg-bg-primary rounded-2xl border border-separator shadow-card p-4 space-y-3">
    <!-- Kategori Group Item -->
    <div class="border border-separator rounded-xl p-3 bg-bg-secondary">
      <div class="flex items-center justify-between pb-2 border-b border-separator/60">
        <div class="flex items-center gap-2 font-bold text-xs uppercase tracking-wider text-label-secondary">
          <span class="cursor-grab text-label-tertiary">⋮⋮</span>
          Kategori: MASTER DATA
        </div>
        <div class="flex items-center gap-1">
          <button class="p-1 hover:bg-fill-secondary rounded text-tint text-xs font-semibold">+ Sub-Menu</button>
          <button class="p-1 hover:bg-fill-secondary rounded text-label-tertiary">✏️</button>
          <button class="p-1 hover:bg-fill-secondary rounded text-danger">🗑️</button>
        </div>
      </div>

      <!-- Nested Submenu List -->
      <div class="pt-2 pl-4 space-y-2">
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-bg-primary border border-separator hover:border-tint/40 transition-all">
          <div class="flex items-center gap-3">
            <span class="cursor-grab text-label-tertiary text-xs">⋮⋮</span>
            <div class="w-7 h-7 rounded-lg bg-tint-subtle text-tint flex items-center justify-center text-xs">
              📁
            </div>
            <div>
              <div class="text-sm font-semibold text-label-primary">Kategori Kendaraan</div>
              <div class="text-[11px] text-label-tertiary">URL: /master/kategori-kendaraan</div>
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span class="badge badge-success text-[10px]">Aktif</span>
            <input type="checkbox" checked class="toggle-switch" />
            <button class="text-label-tertiary hover:text-label-primary text-xs">✏️</button>
            <button class="text-danger hover:text-danger/80 text-xs">🗑️</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## Prinsip Umum (Ringkasan Standar Apple HIG & WCAG)

| Aspek | Aturan Standar | Catatan Implementasi |
|---|---|---|
| **Warna & Kontras** | Selalu pakai semantic token (`--color-label-primary`, bukan `#000`) | Kontras body $\ge 4.5:1$, large text $\ge 3:1$ (WCAG AA/AAA) |
| **Bebas Warna Tunggal** | Dilarang hanya mengandalkan warna untuk status error/sukses | Wajib sertakan teks label atau ikon pendukung |
| **Spacing Grid** | Kelipatan 4px atau 8px murni (`var(--space-*)`) | Dilarang nilai sembarang seperti `13px` atau `19px` |
| **Radius Squircle** | Konsisten per konteks: button `rounded-md`, card `rounded-lg`, modal `rounded-xl` | Halus tanpa sudut tajam kaku |
| **Touch/Click Target** | Mobile $\ge 44\times 44\text{px}$, Desktop pointer $\ge 24\times 24\text{px}$ | Gunakan token `h-touch-min` / `min-h-touch` |
| **Focus State & A11y** | Wajib ada `focus-visible:ring-2 focus-visible:ring-focus-ring` | Keyboard navigation & screen reader support |
| **Microcopy & Writing** | Gunakan **Sentence case** ("Simpan perubahan", "Tambah pengguna") | Hindari ALL CAPS atau Title Case di semua tombol/label |
| **Form Inputs** | Wajib ada `<label>` eksplisit; placeholder bukan label | Error text wajib muncul tepat di bawah input |
| **Liquid Glass & Blur** | Layer fungsional (navbar, modal) terpisah dari layer konten | Gunakan `backdropBlur-navbar` dipadu `bg-glass-regular` & dimming layer |
| **Feedback & Destruktif**| Setiap aksi punya feedback visual; aksi destruktif wajib modal konfirmasi | Konfirmasi jelas konsekuensi hapus/mutasi |
| **Motion & A11y** | Durasi $\le 450\text{ms}$, dukung `@media (prefers-reduced-motion)` | Nonaktifkan animasi berlebih saat diatur pengguna |
| **Dark Mode** | Gunakan 8 tema CSS variables anti-color clash | Zero hardcoded hex colors di markup komponen |

---

## 15. Checklist Audit & Review Kualitas Desain (Design Review Rubric)

Gunakan rubrik berikut untuk memastikan kepatuhan tampilan antarmuka sebelum tahap QA:

### Tingkat Keparahan Temuan Desain (Severity Levels):
1. **Critical (Wajib Diperbaiki Segera)**:
   - Pelanggaran kontras teks ($< 4.5:1$ pada teks biasa).
   - Touch target mobile $< 44\times 44\text{px}$ atau desktop $< 24\times 24\text{px}$.
   - Ketiadaan label formulir (hanya mengandalkan placeholder).
   - Aksi destruktif langsung tereksekusi tanpa dialog konfirmasi.
2. **High (Friction Tinggi)**:
   - Navigasi tidak konsisten antara mobile (bottom nav/drawer) dan desktop (sidebar).
   - Teks UI menggunakan ALL CAPS yang menyulitkan pembacaan.
   - Status error/warning hanya menggunakan warna tanpa ikon atau teks deskriptif.
3. **Medium (Inkonsistensi Visual)**:
   - Spacing melanggar grid 8pt (misal padding ganjil).
   - Loading state tidak memiliki skeleton/spinner yang jelas saat fetching data.
   - Blur/glassmorphism bertumpuk tanpa pemisahan kontras layer yang jelas.
4. **Low (Polish)**:
   - Sedikit ketidaksesuaian kerning/letter-spacing pada headline besar.
   - Minor micro-animation easing yang kurang halus.

