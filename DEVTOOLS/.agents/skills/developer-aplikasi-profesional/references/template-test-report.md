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
| Kategori Pengujian | Total TC | ✅ Pass | ❌ Fail | ⚠️ Partial | % Lulus |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Autentikasi & Login SSO Keycloak | 0 | 0 | 0 | 0 | — |
| Matriks Hak Akses RBAC 4 Role | 0 | 0 | 0 | 0 | — |
| Fungsionalitas Modul Inti (Positive Path) | 0 | 0 | 0 | 0 | — |
| **Negative Testing: Type Mismatch (Teks di Integer dll)** | 0 | 0 | 0 | 0 | — |
| **Negative Testing: Boundary & Length Violations** | 0 | 0 | 0 | 0 | — |
| **Negative Testing: Malformed Payload & Missing Fields** | 0 | 0 | 0 | 0 | — |
| **Negative Testing: Form Injection Sanitization** | 0 | 0 | 0 | 0 | — |
| Object Storage MinIO & Magic Bytes Check | 0 | 0 | 0 | 0 | — |
| **TOTAL** | **0** | **0** | **0** | **0** | **—** |

### 1.2 Status Kelayakan Rilis
> **Status: [✅ LAYAK RILIS / ❌ TIDAK LAYAK — ADA KEGAGALAN / ⚠️ KONDISIONAL]**
>
> [Narasi ringkas tentang hasil uji fungsional, ketahanan terhadap skenario negatif, dan kepatuhan sistem terhadap batas arsitektur.]

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

## 3. 🔍 DETAIL TEST CASE & HASIL PENGUJIAN

> [!NOTE]
> **Aturan Disiplin QA**: Seluruh skenario pengujian di bawah ini (baik **Positive Testing / Happy Path** maupun **Negative Testing**) **WAJIB dirancang dan disusun terlebih dahulu sebelum eksekusi testing dimulai**. Setelah pengujian dijalankan, hasil aktual (*Actual Result*), status kelulusan (*Status*), dan bukti visual tangkapan layar (*Screenshot*) dituangkan ke dalam dokumen laporan ini.

### 3.1 Autentikasi & Otorisasi

#### `TC-AUTH-001` — Login dengan akun SSO JSS valid `[SRS-F-01]`
- **Tipe**: Happy Path
- **Skenario**:
  - *Given*: Pengguna belum login dan mengakses halaman masuk SSO JSS.
  - *When*: Memasukkan kredensial JSS valid.
  - *Then*: Diarahkan ke Dashboard dengan token JWT valid.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Tampilan Diuji**:
  ![Login Berhasil](./screenshots/03-01-login-berhasil.png)
  *Gambar QA-1: Tampilan Dashboard setelah autentikasi SSO berhasil*

#### `TC-AUTH-002` — Request API tanpa Authorization Header / Token Expired
- **Tipe**: Negative Test (Unauthorized)
- **Skenario**: Mengirim request GET/POST ke protected endpoint tanpa bearer token.
- **Expected Result**: HTTP `401 Unauthorized`, response `{"code":"ERR_UNAUTHORIZED"}`.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Penolakan Sesi Habis](./screenshots/n-01-error-sesi-berakhir.png)
  *Gambar QA-2: Dialog penolakan akses tidak terotorisasi*

---

### 3.2 Negative Testing — Type Mismatch & Constraint Validation

#### `TC-NEG-TYPE-001` — Input Teks/String pada Field Numerik/Integer
- **Tipe**: Negative Test (Type Mismatch)
- **Target Endpoint / Form**: Endpoint dengan parameter `id`, `page`, `limit`, atau field numerik lainnya.
- **Payload Uji**: `GET /api/v1/resource?page=satu&limit=sepuluh` atau `{"age": "dua puluh", "amount": "sejuta"}`.
- **Expected Result**: HTTP `400 Bad Request` / `422 Unprocessable Entity` dengan rincian validasi tipe data salah, aplikasi tidak boleh panic/500.
- **Actual Result**: [Isi setelah pengujian]
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Pesan Error Validasi Type Mismatch](./screenshots/qa-neg-001-type-mismatch.png)
  *Gambar QA-3: Pesan validasi penolakan tipe data string pada field integer*

