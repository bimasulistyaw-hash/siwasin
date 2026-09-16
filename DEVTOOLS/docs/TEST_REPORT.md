# 📊 LAPORAN HASIL PENGUJIAN FUNGSIONAL & NEGATIVE TESTING (TEST REPORT)

---

## LEMBAR KONTROL DOKUMEN

| Metadata Dokumen | Detail |
| :--- | :--- |
| **Nama Aplikasi** | [Nama Resmi Aplikasi] |
| **Versi Aplikasi** | `v1.0.0` |
| **Versi Dokumen** | `1.0` |
| **Tanggal Pengujian** | [DD Bulan YYYY, HH:MM WIB] |
| **Penguji** | Antigravity QA & Testing Agent |
| **Lingkungan Pengujian** | Staging / Testing Sandbox (`https://[url-staging]`) |
| **Metode Pengujian** | Functional, Positive, & Negative Testing (Black-box & API Automation) |
| **Standar Acuan** | ISO/IEC/IEEE 29119-3:2021, IEEE 829, ISTQB, Gherkin (Given/When/Then) |
| **Sumber Test Case** | `Blueprint.md` (Acceptance Criteria `SRS-F-xx`) & Rule QA Negative Testing |
| **Lokasi File Output** | `docs/TEST_REPORT.md` dan `docs/Laporan_Pengujian_QA.docx` |

### Riwayat Revisi
| Versi | Tanggal | Perubahan | Penguji |
| :---: | :--- | :--- | :--- |
| 1.0 | [DD/MM/YYYY] | Pengujian fungsional & negative testing menyeluruh | [Nama] |

---

## 1. 📊 RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)

### 1.1 Distribusi Hasil Pengujian
| Kategori Pengujian | Total Kasus | ✅ Pass | ❌ Fail | ⚠️ Partial | % Lulus |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Autentikasi & Login SSO Keycloak (Positive Path) | 0 | 0 | 0 | 0 | — |
| Matriks Hak Akses RBAC 4 Role | 0 | 0 | 0 | 0 | — |
| Fungsionalitas Modul Inti (Positive Path) | 0 | 0 | 0 | 0 | — |
| Negative Testing: Type Mismatch (Teks di Integer dll) | 0 | 0 | 0 | 0 | — |
| Negative Testing: Boundary & Length Violations | 0 | 0 | 0 | 0 | — |
| Negative Testing: Malformed Payload & Missing Fields | 0 | 0 | 0 | 0 | — |
| Negative Testing: Form Injection Sanitization (SQLi/XSS) | 0 | 0 | 0 | 0 | — |
| Negative Testing: RBAC Unauthorized & Forbidden Gates | 0 | 0 | 0 | 0 | — |
| Object Storage MinIO & Negative Magic Bytes Check | 0 | 0 | 0 | 0 | — |
| **TOTAL** | **0** | **0** | **0** | **0** | **—** |

### 1.2 Status Kelayakan Rilis
> **Status: [DRAFT SKENARIO PENGUJIAN / SELESAI UJI: ✅ LAYAK RILIS / ❌ TIDAK LAYAK]**
>
> [Catatan evaluasi kelayakan sistem terhadap skenario pengujian positif dan ketahanan terhadap skenario negatif.]

---

## 2. 🗂️ MATRIKS PENGUJIAN RBAC (4 ROLE × HAK AKSES)

| Fitur / Aksi | Superadmin | Admin | Operator | Pengawas | Catatan Verifikasi |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Login SSO Keycloak | ✅ | ✅ | ✅ | ✅ | Semua role wajib bisa login |
| Akses Dashboard Utama | ✅ | ✅ | ✅ | ✅ | Read-only untuk Pengawas |
| Manajemen User & Mapping Role | ✅ | ✅ | ❌ (403) | ❌ (read) | Operator dilarang kelola user |
| Pengaturan Aplikasi & Konfigurasi | ✅ | ✅ | ❌ (403) | ❌ (read) | |
| Tambah / Ubah Data Transaksi | ✅ | ✅ | ✅ | ❌ (403) | Pengawas ditolak mutasi data |
| Hapus Data Transaksi | ✅ | ✅ | ❌ (403) | ❌ (403) | Dibatasi peran berwenang |
| Audit Trail & Activity Log | ✅ | ❌ | ❌ | ✅ | Superadmin & Pengawas |

---

## 3. 🔍 DETAIL SKENARIO PENGUJIAN & HASIL AKTUAL (TEST CASES)

> [!IMPORTANT]
> **Aturan Disiplin QA**: Seluruh skenario pengujian di bawah ini (baik **Positive Testing / Happy Path** maupun **Negative Testing**) **WAJIB dirancang dan disusun terlebih dahulu sebelum eksekusi testing dimulai**. Setelah pengujian dijalankan, bagian **Actual Result**, **Status**, dan **Bukti Screenshot** diisi sesuai hasil uji nyata.

