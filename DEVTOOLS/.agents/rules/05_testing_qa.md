# 🧪 RULE: AUTOMATED TESTING, QA & DISCIPLINE REPORTING
> **Standar Pengujian Mutu Perangkat Lunak & Quality Assurance Diskominfo Kota Yogyakarta**

---

## 1. Standar 4 Tahapan Siklus Pengujian Mutu (Testing Lifecycle)

Proses pengujian perangkat lunak di lingkungan Diskominfo Kota Yogyakarta **WAJIB** melalui 4 tahapan berurutan berikut secara disiplin:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        4 TAHAPAN SIKLUS PENGUJIAN MUTU (QA LIFECYCLE)                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. PERANCANGAN SKENARIO PENGUJIAN (SEBELUM TESTING DIMULAI)                            │
│    • DILARANG KERAS langsung menguji tanpa skenario tertulis yang terdefinisi jelas.   │
│    • Merancang skenario Positive Testing (Happy Path) untuk alur normal & sukses.      │
│    • Merancang skenario Negative Testing (9 Matriks Cacat/Error) untuk ketahanan.      │
│    • Menetapkan Test Case ID, Fitur Terkait (SRS-F-xx), Given/When/Then, & Expected.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. EKSEKUSI PENGUJIAN MENYELURUH (TEST EXECUTION)                                      │
│    • Eksekusi pengujian berpedoman mutlak pada skenario yang telah disusun.           │
│    • Verifikasi integrasi menyeluruh: Frontend ↔ API Backend ↔ PostgreSQL & MinIO.     │
│    • Eksekusi Automated Negative Test Suite Go (`backend/tests/negative_test.go`).     │
│    • Pengujian form UI & RBAC 4 dummy user (Superadmin, Pengawas, Admin, Operator).    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. PROTOKOL AUTO-FIX MANDIRI (SELF-HEALING LOOP MAKS. 3X)                              │
│    • Jika ditemukan kegagalan/bug, developer langsung perbaiki kode sumber otomatis.  │
│    • Maksimal 3 kali iterasi perbaikan mandiri.                                        │
│    • Jika tetap gagal setelah 3x: Eskalasi ke prompter (Lanjutkan / Skip ke laporan).  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. PENUANGAN HASIL KE DOKUMEN LAPORAN PENGUJIAN QA                                     │
│    • Menuangkan hasil aktual (Actual Result) dan Status (✅ Pass / ❌ Fail).           │
│    • Menyematkan tangkapan layar bukti visual pengujian (`docs/screenshots/qa-*`).    │
│    • Menerbitkan dokumen SSOT Markdown `docs/TEST_REPORT.md`.                          │
│    • Mengompilasi Dokumen Word Resmi Siap Cetak `docs/Laporan_Pengujian_QA.docx`.      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Kebijakan Pokok Pengujian
1. **Wajib Ada Skenario Sebelum Eksekusi**: Setiap pengujian fitur **WAJIB** diawali dengan pembuatan skenario uji tertulis (baik kasus positif maupun negatif) sebelum perintah test atau penelusuran antarmuka dimulai.
2. **Kepatuhan Mutlak Eksekusi Terhadap Skenario (100% Traceability & Compliance)**:
   - Eksekusi testing **WAJIB 100% berpedoman dan merujuk 1-to-1 pada ID Test Case** yang telah didefinisikan dalam skenario.
   - Langkah uji, HTTP method, URL endpoint, dan payload data saat pengetesan **WAJIB PERSIS SAMA** dengan kolom *When / Payload Uji* pada skenario.
   - Evaluasi kelulusan (Assertion) **WAJIB MENGIKUTI KETAT** kolom *Then / Expected Result*. Jika respon aktual berbeda dari ekspektasi skenario, status **MUTLAK ❌ FAIL** (dilarang memanipulasi atau memperlunak ekspektasi skenario di tengah jalan).
   - Seluruh skenario yang telah dirancang wajib dieksekusi tuntas tanpa ada yang diabaikan (*100% Test Execution Rate*).
