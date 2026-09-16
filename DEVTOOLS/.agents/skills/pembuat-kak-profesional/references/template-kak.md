# 📑 TEMPLATE KONTEN KERANGKA ACUAN KERJA (KAK)

---

# KERANGKA ACUAN KERJA (KAK) / TERMS OF REFERENCE (TOR)
## PENGADAAN & PENGEMBANGAN SISTEM INFORMASI [NAMA APLIKASI]

---

## 1. LATAR BELAKANG

### 1.1 Gambaran Umum & Kondisi Saat Ini (As-Is)
Pemerintah Kota Yogyakarta melalui Dinas Komunikasi Informatika dan Persandian berkomitmen meningkatkan kualitas pelayanan publik dan efisiensi tata kelola pemerintahan berbasis digital. Saat ini, proses [uraian proses bisnis berjalan] masih menghadapi sejumlah kendala seperti [kendala 1, kendala 2, pencatatan manual/tersebar]. 

### 1.2 Keterkaitan dengan SPBE & Renstra Pemkot Yogyakarta
Kegiatan pengembangan sistem informasi ini merupakan implementasi nyata dari Roadmap Sistem Pemerintahan Berbasis Elektronik (SPBE) Pemerintah Kota Yogyakarta dan selaras dengan Rencana Strategis (Renstra) Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta untuk mewujudkan arsitektur data terintegrasi, transparan, dan akuntabel.

### 1.3 Permasalahan dan Urgensi Pengembangan
Kebutuhan akan sistem yang terotomasi, memiliki ketersediaan tinggi (*high availability*), performa tinggi (*low latency*), serta keamanan data yang tangguh sangat mendesak guna mendukung pengambilan keputusan berbasis data (*data-driven decision making*) di lingkungan Pemerintah Kota Yogyakarta.

---

## 2. MAKSUD DAN TUJUAN

### 2.1 Maksud
Maksud dari pelaksanaan pekerjaan ini adalah tersedianya aplikasi perangkat lunak [Nama Aplikasi] yang modern, aman, handal, dan terintegrasi untuk mengelola [fungsi utama sistem] di lingkungan Pemerintah Kota Yogyakarta.

### 2.2 Tujuan
Tujuan yang ingin dicapai melalui pekerjaan ini antara lain:
1. Membangun sistem informasi berbasis web dengan backend Golang (Clean Architecture) dan frontend modern yang responsif.
2. Mengintegrasikan autentikasi terpusat berbasis SSO JSS Keycloak OIDC (`sso.jogjakota.go.id`) dengan skema 4 Role RBAC (*Superadmin, Admin, Operator, Pengawas*).
3. Mengimplementasikan penyimpanan dokumen terdesentralisasi menggunakan MinIO Object Storage dengan Presigned URL dan validasi Magic Bytes.
4. Menyediakan antarmuka dokumentasi API interaktif Swagger / OpenAPI untuk interoperabilitas lintas instansi.
5. Menjamin keamanan sistem informasi bebas dari celah kerentanan OWASP Top 10 melalui audit SAST, SCA, dan DAST Pentesting.

---

## 3. SASARAN DAN TARGET KINERJA

Sasaran dari pekerjaan ini adalah terwujudnya sistem informasi [Nama Aplikasi] yang siap operasional (*production-ready*) dengan target kinerja:
- Waktu respon API (*latency*) P95 < 200 ms.
- Ketersediaan sistem (*availability*) minimal 99,5%.
- Target code coverage unit & integration testing minimal 85% dengan cakupan *Positive Testing* dan *Negative Testing* menyeluruh.
- Tingkat kerentanan keamanan 0 temuan berstatus *Medium/High/Critical*.

---

## 4. LANDASAN HUKUM

Dasar hukum pelaksanaan pekerjaan ini mengacu pada:
1. Undang-Undang Nomor 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik sebagaimana telah diubah terakhir dengan Undang-Undang Nomor 1 Tahun 2024.
2. Peraturan Presiden Nomor 95 Tahun 2018 tentang Sistem Pemerintahan Berbasis Elektronik (SPBE).
3. Peraturan Presiden Nomor 16 Tahun 2018 tentang Pengadaan Barang/Jasa Pemerintah beserta perubahannya Peraturan Presiden Nomor 12 Tahun 2021.
4. Peraturan Menteri Komunikasi dan Informatika Nomor 8 Tahun 2019 tentang Penyelenggaraan Pelayanan Perizinan Berusaha Terintegrasi Secara Elektronik Sektor Komunikasi dan Informatika.
5. Peraturan Daerah / Peraturan Wali Kota Yogyakarta terkait Tata Kelola SPBE dan Keamanan Informasi.

---

## 5. SUMBER PENDANAAN DAN ESTIMASI ANGGARAN

