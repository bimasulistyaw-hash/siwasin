# 📋 FORMULIR UJI TERIMA PENGGUNA RESMI (USER ACCEPTANCE TESTING - UAT)
> **Pemerintah Kota Yogyakarta — Dinas Komunikasi Informatika dan Persandian**

---

## LEMBAR KONTROL & METADATA UAT

| Atribut Dokumen | Informasi UAT |
| :--- | :--- |
| **Nama Sistem / Aplikasi** | [Nama Resmi Aplikasi] |
| **Versi Aplikasi** | `v1.0.0` |
| **Nomor Dokumen UAT** | UAT/[KODE-APP]/[BULAN]/[TAHUN] |
| **Tanggal Pelaksanaan** | [DD Bulan YYYY] |
| **Waktu Pengujian** | [09.00 - 15.00 WIB] |
| **Lingkungan Pengujian** | Staging Sandbox (`https://sandbox-[app].jogjakota.go.id`) |
| **Instansi / Unit Kerja Pengguna** | [Nama Organisasi Perangkat Daerah / Bagian Pengguna] |
| **Tim Pendamping Pengembang** | Tim Antigravity Developer & QA Diskominfo Kota Yogyakarta |

---

## 1. 👤 IDENTITAS CALON PENGGUNA / PENGUJI (TESTER PROFILE)

Mohon lengkapi identitas penguji sebelum memulai pengujian fungsional aplikasi:

| Data Penguji | Rincian Isian |
| :--- | :--- |
| **Nama Lengkap Penguji** | ____________________________________________________ |
| **NIP / Identitas Pegawai** | ____________________________________________________ |
| **Jabatan / Bagian** | ____________________________________________________ |
| **OPD / Unit Kerja** | ____________________________________________________ |
| **Peran / Role yang Diuji** | [ ] Superadmin &nbsp;&nbsp;&nbsp; [ ] Admin &nbsp;&nbsp;&nbsp; [ ] Pengawas &nbsp;&nbsp;&nbsp; [ ] Operator |
| **Nomor Kontak / WhatsApp** | ____________________________________________________ |
| **Email Kedinasan (@jogjakota.go.id)** | ____________________________________________________ |

---

## 2. 📖 PETUNJUK PENGISIAN FORMULIR UAT

1. **Persiapan**: Penguji login ke aplikasi menggunakan akun dummy yang disediakan untuk masing-masing peran (atau kredensial SSO JSS pada lingkungan sandbox).
2. **Pelaksanaan Uji**: Jalankan setiap butir skenario pengujian sesuai langkah-langkah yang tertera.
3. **Pemberian Status Hasil**:
   - Beri tanda centang `[✓]` pada kolom **Sesuai (S)** jika fitur bekerja lancar dan memenuhi kebutuhan bisnis Anda.
   - Beri tanda centang `[✓]` pada kolom **Tidak Sesuai (TS)** jika terjadi error, data tidak tampil, form gagal disimpan, atau alur kerja tidak sesuai prosedur.
4. **Catatan Pengamatan**: Tuliskan kendala teknis atau saran perbaikan secara spesifik pada kolom **Catatan Penguji**.

---

## 3. 🧪 MATRIKS PENGUJIAN SKENARIO FITUR OLEH PENGGUNA

### 3.1 Modul Autentikasi & Akses Masuk (SSO Keycloak JSS)
| No | ID Skenario UAT | Fitur / Alur Kerja | Langkah Pengujian Pengguna | Hasil yang Diharapkan | Status Uji | Catatan Penguji |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| 1 | `UAT-AUTH-01` | Halaman Login Terpisah & SSO JSS | Buka alamat aplikasi, pilih role dummy atau masukkan user SSO JSS, klik Masuk | Pengguna berhasil masuk dan dialihkan ke antarmuka dashboard utama | [ ] S<br>[ ] TS | |
| 2 | `UAT-AUTH-02` | Pembatasan Hak Akses (RBAC) | Akses menu sesuai role (misal: Operator mencoba membuka menu konfigurasi sistem) | Menu tersembunyi atau sistem menolak akses dengan informasi izin ditolak | [ ] S<br>[ ] TS | |
| 3 | `UAT-AUTH-03` | Keluar Sistem (Logout) | Klik menu profil di pojok kanan atas, lalu klik tombol Keluar / Logout | Sesi keluar dengan aman dan diarahkan kembali ke halaman login | [ ] S<br>[ ] TS | |

