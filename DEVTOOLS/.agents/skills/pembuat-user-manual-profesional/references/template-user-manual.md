# 📖 PANDUAN PENGGUNAAN APLIKASI [NAMA APLIKASI]

---

## LEMBAR KONTROL DOKUMEN

| Metadata Dokumen | Detail |
| :--- | :--- |
| **Nama Aplikasi** | [Nama Resmi Aplikasi] |
| **Versi Aplikasi** | `v1.0.0` |
| **Versi Dokumen** | `1.0` |
| **Tanggal Terbit** | [DD Bulan YYYY] |
| **Instansi / Unit Kerja** | Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta |
| **Disusun Oleh** | Tim Pengembang / Technical Writer |
| **Disetujui Oleh** | Kepala Bidang [...] |
| **Lokasi File Output** | `docs/USER_MANUAL.md` / `docs/Panduan_Pengguna_[NamaAplikasi].docx` |
| **Klasifikasi** | PUBLIK / INTERNAL |

### Riwayat Revisi
| Versi | Tanggal | Perubahan | Penyusun |
| :---: | :--- | :--- | :--- |
| 1.0 | [DD/MM/YYYY] | Rilis perdana dokumen panduan pengguna | [Nama] |

---

## DAFTAR ISI

1. [Pendahuluan](#bab-1-pendahuluan)
2. [Persyaratan Sistem](#bab-2-persyaratan-sistem)
3. [Memulai Aplikasi & Login](#bab-3-memulai-aplikasi--login)
4. [Navigasi & Antarmuka Utama](#bab-4-navigasi--antarmuka-utama)
5. [Panduan Penggunaan Modul — [Nama Modul 1]](#bab-5-panduan-penggunaan-modul--nama-modul)
6. [Penanganan Pesan Kesalahan (Error Handling)](#bab-n-penanganan-pesan-kesalahan)
7. [Pertanyaan yang Sering Diajukan (FAQ)](#bab-n1-pertanyaan-yang-sering-diajukan-faq)
8. [Lampiran: Glosarium & Singkatan](#lampiran-glosarium--singkatan)

---

## DAFTAR GAMBAR

| No. Gambar | Judul | Bab |
| :--- | :--- | :---: |
| Gambar 3.1 | Tampilan Halaman Login | Bab 3 |
| Gambar 3.2 | Tampilan Dashboard Setelah Login Berhasil | Bab 3 |
| Gambar 4.1 | Komponen Navigasi Sidebar | Bab 4 |

---

## BAB 1: PENDAHULUAN

### 1.1 Tentang Aplikasi
[Nama Aplikasi] adalah sistem informasi berbasis web yang dikembangkan oleh Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta untuk [tujuan utama aplikasi / masalah yang dipecahkan].

### 1.2 Tujuan Dokumen
Dokumen Panduan Penggunaan ini disusun dengan tujuan:
- Membantu pengguna memahami fitur dan fungsi yang tersedia di [Nama Aplikasi].
- Memberikan panduan langkah demi langkah untuk menyelesaikan tugas-tugas operasional.
- Menjadi referensi cepat bagi pengguna ketika menghadapi situasi yang tidak familiar.

### 1.3 Target Pembaca
Panduan ini ditujukan kepada pengguna dengan peran berikut:
| Peran (Role) | Deskripsi Singkat | Bab yang Relevan |
| :--- | :--- | :--- |
| **Superadmin** | Akses penuh seluruh modul & konfigurasi sistem | Semua Bab |
| **Admin** | Manajemen pengguna & pengaturan aplikasi | Bab 3, 4, 5, 6 |
| **Operator** | Operasional transaksi harian | Bab 3, 4, 5 |
| **Pengawas** | Pemantauan & laporan (read-only) | Bab 3, 4 |

### 1.4 Cara Menggunakan Panduan Ini
- Baca **Bab 2 – Persyaratan Sistem** terlebih dahulu untuk memastikan perangkat Anda kompatibel.
- Ikuti prosedur **langkah demi langkah** secara berurutan.
- Perhatikan kotak **⚠️ Perhatian** dan **❌ Larangan** sebelum melakukan tindakan kritis.
- Gambar pada panduan ini menampilkan tampilan nyata aplikasi versi `v[X.X.X]`.

---

## BAB 2: PERSYARATAN SISTEM

### 2.1 Perangkat Keras (Hardware)
| Komponen | Spesifikasi Minimum |
| :--- | :--- |
| Prosesor | Dual-core 1.6 GHz |
| RAM | 4 GB |
| Resolusi Layar | 1280 × 768 piksel (disarankan 1920×1080) |
| Koneksi Internet | Stabil minimal 5 Mbps |

### 2.2 Perangkat Lunak (Browser yang Didukung)
| Browser | Versi Minimum | Status Dukungan |
| :--- | :---: | :---: |
| Google Chrome | v100+ | ✅ Direkomendasikan |
| Mozilla Firefox | v100+ | ✅ Didukung |
| Microsoft Edge | v100+ | ✅ Didukung |
| Safari | v15+ | ⚠️ Terbatas |
| Internet Explorer | Semua | ❌ Tidak Didukung |

> ℹ️ **Informasi:** Untuk pengalaman terbaik, gunakan **Google Chrome versi terbaru** dengan mode tampilan **100%** (zoom tidak diubah).

---

## BAB 3: MEMULAI APLIKASI & LOGIN

### 3.1 Mengakses Aplikasi
1. Buka browser yang direkomendasikan di perangkat Anda.
2. Ketikkan alamat URL aplikasi pada kolom alamat browser:
   ```
   https://[nama-aplikasi].jogjakota.go.id
   ```
3. Tekan **Enter** untuk membuka halaman aplikasi.

**Hasil yang Diharapkan:** Halaman Login aplikasi tampil seperti gambar berikut.

![Halaman Login Aplikasi](./screenshots/03-01-halaman-login.png)
*Gambar 3.1: Tampilan halaman Login [Nama Aplikasi]*

### 3.2 Proses Login via SSO Keycloak
[Nama Aplikasi] menggunakan sistem masuk terpadu **(Single Sign-On / SSO)** Pemerintah Kota Yogyakarta. Anda **tidak perlu** mendaftar akun baru secara manual.

1. Pada halaman Login, klik tombol **"Masuk dengan Akun JSS Yogyakarta"**.

   ![Tombol Login SSO](./screenshots/03-02-tombol-login-sso.png)
   *Gambar 3.2: Tombol Login menggunakan akun JSS Kota Yogyakarta*

2. Anda akan diarahkan ke halaman Login SSO Keycloak (`sso.jogjakota.go.id`). Masukkan:
   - **Username**: Akun JSS Anda (NIP / nomor registrasi)
   - **Password**: Kata sandi akun JSS Anda

3. Klik tombol **"Masuk"** / **"Sign In"**.

4. Jika login berhasil, Anda akan diarahkan kembali ke [Nama Aplikasi] dan masuk ke halaman Dashboard.

   ![Dashboard Setelah Login](./screenshots/03-03-dashboard-setelah-login.png)
   *Gambar 3.3: Tampilan halaman Dashboard setelah login berhasil*

> ⚠️ **Perhatian:** Jika muncul pesan *"Akun Anda tidak memiliki akses ke aplikasi ini"*, hubungi Administrator untuk meminta pemberian hak akses.

### 3.3 Keluar dari Aplikasi (Logout)
Untuk menjaga keamanan data, selalu lakukan logout setelah selesai menggunakan aplikasi.

1. Klik ikon profil / nama pengguna di pojok kanan atas layar.
2. Dari menu yang muncul, klik **"Keluar"** atau **"Logout"**.
3. Anda akan diarahkan kembali ke halaman Login.

> ⚠️ **Perhatian:** Sesi login akan **otomatis berakhir setelah 10 menit tidak aktif** demi alasan keamanan. Simpan pekerjaan Anda sebelum meninggalkan perangkat.

---

## BAB 4: NAVIGASI & ANTARMUKA UTAMA

### 4.1 Komponen Antarmuka
Setelah login, Anda akan melihat tampilan utama aplikasi yang terdiri dari beberapa area:

![Anatomi Antarmuka](./screenshots/04-01-anatomi-antarmuka.png)
*Gambar 4.1: Komponen utama antarmuka [Nama Aplikasi]*

| No. | Nama Komponen | Fungsi |
| :---: | :--- | :--- |
| ① | **Header / Navbar** | Menampilkan logo aplikasi, notifikasi, dan profil pengguna |
| ② | **Sidebar / Menu Navigasi** | Daftar menu dan sub-menu berdasarkan hak akses role |
| ③ | **Area Konten Utama** | Area kerja utama yang berubah sesuai menu yang dipilih |
| ④ | **Breadcrumb** | Menunjukkan posisi halaman Anda saat ini |
| ⑤ | **Footer** | Informasi versi aplikasi dan hak cipta |

### 4.2 Menjelajahi Menu Navigasi
1. Menu navigasi tersedia di **sisi kiri** layar (Sidebar).
2. Klik tanda **▶** atau **nama menu grup** untuk memperluas sub-menu.
3. Klik nama menu untuk membuka halaman terkait.
4. Menu yang sedang aktif akan ditandai dengan **warna berbeda** atau **garis vertikal** di sisi kiri.

> ✅ **Tips:** Sidebar dapat diciutkan dengan mengklik ikon **☰** (hamburger) di pojok kiri atas untuk memperluas area kerja.

---

## BAB 5: PANDUAN PENGGUNAAN MODUL — [NAMA MODUL]

### 5.1 Gambaran Umum Modul
[Nama Modul] digunakan untuk [tujuan & fungsi utama modul]. Modul ini dapat diakses oleh pengguna dengan role: **[Daftar Role]**.

### 5.2 Melihat Daftar [Entitas Data]

1. Pada Sidebar, klik menu **[Nama Menu]** → **[Nama Sub-Menu]**.
2. Halaman daftar [Entitas Data] akan tampil.

   ![Halaman Daftar Data](./screenshots/05-01-daftar-data.png)
   *Gambar 5.1: Tampilan halaman daftar [Entitas Data]*

3. Gunakan **kolom Pencarian** di bagian atas tabel untuk menemukan data tertentu.
4. Klik header kolom untuk mengurutkan data (*ascending/descending*).
5. Atur jumlah data per halaman melalui menu **"Tampilkan [N] data"**.

### 5.3 Menambah [Entitas Data] Baru

1. Klik tombol **"+ Tambah [Entitas Data]"** di pojok kanan atas tabel.

   ![Tombol Tambah Data](./screenshots/05-02-tombol-tambah-data.png)
   *Gambar 5.2: Tombol untuk menambah data baru*

2. Form isian akan tampil. Isi seluruh field yang ditandai tanda bintang (**\***) — field ini wajib diisi.

   ![Form Tambah Data](./screenshots/05-03-form-tambah-data.png)
   *Gambar 5.3: Form isian data baru*

3. Periksa kembali data yang diisikan.
4. Klik tombol **"Simpan"** untuk menyimpan data.

**Hasil yang Diharapkan:** Muncul notifikasi **"Data berhasil disimpan"** di pojok kanan atas layar, dan data baru tampil di daftar.

> ❌ **Larangan:** Jangan menutup atau me-refresh halaman saat proses penyimpanan berlangsung (saat tombol Simpan masih menampilkan indikator loading).

### 5.4 Mengubah (Edit) [Entitas Data]

1. Temukan data yang ingin diubah pada tabel daftar.
2. Klik ikon **✏️ Edit** atau tombol **"Ubah"** pada baris data tersebut.
3. Form edit akan tampil dengan data yang sudah terisi sebelumnya.
4. Ubah field yang diperlukan.
5. Klik tombol **"Simpan Perubahan"**.

**Hasil yang Diharapkan:** Notifikasi **"Data berhasil diperbarui"** tampil dan data pada tabel diperbarui.

### 5.5 Menghapus [Entitas Data]

1. Temukan data yang ingin dihapus pada tabel daftar.
2. Klik ikon **🗑️ Hapus** atau tombol **"Hapus"** pada baris data tersebut.
3. Kotak dialog konfirmasi akan tampil.

   ![Dialog Konfirmasi Hapus](./screenshots/05-04-dialog-konfirmasi-hapus.png)
   *Gambar 5.4: Dialog konfirmasi penghapusan data*

4. Klik **"Ya, Hapus"** untuk mengkonfirmasi penghapusan, atau **"Batal"** untuk membatalkan.

> ⚠️ **Perhatian:** Data yang telah dihapus **tidak dapat dipulihkan kembali**. Pastikan Anda memilih data yang benar sebelum mengkonfirmasi penghapusan.

---

## BAB N: PENANGANAN PESAN KESALAHAN

### N.1 Daftar Pesan Kesalahan Umum

| Pesan Kesalahan | Penyebab | Solusi |
| :--- | :--- | :--- |
| *"Sesi Anda telah berakhir. Silakan login kembali."* | Sesi login otomatis berakhir setelah 10 menit tidak aktif. | Klik tombol **"Login Kembali"** dan masuk dengan akun SSO Anda. |
| *"Akun Anda tidak memiliki akses ke fitur ini."* | Role akun Anda tidak memiliki hak akses ke fitur yang dimaksud. | Hubungi Administrator untuk meminta akses yang sesuai. |
| *"Gagal memuat data. Periksa koneksi internet Anda."* | Koneksi internet terputus atau server sedang tidak dapat dijangkau. | Periksa koneksi internet, refresh halaman, atau tunggu beberapa saat. |
| *"Format file tidak didukung. Gunakan format: [list format]."* | File yang diunggah tidak sesuai format yang diizinkan. | Konversi file ke format yang sesuai sebelum mengunggah. |
| *"Ukuran file melebihi batas maksimum [X] MB."* | Ukuran file unggahan terlalu besar. | Kompres atau perkecil ukuran file sebelum mengunggah. |
| *"Data tidak dapat dihapus karena masih digunakan oleh transaksi lain."* | Data masih memiliki relasi dengan data lain di sistem. | Hapus terlebih dahulu data yang berelasi, kemudian coba hapus data ini kembali. |

### N.2 Langkah Umum Pemecahan Masalah
Jika mengalami masalah yang tidak tercantum di tabel di atas:
1. **Refresh halaman** dengan menekan **F5** atau **Ctrl+R**.
2. Hapus *cache* browser: **Ctrl+Shift+Delete** → pilih "Cached images and files" → klik "Clear data".
3. Coba akses menggunakan **browser berbeda**.
4. Jika masalah masih berlanjut, catat:
   - Waktu kejadian (tanggal & jam)
   - Fitur / menu yang sedang digunakan
   - Tangkapan layar (screenshot) pesan error
5. Hubungi **Helpdesk** dengan informasi di atas.

---

## BAB N+1: PERTANYAAN YANG SERING DIAJUKAN (FAQ)

**Q: Bagaimana jika saya lupa password akun JSS?**
> A: Password akun JSS dikelola secara terpusat. Kunjungi portal JSS di `https://jss.jogjakota.go.id` untuk melakukan reset password, atau hubungi Helpdesk Diskominfo.

**Q: Apakah aplikasi ini dapat diakses melalui smartphone?**
> A: Aplikasi ini dirancang untuk tampilan desktop/laptop. Akses melalui smartphone memungkinkan tetapi tampilan mungkin tidak optimal. Gunakan mode *Desktop View* di browser smartphone untuk pengalaman terbaik.

**Q: Apa yang harus dilakukan jika data yang sudah disimpan tidak muncul di daftar?**
> A: Klik tombol **"Refresh"** atau **"Muat Ulang"** pada tabel, atau tekan **F5** pada keyboard. Jika data masih tidak muncul, hubungi Administrator sistem.

**Q: Bagaimana cara mengekspor data ke Excel/PDF?**
> A: Klik tombol **"Ekspor"** atau ikon unduh yang tersedia di pojok kanan atas tabel data. Pilih format yang diinginkan (Excel / PDF / CSV).

---

## LAMPIRAN: GLOSARIUM & SINGKATAN

| Istilah / Singkatan | Kepanjangan / Penjelasan |
| :--- | :--- |
| **SSO** | Single Sign-On — Sistem masuk terpadu yang memungkinkan satu akun untuk mengakses berbagai aplikasi |
| **JSS** | Jogja Smart Service — Portal layanan terpadu Pemerintah Kota Yogyakarta |
| **RBAC** | Role-Based Access Control — Sistem pengendalian akses berdasarkan peran pengguna |
| **Dashboard** | Halaman utama yang menampilkan ringkasan informasi dan navigasi aplikasi |
| **Cache** | Data sementara yang disimpan browser untuk mempercepat pemuatan halaman |
| **Breadcrumb** | Navigasi beruntun yang menunjukkan posisi halaman pengguna saat ini |
| **Upload / Unggah** | Proses mengirim file dari perangkat lokal ke server aplikasi |
| **Download / Unduh** | Proses mengambil/mengunduh file dari server aplikasi ke perangkat lokal |

---

*Dokumen ini adalah milik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta. Dilarang memperbanyak atau mendistribusikan tanpa izin tertulis.*

*© [Tahun] Diskominfo Kota Yogyakarta — Versi Dokumen [X.X]*