Pekerjaan ini dibiayai melalui:
- **Sumber Dana**: Anggaran Pendapatan dan Belanja Daerah (APBD) Pemerintah Kota Yogyakarta Tahun Anggaran [TA].
- **DPA SKPD**: Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta.
- **Pagu Anggaran / HPS**: Rp [Nominal Anggaran] (termasuk pajak yang berlaku sesuai ketentuan perundang-undangan).

---

## 6. RUANG LINGKUP PEKERJAAN

### 6.1 Ruang Lingkup Fungsional & Modul Sistem (In-Scope)
Pengembangan sistem mencakup modul-modul berikut (mengacu pada Blueprint):
1. **Modul Autentikasi Terpusat SSO Keycloak JSS**:
   - Integrasi OIDC Keycloak JSS (`sso.jogjakota.go.id`).
   - Penegakan 4 Role RBAC (*Superadmin, Pengawas/Auditor read-only, Admin, Operator*).
2. **Modul Manajemen User & Profil Pengguna**:
   - Sinkronisasi identitas JSS, mapping hak akses, dan manajemen status akun.
3. **Modul Pengaturan Aplikasi & Konfigurasi Sistem**:
   - Konfigurasi parameter dinamis, integrasi MinIO, Keycloak client settings, rate limiting.
4. **Modul Inti Bisnis [PRD-01: Nama Fitur 1]**:
   - [Deskripsi fitur dan alur transaksi bisnis utama].
5. **Modul Inti Bisnis [PRD-02: Nama Fitur 2]**:
   - [Deskripsi fitur, pencatatan data, dan validasi bisnis].
6. **Modul Object Storage MinIO**:
   - Upload dokumen privat via Presigned URL, pengecekan Magic Bytes, UUID v4 hashing.
7. **Modul Audit Log & Monitoring**:
   - Pencatatan jejak audit aktivitas transaksi (*audit trail*) untuk keamanan dan pemantauan.
8. **Modul Swagger / OpenAPI Documentation**:
   - Endpoint Swagger UI `/swagger/index.html` dan sinkronisasi berkas spesifikasi di `docs/`.

### 6.2 Batasan Pekerjaan (Out-of-Scope)
- Pengadaan infrastruktur perangkat keras (*server hardware*) dan lisensi pihak ketiga berbayar di luar spesifikasi.
- Migrasi data historis non-digital yang tidak memiliki format terstruktur.

---

## 7. SPESIFIKASI TEKNIS & ARSITEKTUR SISTEM

| Komponen | Spesifikasi Standar |
| :--- | :--- |
| **Backend Language** | Go (Golang) versi 1.22+ (Clean Architecture) |
| **Frontend Framework** | React / Vue 3 dengan Vite + Tailwind CSS / Metronic |
| **Database** | PostgreSQL 16+ dengan Connection Pool (`pgxpool`) |
| **Cache & Queue** | Redis 7+ *(opsional jika dibutuhkan beban tinggi/rate limiting)* |
| **Object Storage** | MinIO Object Storage (Presigned URL) |
| **Otentikasi** | Keycloak JSS OpenID Connect (OIDC) |
| **Kontainerisasi** | Docker & Docker Compose |
| **Dokumentasi API** | OpenAPI 3.0 / Swagger UI |

---

## 8. KEBUTUHAN TENAGA AHLI & KUALIFIKASI

| No | Posisi / Tenaga Ahli | Jumlah | Kualifikasi Minimal & Sertifikasi |
| :-: | :--- | :-: | :--- |
| 1 | **Project Manager** | 1 Orang | S1 Teknik Informatika/Sistem Informasi, pengalaman min. 5 tahun, sertifikasi PMP / Scrum Master. |
| 2 | **System Analyst / Solution Architect** | 1 Orang | S1 Teknik Informatika/Ilmu Komputer, pengalaman min. 4 tahun di bidang arsitektur sistem perangkat lunak. |
| 3 | **Senior Backend Developer (Golang)** | 1 Orang | S1/D4 Komputer, pengalaman min. 3 tahun pengembangan REST API Golang & Clean Architecture. |
| 4 | **Frontend Developer** | 1 Orang | S1/D4 Komputer, pengalaman min. 3 tahun React/Vue, Tailwind CSS, State Management. |
| 5 | **Quality Assurance (QA) Engineer** | 1 Orang | S1/D4 Komputer, pengalaman min. 2 tahun di bidang automated unit/integration testing & negative testing. |
| 6 | **Cybersecurity Specialist / Pentester** | 1 Orang | S1/D4 Komputer, pengalaman min. 3 tahun, sertifikasi CEH / OSCP / CompTIA Security+, ahli OWASP & WSTG. |
| 7 | **Technical Writer** | 1 Orang | S1 Segala Jurusan, pengalaman min. 2 tahun dalam penyusunan dokumentasi teknis & User Manual berstandar ISO 26514. |

---

## 9. JANGKA WAKTU & JADWAL PELAKSANAAN PEKERJAAN

