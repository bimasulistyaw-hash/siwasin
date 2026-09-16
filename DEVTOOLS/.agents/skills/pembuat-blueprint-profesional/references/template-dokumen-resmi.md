<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->
# Template Dokumen Blueprint Resmi — [Nama Produk/Sistem]

> Ini adalah versi **formal** dari Blueprint.md — isi requirement (Bagian A/B/C) harus identik, hanya penyajian yang berbeda: ditambah sampul, bahasa pengesahan, dan halaman tanda tangan. Dokumen ini wajib disimpan di dalam folder **`docs/`** (contoh: `docs/Dokumen_Blueprint_Resmi.docx` atau `docs/Dokumen_Blueprint_Resmi.md`) atau dibuat sebagai **Google Docs** (melalui koneksi Google Drive MCP Antigravity). Gunakan gaya dokumen formal/profesional: heading rapi, penomoran konsisten, tabel untuk daftar requirement, tanpa lampiran mentah wawancara.

## Lokasi Penyimpanan File
- Path Berkas: `docs/Dokumen_Blueprint_Resmi.docx` (atau `docs/Dokumen_Blueprint_Resmi.md`)
- Versi Revisi: `docs/Dokumen_Blueprint_Resmi_v2.docx`

---

## Struktur dokumen

### 1. Halaman Sampul
- Judul: "DOKUMEN BLUEPRINT PROYEK — [Nama Produk/Sistem]"
- Subjudul: "Kesepakatan Ruang Lingkup & Spesifikasi antara [OPD Pemohon] dan Dinas Komunikasi dan Informatika Kota Yogyakarta"
- Kode Dokumen, Versi, Tanggal, Status (DRAFT/DISETUJUI)

### 2. Halaman Pengesahan (Ringkas)
- Pernyataan singkat bahwa kedua pihak menyetujui ruang lingkup, requirement, dan definisi selesai (Definition of Done) yang tercantum dalam dokumen ini sebagai acuan pengerjaan proyek.
- Catatan: dokumen ini **bukan** nasihat hukum baku — sarankan pengguna agar ditinjau oleh pihak legal internal sebelum ditandatangani jika nilai proyek besar atau berisiko tinggi.
- Pernyataan referensi: *"Dokumen ini merujuk pada Blueprint.md versi [x] sebagai spesifikasi teknis lengkap yang menjadi bagian tak terpisahkan dari kesepakatan ini."*

### 3. Ringkasan Eksekutif
Sama seperti Bagian 2 Blueprint.md — masalah, solusi, pengguna, nilai bisnis, ukuran sukses, timeline.

### 4. Ruang Lingkup yang Disepakati
- In-Scope dan Out-of-Scope (dari Bagian A.4 Blueprint) ditulis eksplisit sebagai batas tanggung jawab developer — ini bagian paling penting secara kontraktual, tulis jelas dan tidak ambigu.
- Tegaskan: perubahan lingkup di luar yang tercantum di sini memerlukan adendum/persetujuan tertulis baru (change request), bukan otomatis termasuk.

### 5. Requirement Bisnis & Tujuan (ringkas dari Bagian A)
- Tujuan bisnis & KPI (A.3), Kebutuhan Bisnis (A.6) — tabel ID tetap dipertahankan agar traceable ke Blueprint.md.

### 6. Fitur & Acceptance Criteria (ringkas dari Bagian B)
- Daftar fitur (B.7.1) dengan prioritas MoSCoW dan acceptance criteria inti — ini yang menjadi acuan "selesai/tidak selesai" secara kontraktual.

### 7. Spesifikasi Teknis Kunci (ringkas dari Bagian C)
- Functional & non-functional requirement penting (C.2–C.3), constraint teknis (C.7), Definition of Done (C.8).
- Tidak perlu semua detail SRS granular — cukup yang relevan sebagai acuan penerimaan (acceptance) proyek. Detail teknis penuh tetap di Blueprint.md untuk keperluan development.

