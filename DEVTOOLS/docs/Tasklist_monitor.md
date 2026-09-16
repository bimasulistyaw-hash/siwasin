# 📊 TASK LIST MONITORING PENGEMBANGAN SISTEM INFORMASI
> **Pemerintah Kota Yogyakarta — Dinas Komunikasi Informatika dan Persandian**

---

## 📌 Informasi Proyek
- **Nama Aplikasi**: `SIWASIN (Sistem Informasi Pengawasan Internal)`
- **OPD / Unit Kerja**: `Inspektorat Kota Yogyakarta`
- **Tahun Anggaran**: `2026`
- **Lead Architect / Pengembang**: `Antigravity 2.0 AI Assistant & Tim Developer Diskominfo`
- **Terakhir Diperbarui**: `2026-09-15`
- **Status Keseluruhan**: `[x] IN PROGRESS (Tahap 1 Completed)`

---

## 📈 Ringkasan Progres Proyek

```text
[███░░░░░░░░░░░░░░░░░] 18% Selesai
```

| Tahapan Kerja | Status | Total Task | Selesai | Persentase |
| :--- | :---: | :---: | :---: | :---: |
| **1️⃣ Blueprint (BRD+PRD+SRS)** | `COMPLETED` | 5 | 5 | 100% |
| **2️⃣ Kerangka Acuan Kerja (KAK)** | `PENDING` | 3 | 0 | 0% |
| **3️⃣ Developer & QA (App+Seeds+QA)** | `PENDING` | 9 | 0 | 0% |
| **4️⃣ User Manual (Panduan Pengguna)** | `PENDING` | 5 | 0 | 0% |
| **5️⃣ Security Pentest & Rilis** | `PENDING` | 6 | 0 | 0% |
| **TOTAL** | | **28** | **5** | **18%** |

---

## 📋 DAFTAR RINCIAN PEKERJAAN & CHECKLIST MONITORING

### 1️⃣ TAHAP 1: BLUEPRINT & SPESIFIKASI ARSITEKTUR (`pembuat-blueprint-profesional`)
*Fokus: Menggali kebutuhan bisnis (BRD), fitur produk (PRD), spesifikasi teknis (SRS), rencana modular (MOD), dan UI (Apple HIG).*

- [x] **1.1. Pre-Flight Check**: Memastikan mode `caveman` aktif dan CLI diagram `mermaid` (`@mermaid-js/mermaid-cli`) terpasang.
- [x] **1.2. Wawancara Terstruktur**: Menjalankan tanya-jawab per fase (BRD → PRD → SRS) dan mencatat seluruh transkrip ke `docs/INTERVIEW_LOG.md`.
- [x] **1.3. Konfirmasi Alur Bisnis Modul**: Menanyakan opsi penentuan alur proses bisnis kepada prompter (Didefinisikan Sendiri [A] / Rekomendasi AI [B]) dan memastikan anti-halusinasi AI.
- [x] **1.4. Penerbitan Blueprint Teknis & Penguncian ERD 100%**: Menghasilkan `Blueprint.md` (SSOT di root) lengkap dengan diagram Mermaid, Halaman Login Terpisah (4 Dummy Users), 5 Modul Pengaturan Sistem (termasuk Sidebar Drag-to-Reorder), Log Aktivitas Pengguna, Matriks Keterlacakan, dan penguncian skema ERD global 100% sebelum coding dimulai.
- [x] **1.5. Penerbitan Dokumen Resmi**: Mengompilasi `docs/Dokumen_Blueprint_Resmi.docx` dan menginisialisasi `docs/MODULE_PROGRESS.md`.

---

### 2️⃣ TAHAP 2: KERANGKA ACUAN KERJA (KAK / TOR) (`pembuat-kak-profesional`)
*Fokus: Administrasi pengadaan resmi standar LKPP dan Diskominfo Kota Yogyakarta.*

- [ ] **2.1. Ekstraksi Data Acuan**: Mengekstrak data anggaran, DPA, Renstra, dan spesifikasi dari `Blueprint.md` atau rekaman audio.
- [ ] **2.2. Penyusunan Rincian KAK**: Menetapkan Latar Belakang, Maksud & Tujuan, Pagu/HPS, Kualifikasi 7 Tenaga Ahli, dan Jadwal Milestone.
- [ ] **2.3. Penerbitan Dokumen KAK Resmi**: Menghasilkan `docs/Dokumen_KAK_Resmi.docx` (lengkap dengan lembar pengesahan PPK) dan `docs/KAK.md`.

---

### 3️⃣ TAHAP 3: REKAYASA, PEMBANGUNAN REAL APLIKASI & QA TESTING (`developer-aplikasi-profesional`)
*Fokus: Setup infrastruktur, direct-to-real full-stack (tanpa mockup statis), real DB dummy seeds, audit kelengkapan fitur 100%, E2E QA testing, auto-fix mandiri, dan penerbitan laporan QA & Form UAT DOCX.*

