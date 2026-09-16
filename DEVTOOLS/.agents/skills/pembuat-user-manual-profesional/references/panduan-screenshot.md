# 📸 PANDUAN PENGAMBILAN & ANOTASI SCREENSHOT USER MANUAL

Dokumen ini adalah panduan teknis operasional bagi Technical Writer / Antigravity Agent dalam mengambil, memproses, dan menyematkan screenshot nyata aplikasi ke dalam User Manual.

---

## 1. PRINSIP DASAR SCREENSHOT

### 1.1 Kapan Screenshot WAJIB Ada
Setiap prosedur di User Manual WAJIB menyertakan screenshot jika mencakup:
- [ ] Tampilan halaman baru yang pertama kali diperkenalkan
- [ ] Lokasi elemen UI yang diklik / diisi
- [ ] Hasil akhir yang diharapkan setelah prosedur selesai (konfirmasi berhasil / perubahan data)
- [ ] Pesan error atau dialog konfirmasi yang mungkin muncul
- [ ] Komponen navigasi yang mungkin membingungkan

### 1.2 Kapan Screenshot TIDAK Diperlukan
- Langkah yang hanya berupa pengetikan teks tanpa perubahan UI yang signifikan
- Prosedur berulang yang tampilan UI-nya identik dengan screenshot sebelumnya
- Deskripsi konsep / latar belakang (bukan prosedur)

---

## 2. ALUR KERJA SCREENSHOT DENGAN ANTIGRAVITY TOOLS

Gunakan salah satu dari 2 metode screenshot yang tersedia:

### 2.1 Metode A: Utility Script Otomatis (`capture_screenshots.py`)
Gunakan tool screenshot CLI standar Diskominfo:
```bash
# 1. Pre-flight check
python3 .agents/scripts/capture_screenshots.py --check

# 2. Capture screenshot dari URL aktif
python3 .agents/scripts/capture_screenshots.py -u "http://localhost:3000/login" -o "docs/screenshots/03-01-halaman-login.png"
python3 .agents/scripts/capture_screenshots.py -u "http://localhost:3000/dashboard" -o "docs/screenshots/03-03-dashboard-setelah-login.png"
```

### 2.2 Metode B: Antigravity Browser Subagent
Gunakan `browser_subagent` untuk skenario interaktif yang membutuhkan login, form submission, dan simulasi error:
```
Task: Navigasi ke [URL aplikasi], login dengan [username/password akun uji],
buka halaman [nama halaman/menu], dan ambil screenshot seluruh halaman 
dalam kondisi [state yang dimaksud: form kosong / data terisi / konfirmasi berhasil].
Kembalikan screenshot ke path: docs/screenshots/[nomor-bab]-[nomor-langkah]-[nama-deskripsi].png
```

---

## 5. STRUKTUR FOLDER OUTPUT

```
docs/
├── Laporan_Pengujian_QA.docx           # Laporan Pengujian QA resmi (.docx)
├── TEST_REPORT.md                      # Laporan Pengujian QA (Markdown)
├── Panduan_Penggunaan_Aplikasi.docx    # Dokumen User Manual resmi (.docx)
├── USER_MANUAL.md                      # Dokumen User Manual (Markdown)
└── screenshots/                         # Folder aset screenshot PNG bersama
    ├── 03-01-halaman-login.png
    ├── 03-02-tombol-login-sso.png
    ├── 03-03-dashboard-setelah-login.png
    ├── 04-01-anatomi-antarmuka.png
    ├── 05-01-daftar-data.png
    ├── 05-02-tombol-tambah-data.png
    ├── 05-03-form-tambah-data.png
    ├── 05-04-dialog-konfirmasi-hapus.png
    └── ...
```

---

## 6. CHECKLIST FINAL SEBELUM SUBMIT SCREENSHOT

Sebelum menyematkan screenshot ke dokumen, periksa:
- [ ] Resolusi minimal 1280×800px
- [ ] Format PNG, bukan JPG atau WebP
- [ ] Browser zoom 100%
- [ ] Tidak ada data sensitif / PII yang terekspos (sudah di-blur)
- [ ] Elemen yang dimaksud terfokus dan terlihat jelas
- [ ] Nama file mengikuti konvensi `[bab]-[langkah]-[deskripsi].png`
- [ ] Caption sudah ada di bawah gambar dalam format yang benar
- [ ] File tersimpan di folder `docs/screenshots/`