Pekerjaan ini dilaksanakan selama **[Durasi, mis. 60 / 90] hari kalender** terhitung sejak penandatanganan Surat Perintah Mulai Kerja (SPMK).

| No | Tahapan Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
| :-: | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | Kick-off Meeting & Requirement Gathering | █ | | | | | | | |
| 2 | Penyusunan Blueprint & Desain Arsitektur | | █ | | | | | | |
| 3 | Pengembangan Backend API & Database | | | █ | █ | | | | |
| 4 | Pengembangan Frontend UI & Integrasi SSO | | | | █ | █ | | | |
| 5 | Testing QA (Unit, Integration, Negative Test) | | | | | █ | █ | | |
| 6 | Audit Keamanan, SAST/DAST, Pentest | | | | | | █ | █ | |
| 7 | Penyusunan Dokumentasi Teknis & User Manual | | | | | | | █ | █ |
| 8 | UAT, Pelatihan/Alih Pengetahuan, BAST | | | | | | | | █ |

---

## 10. METODOLOGI & QUALITY ASSURANCE

### 10.1 Metodologi Pengembangan
Menggunakan pendekatan Agile / Scrum yang dipadukan dengan standar Clean Architecture untuk menjamin keterpisahan tanggung jawab (*separation of concerns*).

### 10.2 Standar Pengujian QA & Negative Testing Wajib
Pengujian otomatis dan manual wajib mencakup:
1. **Positive / Happy Path Testing**: Pengujian input valid sesuai alur bisnis.
2. **Negative & Boundary Testing**:
   - Validasi ketidakcocokan tipe data (*type mismatch*, contoh: field integer diinput teks/string).
   - Validasi nilai batas (*boundary value*, batas karakter, nilai negatif, integer limit).
   - Validasi payload tidak lengkap (*missing mandatory fields*) atau malformed JSON.
   - Uji injeksi formulir (SQL injection patterns, XSS script tags, directory traversal).
   - Uji penolakan akses RBAC dan token tidak valid.

### 10.3 Standar Pengujian Keamanan
Audit keamanan mengacu pada OWASP Top 10 2021, OWASP API Security Top 10 2023, dan WSTG v4.2 dengan target 0 kerentanan *Medium/High/Critical*.

---

## 11. KELUARAN / DELIVERABLES PEKERJAAN

Penyedia wajib menyerahkan deliverables lengkap yang tersimpan pada repositori dan folder `docs/`:
1. **Source Code Lengkap**: Backend Go, Frontend React/Vue, Docker configuration, dan migration scripts.
2. **`docs/Dokumen_Blueprint_Resmi.docx` & `Blueprint.md`**: Dokumen spesifikasi arsitektur (BRD + PRD + SRS).
3. **`docs/Dokumen_KAK_Resmi.docx` & `docs/KAK.md`**: Dokumen Kerangka Acuan Kerja resmi.
4. **`docs/Laporan_Pengujian_QA.docx` & `docs/TEST_REPORT.md`**: Laporan hasil pengujian QA fungsional dan *Negative Testing*.
5. **`docs/Dokumen_Laporan_Pentest_Resmi.docx` & `docs/SECURITY_REPORT.md`**: Laporan hasil audit keamanan dan pengujian penetrasi OWASP.
6. **`docs/Dokumen_Spesifikasi_API.docx`, `docs/swagger.json`, `docs/swagger.yaml`**: Panduan integrasi API untuk developer eksternal.
7. **`docs/Panduan_Pengguna_[NamaApp].docx` & `docs/USER_MANUAL.md`**: Buku panduan operasional pengguna disertai screenshot visual.

---

## 12. PEMELIHARAAN, GARANSI, SLA, DAN ALIH PENGETAHUAN

1. **Masa Garansi & Pemeliharaan**: Minimal 3 (tiga) bulan sejak Berita Acara Serah Terima (BAST) ditandatangani, mencakup perbaikan *bug/defect* dan *security patching*.
2. **Service Level Agreement (SLA)**: Penanganan insiden kritis maksimal 4 jam respons dan 24 jam resolusi.
3. **Alih Pengetahuan (Knowledge Transfer)**: Pelatihan teknis bagi Tim Teknis Diskominfo (administrator sistem) dan pelatihan operasional bagi pengguna akhir (*end-user*).

---

## 13. LAPORAN & SERAH TERIMA PEKERJAAN

Laporan yang wajib disampaikan:
1. **Laporan Pendahuluan**: Hasil analisis kebutuhan dan rencana kerja.
2. **Laporan Antara**: Hasil rancang bangun arsitektur dan progres pengkodean sistem (50%).
3. **Laporan Akhir**: Hasil keseluruhan pekerjaan, laporan pengujian, dan seluruh dokumen deliverable.
4. **Berita Acara Serah Terima (BAST)** setelah verifikasi pengujian UAT dinyatakan lulus 100%.