#### `TC-NEG-BOUND-002` — Nilai Negatif & Boundary Overflow pada Parameter ID/Paginasi
- **Tipe**: Negative Test (Boundary Violation)
- **Payload Uji**: `GET /api/v1/resource?page=-5&limit=-100` atau ID bernilai `999999999999999999999`.
- **Expected Result**: HTTP `400 Bad Request` (Constraint Violation).
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Pesan Error Batas Input](./screenshots/qa-neg-002-boundary.png)
  *Gambar QA-4: Validasi batasan nilai minimum/maksimum*

#### `TC-NEG-STR-003` — String Panjang Melampaui Batas Maksimum Karakter
- **Tipe**: Negative Test (Length Constraint)
- **Payload Uji**: Mengisi field judul (varchar 100) dengan 1.000 karakter string teks.
- **Expected Result**: Validasi menolak input dengan pesan *length exceeds 100 characters*.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Validasi Panjang Teks](./screenshots/qa-neg-003-max-length.png)
  *Gambar QA-5: Indikator panjang karakter melampaui batas*

---

### 3.3 Negative Testing — Malformed Payload & Security Payloads

#### `TC-NEG-PAYLOAD-001` — Malformed JSON & Extra Unmapped Fields (Mass Assignment)
- **Tipe**: Negative Test (Malformed Payload)
- **Payload Uji**: JSON cacat sintaks `{"name": "test"` dan injection field tak dikenal `{"role": "Superadmin", "is_admin": true}`.
- **Expected Result**: HTTP `400 Bad Request`, extra fields diabaikan secara ketat oleh DTO sanitizer.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Penolakan Malformed JSON](./screenshots/qa-neg-payload-001.png)
  *Gambar QA-6: Respon penolakan payload tidak valid*

#### `TC-NEG-INJ-002` — Form Field Injection (SQLi & XSS String Tests)
- **Tipe**: Negative Test (Security Input Sanitization)
- **Payload Uji**:
  - SQLi: `' OR '1'='1 --`
  - XSS: `<script>alert('xss')</script>`
- **Expected Result**: Input disimpan aman melalui parameterized queries `pgxpool`, karakter di-escape di antarmuka web, tidak dieksekusi sebagai script.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Form Sanitization Test](./screenshots/qa-neg-inj-002.png)
  *Gambar QA-7: Karakter khusus di-escape dengan aman pada antarmuka web*

---

### 3.4 Object Storage MinIO & File Upload Validation

#### `TC-UPLOAD-001` — Upload Dokumen Valid via Presigned URL
- **Tipe**: Happy Path
- **Expected Result**: Berkas terunggah ke MinIO dengan nama UUID v4, tautan privat via Presigned URL aktif 5–15 menit.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Tampilan Diuji**:
  ![Upload Berhasil](./screenshots/qa-upload-001-success.png)
  *Gambar QA-8: Notifikasi dokumen berhasil diunggah*

#### `TC-UPLOAD-NEG-002` — Upload File Terlarang & Extension Spoofing (Magic Bytes Check)
- **Tipe**: Negative Test (File Security)
- **Payload Uji**: Mengunggah berkas executable `.exe` atau script biner yang diubah ekstensinya menjadi `.jpg`.
- **Expected Result**: Sistem mendeteksi header biner tidak sesuai dan menolak file dengan HTTP `400 Bad Request`.
- **Status**: [ ] ✅ Pass  [ ] ❌ Fail
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Penolakan Upload File Terlarang](./screenshots/qa-upload-neg-002-magicbytes.png)
  *Gambar QA-9: Penolakan file spoofing berdasarkan Magic Bytes*

---

## 4. 🐛 DAFTAR TEMUAN & ANOMALI (DEFECT LOG)

| ID Defect | Modul | TC Terkait | Deskripsi Temuan | Severity | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `DEF-001` | [Modul] | `TC-xxx-001` | [Deskripsi temuan] | 🔴 Critical / 🟠 High / 🟡 Medium / 🔵 Low | Open / Fixed |

---

## 5. 📝 KESIMPULAN & LEMBAR PENGESAHAN

### 5.1 Kesimpulan
[Ringkasan kelayakan sistem terhadap pengujian fungsional dan ketahanan terhadap kasus uji negatif.]

### 5.2 Lembar Pengesahan

| Disusun Oleh | Diperiksa Oleh | Disetujui Oleh |
| :---: | :---: | :---: |
| <br><br>_______________________<br>**QA & Testing Specialist**<br>Tim Pengembang | <br><br>_______________________<br>**Lead Architect / Backend Lead**<br>Tim Pengembang | <br><br>_______________________<br>**Kepala Bidang Sistem Informasi**<br>Diskominfo Kota Yogyakarta |