### 8. Ketentuan Tambahan
- Timeline/milestone (jika dibahas saat wawancara)
- Mekanisme perubahan lingkup (change request): setiap perubahan scope wajib diajukan secara tertulis dan disetujui kedua pihak sebelum dilaksanakan.
- Referensi ke Blueprint.md sebagai lampiran teknis: *"Dokumen ini merujuk pada Blueprint.md versi [x] sebagai spesifikasi teknis lengkap yang menjadi bagian tak terpisahkan dari kesepakatan ini."*

### 9. Riwayat Revisi
Sama seperti Blueprint.md — tabel versi, tanggal, deskripsi perubahan, penulis.

### 10. Halaman Persetujuan & Tanda Tangan

> **PENTING**: Ini adalah bagian terakhir dokumen dan wajib selalu ada. Sertakan pernyataan persetujuan dan blok tanda tangan dua kolom: kiri = Pihak Pemohon (OPD, min. Kepala Bidang), kanan = Kabid Sistem Informasi dan Statistik Diskominfo. Format tanda tangan mengikuti standar surat dinas Pemkot Yogyakarta: jabatan di atas, ruang tanda tangan, nama lengkap, NIP, dan ruang stempel di bawah nama.

Gunakan template blok tanda tangan berikut secara **verbatim** saat menyusun dokumen resmi:

---

```
PERSETUJUAN DAN PENGESAHAN DOKUMEN

Dengan ditandatanganinya dokumen ini, kedua pihak menyatakan telah membaca,
memahami, dan menyetujui seluruh isi Dokumen Blueprint Proyek [Nama Sistem]
sebagai acuan resmi pengembangan dan penerimaan sistem.

Yogyakarta, [Tanggal Bulan Tahun]


Pihak Pemohon,                          Pihak Pengembang,
[Jabatan — minimal Kepala Bidang]       Kepala Bidang Sistem Informasi
[Nama OPD / Instansi]                   dan Statistik Diskominfo
                                         Kota Yogyakarta




_____________________________           _____________________________
[Nama Lengkap]                          Aan Suprobo, S.Kom.
NIP. [NIP Pemohon]                      NIP. 19810904 200604 1 006


Mengetahui,
[Jabatan Atasan — mis. Kepala Dinas / Sekretaris Dinas OPD]
[Nama OPD / Instansi]




_____________________________
[Nama Lengkap Atasan]
NIP. [NIP Atasan]
```

---

**Catatan pengisian tanda tangan:**
- **Pihak Pemohon**: Pejabat yang menandatangani dari sisi OPD pemohon minimal setingkat **Kepala Bidang** yang membawahi kebutuhan sistem ini. Jika nilai proyek strategis atau lintas bidang, pertimbangkan level **Kepala Dinas / Sekretaris Dinas**.
- **Pihak Pengembang**: Selalu **Kepala Bidang Sistem Informasi dan Statistik** Dinas Komunikasi dan Informatika Kota Yogyakarta.
- **Kolom Mengetahui**: Opsional — tambahkan jika diperlukan validasi hierarki atasan dari pihak pemohon.
- Stempel dinas masing-masing instansi ditempelkan di area bawah tanda tangan sesuai kewenangan.
- Dokumen ditandatangani dalam **rangkap 2** (satu untuk OPD pemohon, satu untuk Diskominfo).

---

## Gaya penulisan
- Bahasa Indonesia formal, kalimat lugas, hindari jargon tanpa penjelasan.
- Setiap requirement/fitur yang disebut tetap mencantumkan ID yang sama dengan Blueprint.md (`BR-xx`, `PRD-xx`, `SRS-F-xx`, dst.) agar dua dokumen tetap bisa saling dirujuk.
- Dokumen ini untuk pengesahan lingkup & penerimaan. Detail teknis penuh tetap tinggal di `Blueprint.md`.
- Halaman tanda tangan (Seksi 10) **wajib selalu ada** — tidak boleh dihilangkan meskipun dokumen berstatus DRAFT (tandai dengan watermark "DRAFT — BELUM BERLAKU" jika belum ditandatangani).