3. **Cakupan Pengujian Seimbang**: Tidak boleh hanya menguji alur sukses. Pengujian wajib mencakup *Positive Path* dan seluruh 9 matriks *Negative Testing*.
4. **Target Code Coverage**: Minimal **85%** pada layer business logic (usecase) dan delivery (handlers).
5. **Kewajiban Bukti Visual (Screenshot Evidence)**:
   - Setiap pengujian fitur antarmuka web (UI) dan alur pengguna **WAJIB** menyertakan screenshot nyata dari tampilan aplikasi yang sedang diuji (baik *Happy Path*, status validasi form, penolakan tipe data mismatch, halaman 403 Forbidden RBAC, maupun dialog error).
   - Seluruh aset screenshot disimpan di direktori `docs/screenshots/` dengan format penamaan terstandarisasi: `docs/screenshots/qa-[modul]-[skenario]-[status].png`.
   - Screenshot **WAJIB disematkan** (embedded) pada laporan pengujian `docs/TEST_REPORT.md` dan `docs/Laporan_Pengujian_QA.docx`.
6. **Sinkronisasi Dokumentasi API**: Setiap endpoint baru atau perubahan skema payload **WAJIB** terverifikasi memiliki anotasi Swagger yang valid dan tersinkronisasi pada `docs/swagger.json`, `docs/swagger.yaml`, serta `docs/Dokumen_Spesifikasi_API.docx`.
7. **Deliverables Hasil Pengujian & Dokumen UAT Calon Pengguna**:
   - `docs/TEST_REPORT.md` — Laporan pengujian fungsional & teknis markdown di repositori disertai skenario awal, hasil aktual, dan screenshot bukti uji.
   - `docs/Laporan_Pengujian_QA.docx` — Dokumen resmi formal laporan pengujian QA berformat Microsoft Word lengkap dengan gambar screenshot bukti uji.
   - `docs/Form_UAT_Resmi.docx` & `docs/Form_UAT_Resmi.md` — Dokumen Formulir Uji Terima Pengguna (User Acceptance Testing) resmi berformat Microsoft Word siap cetak untuk diisi oleh calon pengguna / OPD saat uji terima sistem.

---

## 2. Format Baku Skenario Pengujian (Wajib Dibuat Sebelum Testing Dimulai)

Sebelum melakukan eksekusi pengujian, rancang setiap kasus uji menggunakan format terstandarisasi berikut:

```markdown
### `[ID-TEST-CASE]` — [Judul Skenario Pengujian] `[ID-SRS-F]`
- **Kategori**: [Positive Testing (Happy Path) / Negative Testing (Kategori)]
- **Modul / Fitur**: [Nama Modul / Endpoint / Form UI]
- **Tujuan Pengujian**: [Deskripsi singkat tujuan pengujian]
- **Prakondisi (Given)**: [Keadaan awal sistem atau data sebelum aksi dijalankan, misal: User berstatus login sebagai Operator]
- **Langkah & Payload Uji (When)**: [Aksi pengujian, HTTP method & endpoint, atau payload JSON yang dikirimkan]
- **Ekspektasi Hasil (Then / Expected Result)**: [Respon yang diharapkan, kode HTTP misal 200/400/403, pesan error validasi, atau tampilan UI yang diharapkan]
```