---

### 3.2 Modul Transaksi & Proses Bisnis Utama
| No | ID Skenario UAT | Fitur / Alur Kerja | Langkah Pengujian Pengguna | Hasil yang Diharapkan | Status Uji | Catatan Penguji |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| 4 | `UAT-CORE-01` | Penelusuran & Tampilan Data | Membuka halaman modul bisnis utama, amati penyajian tabel data dan statusnya | Tabel data tersaji rapi, jelas, indikator status mudah dibedakan | [ ] S<br>[ ] TS | |
| 5 | `UAT-CORE-02` | Pencarian & Filter Data | Masukkan kata kunci pada kotak pencarian dan pilih opsi filter dropdown | Data pada tabel tersaring secara cepat dan akurat sesuai filter | [ ] S<br>[ ] TS | |
| 6 | `UAT-CORE-03` | Tambah Data Baru | Klik tombol "Tambah Data", isi seluruh isian wajib pada formulir, klik Simpan | Data baru berhasil tersimpan dan langsung muncul pada urutan atas tabel | [ ] S<br>[ ] TS | |
| 7 | `UAT-CORE-04` | Validasi Form Kosong | Klik "Tambah Data", biarkan isian wajib kosong, klik Simpan | Muncul tanda peringatan merah pada isian yang wajib diisi, form tidak terkirim | [ ] S<br>[ ] TS | |
| 8 | `UAT-CORE-05` | Ubah Data | Pilih salah satu baris data, klik tombol Edit/Ubah, perbarui data, klik Simpan | Perubahan data tersimpan dan tabel memperbarui informasi terbaru | [ ] S<br>[ ] TS | |
| 9 | `UAT-CORE-06` | Hapus Data | Klik tombol Hapus pada data yang dapat dihapus, konfirmasi dialog hapus | Data terhapus dengan aman setelah konfirmasi persetujuan pengguna | [ ] S<br>[ ] TS | |
| 10 | `UAT-CORE-07` | Paginasi Data | Klik nomor halaman (2, 3) atau tombol Berikutnya pada navigasi bawah tabel | Tabel menampilkan baris data halaman berikutnya dengan tepat | [ ] S<br>[ ] TS | |

---

### 3.3 Modul Berkas & Unggah Dokumen (Object Storage MinIO)
| No | ID Skenario UAT | Fitur / Alur Kerja | Langkah Pengujian Pengguna | Hasil yang Diharapkan | Status Uji | Catatan Penguji |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| 11 | `UAT-DOC-01` | Unggah Berkas Dokumen Valid | Pilih file lampiran PDF/JPG yang sah (ukuran < 5 MB), klik unggah | Berkas terunggah sukses, nama file tertera, tombol lihat/unduh aktif | [ ] S<br>[ ] TS | |
| 12 | `UAT-DOC-02` | Unduh & Pratinjau Berkas | Klik tombol "Lihat Berkas" atau tautan unduh dokumen | Dokumen terbuka di tab baru atau terunduh utuh tanpa corrupt | [ ] S<br>[ ] TS | |
| 13 | `UAT-DOC-03` | Penolakan File Melebihi Batas | Coba unggah file dengan ukuran melampaui batas yang diizinkan | Muncul pesan peringatan ukuran berkas melebihi batas maksimal | [ ] S<br>[ ] TS | |

---