- [ ] **3.1. Validasi Infrastruktur & Layanan**: Konfirmasi mode Docker Compose / Native Lokal (PostgreSQL 16+, Redis 7+, MinIO, Portainer, Nginx).
- [ ] **3.2. Core Foundation & Real Database Seeding**:
  - [ ] Inisiasi pelacak `docs/MODULE_PROGRESS.md` mengekstrak 100% ID `SRS-F-xx` dari `Blueprint.md`.
  - [ ] Migrasi database dasar & **Seed 4 Dummy Users langsung ke PostgreSQL** (`db/migrations/`, `db/seeds/`).
  - [ ] Backend Clean Architecture core engine (JWT Keycloak, Mock Auth Sandbox, RBAC 4 role).
  - [ ] Frontend base shell Apple HIG, **Halaman Login Terpisah (`/login`)**, dan **Brand Unit (`logo-jogja.svg` + Nama Aplikasi)**.
- [ ] **3.3. Pembangunan Real Full-Stack Modul Bisnis (Direct-to-Real, 100% Real API Connected)**:
  - [ ] Implementasi bertahap modul per-modul, fungsi per-fungsi tuntas end-to-end: Skema DB SQL $\rightarrow$ Real Seeds $\rightarrow$ Clean Arch Go $\rightarrow$ Frontend UI terhubung langsung ke API (tanpa mock in-memory).
- [ ] **3.4. Implementasi 5 Modul Pengaturan Sistem & Log Aktivitas**:
  - [ ] Manajemen Pengguna (Form ID JSS + Nama terisi otomatis + Role)
  - [ ] Manajemen Role (Proteksi role aktif tidak boleh dihapus)
  - [ ] Manajemen Hak Akses (Matriks izin per-role: Lihat, Tambah, Ubah, Hapus & toggle switch)
  - [ ] Manajemen Menu Sidebar (**Pengurutan menu interaktif via geser / drag-and-drop / drag-to-reorder**)
  - [ ] Manajemen Tema (8 Tema terstandarisasi anti-color clash)
  - [ ] Log Aktivitas Pengguna / Audit Trail (Akses eksklusif hanya untuk role Superadmin dan Pengawas; role lain 403 Forbidden)
- [ ] **3.5. Dokumentasi API, Swagger & Auto-Generate TypeScript Client**: Mounting Swagger UI otomatis di `/swagger/index.html`, sinkronisasi `docs/swagger.json`, `docs/swagger.yaml`, `docs/Dokumen_Spesifikasi_API.docx`, serta auto-generate interface TypeScript (`frontend/src/types/api.ts`).
- [ ] **3.6. Quality Gate: Audit Kelengkapan Fitur 100% (Anti-Tertinggal)**:
  - [ ] Meneliti ulang seluruh kebutuhan fungsional `SRS-F-xx` dan modul `MOD-xx` dari `Blueprint.md` terhadap tabel database, endpoint backend, dan komponen frontend.
  - [ ] Memastikan tidak ada fungsi tertinggal, kode stub kosong (`// TODO`), atau tombol UI yang belum memanggil API backend.
  - [ ] Memastikan status pelacak `docs/MODULE_PROGRESS.md` mencapai 100% `✅ Completed`.
- [ ] **3.7. Auto-Launch Aplikasi Live & Sesi Review Modul Bersama Prompter**:
  - [ ] Menjalankan seluruh stack layanan (Backend Go, Frontend Vite, PostgreSQL, MinIO) secara otomatis di background task tanpa menunggu instruksi manual prompter.
  - [ ] Memberikan URL akses live dan kredensial 4 role dummy sandbox kepada prompter.
  - [ ] Mengundang prompter melakukan peninjauan modul per modul serta mengonfirmasi apakah ada bagian yang perlu disesuaikan sebelum beralih ke tahap QA testing.