### Tabel Rangkuman Skenario: Positive vs Negative Testing
```
┌────────────────────────────────────────────────────────────────────────┐
│                        SKEMA PENGUJIAN KOMPREHENSIF                    │
├───────────────────────────────────┬────────────────────────────────────┤
│         POSITIVE TESTING          │          NEGATIVE TESTING          │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Valid input & Happy path        │ • Type mismatch (teks di integer)  │
│ • Valid session & Role matrix     │ • Boundary & Length violations     │
│ • Expected response 200/201       │ • Malformed JSON & Missing fields  │
│ • Successful file upload          │ • Form payload injection (SQL/XSS) │
│ • Valid state transitions         │ • RBAC bypass & Tampered tokens    │
│ • Screenshot bukti tampilan UI    │ • File spoofing & Size limits      │
│                                   │ • Screenshot pesan/dialog validasi │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 3. Matriks Kategori Pengujian Negatif (Negative Testing Matrix)

Setiap endpoint API dan form UI **WAJIB** diuji terhadap 9 kategori pengujian negatif berikut:

### 3.1 Type Mismatch & Invalid Data Types
- **Skenario**: Mengirimkan tipe data yang tidak sesuai dengan definisi DTO/skema.
- **Contoh Kasus**:
  - Field `id`, `age`, `amount`, `page`, `limit` (tipe integer) diisi dengan string/teks: `{"limit": "sepuluh"}`, `{"page": "abc"}`.
  - Field bertipe boolean diisi angka atau teks acak.
  - Field bertipe object/array diisi primitive type atau sebaliknya.
- **Expected Result**: HTTP `400 Bad Request` atau `422 Unprocessable Entity` dengan pesan error validasi yang spesifik, sistem tidak mengalami *panic* / *500 Internal Server Error*.
- **Bukti Visual**: Screenshot form UI menampilkan pesan validasi tipe data tidak sesuai.

### 3.2 Boundary Value & Length Limit Violations
- **Skenario**: Mengirimkan nilai di luar batas minimum/maksimum yang diizinkan.
- **Contoh Kasus**:
  - Nilai negatif pada ID atau paginasi: `page = -1`, `limit = -50`.
  - Integer overflow: angka melebihi batas tipe integer (`99999999999999999999`).
  - String panjang melampaui `max_length` kolom database (misal varchar(50) diisi 500 karakter).
  - String kosong (`""`) atau hanya spasi (`"   "`) pada kolom wajib (*required*).
- **Expected Result**: HTTP `400 Bad Request` dengan deskripsi *field exceeds maximum constraint*.
- **Bukti Visual**: Screenshot pesan error batasan input pada antarmuka.

### 3.3 Malformed Payload & Syntax Errors
- **Skenario**: Payload body request cacat atau tidak sesuai format JSON standar.
- **Contoh Kasus**:
  - Sintaks JSON rusak: missing curly brace `{"name": "test"`, trailing comma.
  - Request body kosong pada method `POST` / `PUT` / `PATCH`.
  - *Mass Assignment attempt*: Menyisipkan field tak terduga seperti `{"role": "Superadmin", "is_admin": true}` pada endpoint registrasi/profil umum.
  - Menyisipkan nilai `null` pada non-nullable fields.
- **Expected Result**: HTTP `400 Bad Request`, extra fields diabaikan atau ditolak ketat.

### 3.4 Missing Mandatory Fields
- **Skenario**: Menghilangkan field wajib satu per satu dari payload request.
- **Contoh Kasus**:
  - Request pembuatan transaksi tanpa menyertakan field `user_id` atau `items`.
- **Expected Result**: HTTP `400 Bad Request` / `422` merinci daftar field yang wajib diisi (*required validation*).
- **Bukti Visual**: Screenshot highlight merah / alert pada form isian yang kosong.

### 3.5 Security Payloads & Injection Strings in Form Fields
- **Skenario**: Memasukkan string berbahaya ke dalam field input teks.
- **Contoh Kasus**:
  - SQL Injection strings: `' OR '1'='1`, `admin' --`, `1; DROP TABLE users;`.
  - Cross-Site Scripting (XSS): `<script>alert('xss')</script>`, `<img src=x onerror=alert(1)>`.
  - Path Traversal: `../../../../etc/passwd`, `..\\..\\windows\\system32`.
  - Null Byte injection: `dokumen.pdf%00.exe`.
- **Expected Result**: Input disanitasi / dievaluasi aman melalui parameterized query (`pgxpool`), karakter khusus di-encode, atau ditolak dengan HTTP `400`. Sistem tidak boleh mengeksekusi payload.
- **Bukti Visual**: Screenshot form yang meng-escape payload atau menolak submit dengan aman.

### 3.6 Format & Regex Violations
- **Skenario**: Input data dengan format tidak sesuai standar spesifikasi.
- **Contoh Kasus**:
  - Format email invalid: `user@`, `user@domain`, `@domain.com`.
  - UUID format invalid: `12345-abc` pada endpoint `/api/v1/resource/:id`.
  - NIK tidak 16 digit numerik, No HP berisi huruf.
  - Tanggal dengan format salah (`31-02-2026`, format string acak).
- **Expected Result**: HTTP `400 Bad Request` dengan keterangan format tidak valid.
- **Bukti Visual**: Screenshot notifikasi format salah pada form UI.

### 3.7 Authentication & Authorization Failure Paths
- **Skenario**: Pengujian kegagalan autentikasi dan penegakan batas wewenang role (RBAC).
- **Contoh Kasus**:
  - Request ke protected endpoint tanpa `Authorization` header -> HTTP `401 Unauthorized`.
  - Request menggunakan token JWT kedaluwarsa (*expired*) -> HTTP `401 Unauthorized`.
  - Request menggunakan token dengan tanda tangan (*signature*) palsu / dimanipulasi -> HTTP `401 Unauthorized`.
  - Role `Pengawas` mencoba melakukan mutasi data (`POST`, `PUT`, `DELETE`) -> HTTP `403 Forbidden`.
  - Role `Operator` mencoba mengakses endpoint manajemen user/konfigurasi aplikasi -> HTTP `403 Forbidden`.
- **Expected Result**: Penolakan tegas dengan kode HTTP 401/403 tanpa kebocoran data (*data leakage*).
- **Bukti Visual**: Screenshot halaman 403 Forbidden / tombol aksi tersembunyi/disabled untuk role terbatas.

### 3.8 Resource Conflict & State Violations
- **Skenario**: Operasi yang melanggar integritas relasi atau status siklus data.
- **Contoh Kasus**:
  - Menyimpan data dengan nilai unik yang sudah terdaftar (*duplicate key violation*) -> HTTP `409 Conflict`.
  - Mengubah atau menghapus data yang tidak ada di database (`ID not found`) -> HTTP `404 Not Found`.
  - Mengubah status entitas yang sudah berstatus final (*invalid state machine transition*) -> HTTP `422 Unprocessable Entity`.
- **Expected Result**: Pesan kesalahan bisnis yang jelas dan konsisten.
- **Bukti Visual**: Screenshot toast/modal notifikasi konflik data.

### 3.9 File Upload Negative Tests (MinIO)
- **Skenario**: Pengujian pengunggahan berkas tidak aman.
- **Contoh Kasus**:
  - Mengunggah berkas dengan ekstensi terlarang (`.exe`, `.php`, `.sh`, `.bat`, `.html`).
  - *Extension Spoofing*: File biner executable diubah namanya menjadi `.jpg` atau `.pdf` (wajib ditolak melalui verifikasi header biner / *Magic Bytes*).
  - Ukuran file melebihi kuota batas maksimal (misal > 5MB).
  - Mengunggah file kosong (0 bytes).
- **Expected Result**: HTTP `400 Bad Request` / `413 Payload Too Large`, file ditolak sebelum disimpan ke MinIO Object Storage.
- **Bukti Visual**: Screenshot dialog error penolakan tipe berkas / ukuran melebihi batas.

---

## 4. Format Laporan Pengujian (`docs/TEST_REPORT.md`)

```markdown
# 📊 Laporan Hasil Pengujian Fungsional & Negative Testing

- **Nama Aplikasi**: [Nama Aplikasi]
- **Versi**: [1.0.0]
- **Tanggal Pengujian**: YYYY-MM-DD HH:mm:ss WIB
- **Penguji**: QA & Testing Agent
- **Target Code Coverage**: Min. 85% (Capaian: XX%)
- **Folder Bukti Tangkapan Layar**: `docs/screenshots/`

## 1. Ringkasan Eksekutif Pengujian
| Kategori Pengujian | Total Kasus | ✅ Pass | ❌ Fail | ⚠️ Partial | Persentase |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Autentikasi SSO Keycloak & Session | 10 | 10 | 0 | 0 | 100% |
| RBAC 4 Role Matrix & Unauthorized Access | 12 | 12 | 0 | 0 | 100% |
| Negative Testing: Type Mismatch & Boundaries | 15 | 15 | 0 | 0 | 100% |
| Negative Testing: Malformed Payload & Injection | 10 | 10 | 0 | 0 | 100% |
| MinIO Upload (Valid & Negative Magic Bytes) | 8 | 8 | 0 | 0 | 100% |
| Core Business Logic (Positive & Sad Path) | 20 | 20 | 0 | 0 | 100% |
| **TOTAL** | **75** | **75** | **0** | **0** | **100%** |

## 2. Detail Pengujian Fungsional & Bukti Visual (Sample Test Cases)

### `TC-AUTH-001` — Login SSO JSS Valid & Masuk Dashboard
- **Tipe**: Happy Path (Positive Test)
- **Skenario**: Pengguna memasukkan kredensial JSS valid dan diarahkan ke Dashboard.
- **Expected Result**: Login berhasil, token JWT tersimpan, dashboard tampil.
- **Actual Result**: Dashboard tampil lengkap dengan left panel navigation.
- **Status**: ✅ Pass
- **Bukti Screenshot Tampilan Diuji**:
  ![Dashboard Utama Setelah Login](./screenshots/qa-auth-001-dashboard-pass.png)
  *Gambar QA-1: Tampilan Dashboard setelah login SSO berhasil*

### `TC-NEG-001` — Input String pada Field Integer ID/Pagination
- **Tipe**: Negative Test (Type Mismatch)
- **Input**: `GET /api/v1/data?page=abc&limit=sepuluh`
- **Expected Result**: HTTP 400 Bad Request, payload JSON error standar.
- **Actual Result**: HTTP 400 Bad Request (`"code": "ERR_VALIDATION"`).
- **Status**: ✅ Pass
- **Bukti Screenshot Respon/Tampilan Diuji**:
  ![Validasi Error Type Mismatch](./screenshots/qa-neg-001-type-mismatch-pass.png)
  *Gambar QA-2: Pesan validasi penolakan tipe data string pada field integer*

### `TC-RBAC-003` — Penolakan Mutasi Data oleh Role Pengawas
- **Tipe**: Negative Test (RBAC Authorization)
- **Skenario**: Role Pengawas mencoba menekan tombol Hapus/Ubah transaksi.
- **Expected Result**: Tombol aksi non-aktif / request ditolak dengan HTTP 403 Forbidden.
- **Actual Result**: Tombol tersembunyi dan API merespon HTTP 403 Forbidden.
- **Status**: ✅ Pass
- **Bukti Screenshot Tampilan Diuji**:
  ![Tampilan Read-Only Pengawas](./screenshots/qa-rbac-003-pengawas-readonly.png)
  *Gambar QA-3: Antarmuka read-only role Pengawas tanpa tombol mutasi*
```

---

## 5. Pembuatan Dokumen DOCX Resmi Pengujian & Form UAT

### 5.1 Laporan Pengujian QA (`docs/Laporan_Pengujian_QA.docx`)
Setelah `docs/TEST_REPORT.md` terisi lengkap dan seluruh file screenshot tersimpan di `docs/screenshots/`:
```bash
python3 .agents/scripts/generate_docx.py -i docs/TEST_REPORT.md -o docs/Laporan_Pengujian_QA.docx -t "LAPORAN PENGUJIAN QA" --title "Laporan Hasil Pengujian Fungsional & Negative Testing" --app "[Nama Aplikasi]"
```
Dokumen `.docx` yang dihasilkan otomatis memuat seluruh screenshot bukti pengujian visual secara rapi dan proporsional.

### 5.2 Formulir Uji Terima Pengguna / UAT Resmi (`docs/Form_UAT_Resmi.docx`)
Untuk keperluan pengujian langsung dan penandatanganan berita acara uji terima oleh calon pengguna / OPD, sediakan dokumen formulir UAT formal:
```bash
python3 .agents/scripts/generate_docx.py -i docs/Form_UAT_Resmi.md -o docs/Form_UAT_Resmi.docx -t "FORMULIR UJI TERIMA PENGGUNA (UAT)" --title "Formulir Uji Terima Pengguna (User Acceptance Testing - UAT)" --app "[Nama Aplikasi]"
```
Dokumen ini siap dicetak atau diisi secara digital oleh calon pengguna saat sesi evaluasi penerimaan aplikasi berlangsung.

---

## 6. Automated Go Negative Testing Suite (`backend/tests/negative_test.go`)

Untuk mencegah pengujian negatif hanya sebatas catatan deskriptif di markdown, setiap backend Go **WAJIB** menyertakan file test runner otomatis `backend/tests/negative_test.go` (mengacu template `.agents/skills/developer-aplikasi-profesional/templates/negative_test.go`) yang mengeksekusi test matrix:
1. **Type Mismatch Assertion**: Menjamin input string pada kolom integer mengembalikan `400/422`.
2. **Boundary Overflow Assertion**: Menjamin panjang string > batas max atau limit negatif ditolak.
3. **Malformed JSON Body**: Menjamin payload JSON terpotong/rusak ditolak `400 Bad Request`.
4. **SQL Injection String Sanitization**: Menjamin string tautologi `' OR 1=1 --` aman dan tidak memicu SQL syntax error.
5. **Form XSS Sanitization**: Menjamin tag `<script>` tersanitasi.
6. **File Spoofing & Magic Bytes**: Menjamin file executable `.exe` berkedok `.jpg` ditolak `422`.
7. **RBAC Forbidden Gate**: Menjamin role `Pengawas` diblokir dari `POST/PUT/DELETE` (`403 Forbidden`) dan role `Admin`/`Operator` diblokir dari endpoint `/api/v1/pengaturan/activity-logs` (`403 Forbidden`).

Eksekusi wajib diverifikasi dengan perintah:
```bash
go test -v -coverprofile=coverage.out ./tests/...
go tool cover -func=coverage.out
```

---

## 7. Protokol Auto-Fix Mandiri (Self-Healing Loop) & Batas 3x Percobaan

Saat pengujian end-to-end FE-API-DB atau negative testing dijalankan:
1. **Pencatatan Status**: Catat setiap endpoint/fitur yang berstatus ✅ Pass atau ❌ Fail.
2. **Auto-Fix Mandiri (Maksimal 3 Kali Percobaan)**:
   - Jika ditemukan kegagalan (query DB error, submit form gagal, token JWT mismatch, HTTP 500), developer **WAJIB langsung memperbaiki root-cause pada source code secara mandiri** hingga maksimal 3 kali iterasi perbaikan.
3. **Eskalasi ke Prompter Setelah Percobaan ke-3**:
   - Jika setelah 3 kali perbaikan pengujian masih gagal, AI **WAJIB bertanya kepada prompter**:
     - *Pilihan [A] (Ya)*: Lanjutkan siklus perbaikan kode berikutnya.
     - *Pilihan [B] (Lewati/Skip)*: Lewati modul tersebut, lanjutkan pengerjaan, dan **tetap catat secara transparan** di `docs/TEST_REPORT.md` & `docs/Laporan_Pengujian_QA.docx` dengan status **`❌ FAIL (Dilewati atas konfirmasi prompter)`** beserta detail defect teknisnya.