### 3.1 Autentikasi SSO & Otorisasi

#### `TC-AUTH-001` — Login dengan akun SSO JSS valid `[SRS-F-01]`
- **Kategori**: Positive Testing (Happy Path)
- **Modul**: Modul Autentikasi SSO Keycloak JSS
- **Prakondisi (Given)**: Pengguna belum login dan membuka halaman login aplikasi (`/login`).
- **Langkah & Payload Uji (When)**: Memasukkan kredensial JSS valid untuk user `Superadmin`.
- **Ekspektasi Hasil (Expected / Then)**: Login berhasil, JWT tersimpan, dialihkan ke dashboard utama (HTTP 200).
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Tampilan Diuji**:
  ![Login Berhasil](./screenshots/qa-auth-001-dashboard-pass.png)
  *Gambar QA-1: Tampilan antarmuka dashboard setelah login SSO berhasil*

#### `TC-AUTH-002` — Request API tanpa Authorization Header / Token Expired
- **Kategori**: Negative Testing (Unauthorized Access)
- **Modul**: Middleware Auth JWT
- **Prakondisi (Given)**: Pengguna tidak menyertakan Authorization Bearer Token.
- **Langkah & Payload Uji (When)**: Mengirimkan HTTP `GET /api/v1/users` tanpa header `Authorization`.
- **Ekspektasi Hasil (Expected / Then)**: Akses ditolak dengan HTTP `401 Unauthorized` (`{"code": "ERR_UNAUTHORIZED"}`).
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Penolakan Akses Tanpa Token](./screenshots/qa-auth-002-unauthorized.png)
  *Gambar QA-2: Respon error 401 Unauthorized*

---

### 3.2 Negative Testing — Type Mismatch & Constraint Validation

#### `TC-NEG-TYPE-001` — Input Teks/String pada Field Numerik/Integer
- **Kategori**: Negative Testing (Type Mismatch)
- **Modul**: DTO Validation & Controller
- **Prakondisi (Given)**: Endpoint menerima parameter query integer `page` dan `limit`.
- **Langkah & Payload Uji (When)**: Mengirimkan `GET /api/v1/resource?page=abc&limit=sepuluh`.
- **Ekspektasi Hasil (Expected / Then)**: HTTP `400 Bad Request` / `422 Unprocessable Entity` dengan rincian validasi tipe data, sistem tidak panic/500.
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Validasi Type Mismatch](./screenshots/qa-neg-001-type-mismatch-pass.png)
  *Gambar QA-3: Pesan validasi penolakan tipe data string pada field integer*

#### `TC-NEG-BOUND-002` — Nilai Negatif & Boundary Overflow pada ID / Paginasi
- **Kategori**: Negative Testing (Boundary Violation)
- **Modul**: Paginasi & Input Constraint
- **Prakondisi (Given)**: Endpoint paginasi aktif.
- **Langkah & Payload Uji (When)**: Mengirimkan query `GET /api/v1/resource?page=-5&limit=-50`.
- **Ekspektasi Hasil (Expected / Then)**: HTTP `400 Bad Request` (Constraint Violation).
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Validasi Boundary Error](./screenshots/qa-neg-002-boundary.png)
  *Gambar QA-4: Validasi batasan nilai minimum parameter*

---

### 3.3 Negative Testing — Malformed Payload & Security Injection

#### `TC-NEG-PAYLOAD-001` — Malformed JSON & Extra Unmapped Fields
- **Kategori**: Negative Testing (Malformed Payload)
- **Modul**: Request Body Parser
- **Prakondisi (Given)**: Endpoint `POST /api/v1/resource`.
- **Langkah & Payload Uji (When)**: Mengirimkan JSON tidak lengkap `{"name": "test"` dan extra field `{"role": "Superadmin"}`.
- **Ekspektasi Hasil (Expected / Then)**: HTTP `400 Bad Request`, payload cacat ditolak sebelum masuk logika usecase.
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Penolakan Malformed JSON](./screenshots/qa-neg-payload-001.png)
  *Gambar QA-5: Penolakan payload JSON rusak*

#### `TC-NEG-INJ-002` — Form Field Injection (SQLi & XSS String Tests)
- **Kategori**: Negative Testing (Form Input Sanitization)
- **Modul**: Form UI & Repository Layer
- **Prakondisi (Given)**: Form isian data aktif.
- **Langkah & Payload Uji (When)**: Memasukkan string `' OR '1'='1 --` dan `<script>alert('xss')</script>` pada input teks.
- **Ekspektasi Hasil (Expected / Then)**: Input disimpan aman via parameterized query (`pgxpool`), karakter di-escape di antarmuka web, tidak terjadi eksekusi script atau SQL error.
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Sanitisasi Form Injection](./screenshots/qa-neg-inj-002.png)
  *Gambar QA-6: Input tersanitasi dengan aman di antarmuka web*

---

