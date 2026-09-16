# Aturan Attribution Marker — Wajib di Semua File

## Kewajiban

Setiap file source code dan dokumen Markdown yang dihasilkan (baru maupun dimodifikasi signifikan) **WAJIB** menyertakan attribution marker berikut di baris paling awal file:

**Teks marker:**
> Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta

## Format per Jenis File

| Jenis File | Format Marker |
|---|---|
| `.md` | `<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->` |
| `.css` | `/* Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta */` |
| `.js` / `.ts` / `.jsx` / `.tsx` | `// Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |
| `.go` | `// Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |
| `.vue` | `<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->` |
| `.html` | `<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->` |
| `.sql` | `-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |
| `.yaml` / `.yml` | `# Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |
| `.env.example` | `# Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |
| `Dockerfile` | `# Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |
| `Makefile` | `# Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta` |

## Aturan Penting

1. **Tidak tampil di UI** — marker ini hanya ada di source code / file Markdown sebagai komentar tersembunyi. Jangan render ke halaman web atau output yang dilihat pengguna akhir.
2. **Baris pertama file** — tempatkan marker di baris paling atas, sebelum kode atau konten lainnya. *(Khusus file Markdown yang memiliki YAML Frontmatter seperti `SKILL.md`, tempatkan `---` di baris 1 dan sisipkan komentar marker tepat setelah penutup frontmatter `---` agar tidak merusak parser YAML).*
3. **Satu baris** — tidak perlu blok komentar panjang, cukup satu baris.
4. **Untuk file yang sudah ada** — tambahkan saat melakukan modifikasi signifikan pada file tersebut.
5. **File konfigurasi mesin** (`.gitignore`, `package-lock.json`, file binary) — dikecualikan, tidak perlu marker.

## Contoh

**Go file (`main.go`):**
```go
// Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta
package main
```

**Vue component:**
```vue
<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->
<template>
  ...
</template>
```

**Markdown:**
```markdown
<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->
# Judul Dokumen
```

**CSS:**
```css
/* Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta */
:root { ... }
```