### 3.4 Modul Pengaturan Sistem (System Settings)
| No | ID Skenario UAT | Fitur / Alur Kerja | Langkah Pengujian Pengguna | Hasil yang Diharapkan | Status Uji | Catatan Penguji |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| 14 | `UAT-SET-01` | Manajemen Pengguna & Role | Buka menu Manajemen User, periksa daftar user dan penugasan rolenya | Daftar user tampil, admin dapat memetakan role pengguna | [ ] S<br>[ ] TS | |
| 15 | `UAT-SET-02` | Manajemen Menu Geser (Drag-and-Drop) | Buka pengaturan menu sidebar, geser/tarik salah satu posisi item menu | Urutan menu berpindah secara interaktif dan tersimpan otomatis | [ ] S<br>[ ] TS | |
| 16 | `UAT-SET-03` | Pilihan Tema Tampilan | Pilih tema visual pada tombol tema (Light / Dark Themes) | Warna antarmuka berganti mulus tanpa teks yang sulit dibaca | [ ] S<br>[ ] TS | |
| 17 | `UAT-SET-04` | Log Aktivitas Pengguna (Audit) | Login sebagai Superadmin/Pengawas, buka Log Aktivitas Pengguna | Rekam jejak waktu, user, aksi, dan modul tercatat transparan | [ ] S<br>[ ] TS | |

---

## 4. 🌟 EVALUASI KEPUASAN & KUALITAS ANTARMUKA (USABILITY)

Berikan nilai evaluasi umum terhadap kenyamanan dan kinerja sistem aplikasi:

| Parameter Evaluasi | Sangat Baik (5) | Baik (4) | Cukup (3) | Kurang (2) | Sangat Kurang (1) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Kemudahan Navigasi & Menu** | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Kerapian Desain Antarmuka (Apple HIG)** | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Kejelasan Label, Istilah & Notifikasi** | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Kenyamanan Membaca Warna & Kontras Font** | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Kecepatan & Responsivitas Aplikasi** | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 5. 📝 CATATAN MASUKAN & REKOMENDASI CALON PENGGUNA

Silakan tuliskan masukan, perbaikan yang diharapkan, atau kendala khusus yang ditemukan selama pengujian:

```
[Ruang Catatan Calon Pengguna]
1. ...................................................................................................................................
   ...................................................................................................................................

2. ...................................................................................................................................
   ...................................................................................................................................

3. ...................................................................................................................................
   ...................................................................................................................................
```

---

## 6. 📜 BERITA ACARA KESIMPULAN & PENGESAHAN UAT

### 6.1 Kesimpulan Penerimaan Pengguna
Berdasarkan hasil pengujian yang telah dilaksanakan, calon pengguna menyatakan bahwa sistem aplikasi ini:

- [ ] **DITERIMA PENUH**: Seluruh fungsi bekerja dengan baik dan disetujui untuk rilis operasional.
- [ ] **DITERIMA DENGAN CATATAN**: Disetujui dengan catatan perbaikan minor pada butir catatan di atas.
- [ ] **DITOLAK / PERLU PERBAIKAN ULANG**: Perlu dilakukan revisi substansial dan dijadwalkan uji ulang UAT.

---

### 6.2 Lembar Pengesahan Para Pihak

Pengujian ini dilaksanakan secara sadar dan disahkan bersama oleh para pihak pada tanggal [DD Bulan YYYY]:

| Calon Pengguna / Penguji OPD | Tim Teknis Pengembang | Penanggung Jawab Teknis |
| :---: | :---: | :---: |
| <br><br><br>____________________________________<br>**[Nama Penguji Pengguna]**<br>NIP. ................................................... | <br><br><br>____________________________________<br>**[Nama QA / Lead Developer]**<br>Tim Pengembang Aplikasi | <br><br><br>____________________________________<br>**[Nama PPTK / Pejabat Diskominfo]**<br>NIP. ................................................... |