### 3.4 Negative Testing — RBAC Authorization Gates

#### `TC-RBAC-001` — Penolakan Mutasi Data oleh Role Pengawas
- **Kategori**: Negative Testing (RBAC Authorization)
- **Modul**: Modul Transaksi & RBAC Middleware
- **Prakondisi (Given)**: User login sebagai role `Pengawas` (`pengawas@jogjakota.go.id`).
- **Langkah & Payload Uji (When)**: Mengirimkan request `POST /api/v1/transaksi` atau `DELETE /api/v1/transaksi/1`.
- **Ekspektasi Hasil (Expected / Then)**: HTTP `403 Forbidden` (`{"code": "ERR_FORBIDDEN"}`), tombol mutasi di UI tersembunyi/disabled.
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Tampilan Diuji**:
  ![Tampilan Read-Only Pengawas](./screenshots/qa-rbac-003-pengawas-readonly.png)
  *Gambar QA-7: Antarmuka read-only role Pengawas tanpa tombol mutasi*

#### `TC-RBAC-002` — Pembatasan Akses Log Aktivitas Pengguna
- **Kategori**: Negative Testing (RBAC Audit Access)
- **Modul**: Modul Log Aktivitas Pengguna (Audit Trail)
- **Prakondisi (Given)**: User login sebagai role `Operator` atau `Admin`.
- **Langkah & Payload Uji (When)**: Mengakses route `/settings/activity-logs` atau `GET /api/v1/pengaturan/activity-logs`.
- **Ekspektasi Hasil (Expected / Then)**: HTTP `403 Forbidden`, menu tidak tampak di sidebar.
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Blokir Akses Audit Trail](./screenshots/qa-rbac-004-audit-blocked.png)
  *Gambar QA-8: Halaman 403 Forbidden saat operator mengakses audit trail*

---

### 3.5 Object Storage MinIO & File Upload Validation

#### `TC-UPLOAD-001` — Upload Dokumen Valid via Presigned URL
- **Kategori**: Positive Testing (File Upload)
- **Modul**: MinIO Storage Service
- **Prakondisi (Given)**: User berhak mengunggah berkas PDF/JPG valid (< 5MB).
- **Langkah & Payload Uji (When)**: Mengunggah file `dokumen.pdf` melalui Presigned URL.
- **Ekspektasi Hasil (Expected / Then)**: File tersimpan dengan nama UUID v4, tautan presigned dapat diakses sementara (5–15 menit).
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Tampilan Diuji**:
  ![Upload Berhasil](./screenshots/qa-upload-001-success.png)
  *Gambar QA-9: Notifikasi berkas berhasil diunggah*

#### `TC-UPLOAD-NEG-002` — Upload File Terlarang & Extension Spoofing (Magic Bytes Check)
- **Kategori**: Negative Testing (File Security)
- **Modul**: MinIO Upload Validator
- **Prakondisi (Given)**: User mencoba mengunggah file berbahaya.
- **Langkah & Payload Uji (When)**: Mengunggah file binary executable `.exe` yang diubah ekstensinya menjadi `lampiran.pdf` atau `foto.jpg`.
- **Ekspektasi Hasil (Expected / Then)**: Sistem membaca header biner (*Magic Bytes*), menolak berkas dengan HTTP `400 Bad Request` / `422 Unprocessable Entity`.
- **Hasil Aktual (Actual Result)**: [Diisi setelah pengujian dieksekusi]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Penolakan File Spoofing](./screenshots/qa-upload-neg-002-magicbytes.png)
  *Gambar QA-10: Notifikasi error deteksi berkas tidak sah berdasarkan Magic Bytes*

---

## 4. 🐛 DAFTAR TEMUAN & ANOMALI (DEFECT LOG)

| ID Defect | Modul | TC Terkait | Deskripsi Temuan | Severity | Status | Iterasi Fix |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| `DEF-001` | [Nama Modul] | `TC-xxx-001` | [Deskripsi bug/kegagalan pengujian] | 🔴 Critical / 🟠 High / 🟡 Medium / 🔵 Low | Open / Fixed / Skipped | Iterasi 1/2/3 |

---

## 5. 📝 KESIMPULAN & LEMBAR PENGESAHAN

### 5.1 Kesimpulan Kelayakan Sistem
[Uraikan ringkasan kesimpulan kelayakan rilis aplikasi berdasarkan hasil pengujian skenario positif dan seluruh kategori skenario negatif.]

### 5.2 Lembar Pengesahan Pengujian Mutu

| Disusun Oleh | Diperiksa Oleh | Disetujui Oleh |
| :---: | :---: | :---: |
| <br><br>_______________________<br>**QA & Testing Specialist**<br>Tim Pengembang | <br><br>_______________________<br>**Lead Architect / Backend Lead**<br>Tim Pengembang | <br><br>_______________________<br>**Kepala Bidang Sistem Informasi**<br>Diskominfo Kota Yogyakarta |