- [ ] **3.8. Pengujian Menyeluruh (QA), Auto-Fix Mandiri & Penerbitan Dokumen QA & Form UAT**:
  - [ ] **Penyusunan Skenario Pengujian (Wajib Sebelum Testing)**: Merancang skenario pengujian tertulis mencakup Positive Testing (Happy Path) dan Negative Testing (9 matriks cacat/error) lengkap dengan given-when-then & expected result.
  - [ ] **Kepatuhan Eksekusi 100% Terhadap Skenario**: Eksekusi pengujian FE $\leftrightarrow$ API $\leftrightarrow$ DB dan automated negative test suite Go (`backend/tests/negative_test.go`) patuh mutlak pada parameter input, payload, dan kriteria assertion skenario.
  - [ ] **Auto-Fix Mandiri (Maks. 3x)**: Langsung memperbaiki kegagalan/error secara mandiri hingga maksimal 3 kali percobaan. Jika tetap gagal, konfirmasi prompter (Lanjut/Skip).
  - [ ] Mengambil screenshot bukti uji ke `docs/screenshots/qa-*`.
  - [ ] **Penuangan Hasil ke Dokumen QA**: Menuangkan seluruh hasil pengujian aktual dan embed screenshot ke `docs/TEST_REPORT.md` serta mengompilasi dokumen Word resmi `docs/Laporan_Pengujian_QA.docx` (Coverage ≥ 85%).
  - [ ] **Penerbitan Dokumen Formulir UAT Resmi**: Menyediakan formulir uji terima calon pengguna `docs/Form_UAT_Resmi.docx` dan `docs/Form_UAT_Resmi.md` lengkap dengan berita acara dan checklist penerimaan OPD.
- [ ] **3.9. Verifikasi Diagnostic Healthcheck**: Memastikan endpoint `/api/v1/health` mengembalikan status `UP` untuk seluruh layanan.

---

### 4️⃣ TAHAP 4: PENYUSUNAN BUKU PANDUAN PENGGUNA (USER MANUAL) (`pembuat-user-manual-profesional`)
*Fokus: Penelusuran antarmuka, penangkapan screenshot langkah demi langkah, dan penerbitan buku panduan pengguna formal Word berstandar ISO/IEC/IEEE 26514.*

- [ ] **4.1. Pre-Flight Screenshot Tool**: Menjalankan `.agents/scripts/capture_screenshots.py --check` untuk memvalidasi Google Chrome / Playwright.
- [ ] **4.2. Penelusuran Browser & Capture Screenshot Antarmuka**: Mengambil tangkapan layar prosedur nyata di browser ke `docs/screenshots/um-*`.
- [ ] **4.3. Penyusunan Panduan Akses & 4 Role Dummy**: Mendokumentasikan prosedur login SSO Keycloak dan akses 4 role dummy testing sandbox pada halaman login terpisah.
- [ ] **4.4. Penyusunan Prosedur Modul Bisnis & Pengaturan Sistem**: Menulis instruksi langkah kerja bernomor untuk seluruh modul bisnis dan pengaturan sistem (termasuk fitur geser urutan sidebar & 8 tema UI).
- [ ] **4.5. Penerbitan Buku Panduan Pengguna Resmi DOCX**: Mengompilasi `docs/Panduan_Penggunaan_Aplikasi.docx` (berstandar ISO/IEC/IEEE 26514 lengkap screenshot langkah kerja) dan `docs/USER_MANUAL.md`.

---

### 5️⃣ TAHAP 5: AUDIT KEAMANAN (PENTEST) & PERSIAPAN RILIS (`security-pentester-profesional`)
*Fokus: Audit SAST/SCA/DAST berstandar internasional, bukti PoC screenshot, gatekeeper 0 kerentanan, dan rilis BAST.*

- [ ] **5.1. Audit SAST & SCA**: Menjalankan scanning kode statis (`gosec`, `semgrep`, `govulncheck`, `npm audit`).
- [ ] **5.2. Audit DAST Pentest**: Pengujian penetrasi live endpoints (OWASP Top 10, WSTG v4.2, ASVS v4.0, NIST SP 800-115, OSSTMM).
- [ ] **5.3. Penangkapan Bukti PoC Keamanan**: Menyimpan screenshot bukti respon pengujian dan kontrol keamanan ke `docs/screenshots/sec-*`.
- [ ] **5.4. Penerbitan Laporan Resmi Pentest**: Menghasilkan `docs/Dokumen_Laporan_Pentest_Resmi.docx` dan `docs/SECURITY_REPORT.md`.
- [ ] **5.5. Pengisian Lembar Kerja Audit WSTG**: Melengkapi `docs/WSTG_AUDIT_CHECKLIST.md`.
- [ ] **5.6. Security Gatekeeper & Pencatatan Changelog**:
  - [ ] Memastikan 0 temuan berstatus Medium / High / Critical.
  - [ ] Mendokumentasikan riwayat rilis pada `docs/CHANGELOG.md`.
  - [ ] Sistem siap Berita Acara Serah Terima (BAST) & Production Deployment.

---

## 🛠️ Panduan Pembaruan Task List untuk Prompter & Developer
1. Beri tanda centang `[x]` pada setiap item pekerjaan yang telah diselesaikan.
2. Perbarui baris **Persentase** dan **Status Keseluruhan** di bagian atas dokumen.
3. Seluruh file artefak output yang tertera pada setiap task wajib dipastikan keberadaannya di folder `docs/` atau lokasi target.
