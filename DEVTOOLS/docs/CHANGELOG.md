# 📋 Change Log - [Nama Aplikasi]

Semua perubahan penting pada proyek ini terdokumentasi di dalam file ini.
Format acuan berdasar pada [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.6.0] - 2026-09-04
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead QA & Testing Specialist Team

### 🚀 Perubahan Terintegrasi
- **Enhanced (Disiplin Siklus Pengujian QA: Wajib Skenario Pengujian Sebelum Testing & Kepatuhan Eksekusi 100%)**: Memperbarui alur kerja dan aturan pengujian mutu pada `AGENTS.md`, `.agents/rules/05_testing_qa.md`, skill `developer-aplikasi-profesional`, `docs/Tasklist_monitor.md`, dan `README.md`.
- **Standarisasi Pre-Execution Test Scenarios**: Pengembang/QA **WAJIB merancang skenario pengujian tertulis secara lengkap** (mencakup kasus uji **Positive Testing / Happy Path** dan seluruh 9 matriks **Negative Testing**) lengkap dengan Test Case ID, ID SRS-F, prakondisi (*Given*), aksi/payload (*When*), dan hasil yang diharapkan (*Then / Expected Result*) **SEBELUM testing dieksekusi**.
- **Kepatuhan Mutlak Eksekusi Terhadap Skenario (100% Traceability)**: Eksekusi pengujian FE-API-DB dan negative test suite **WAJIB 100% konsisten berpedoman pada skenario yang dibuat**. Payload, method, input data, dan kriteria assertion tidak boleh diubah di tengah jalan demi meluluskan pengujian. Setiap ketidakcocokan terhadap Expected Result wajib dinyatakan ❌ FAIL.
- **Standarisasi Penuangan Hasil Pengujian QA**: Hasil pengujian aktual (*Actual Result*), status kelulusan (✅ Pass / ❌ Fail), defect log, dan screenshot bukti pengujian visual wajib dituangkan secara terstruktur ke dalam dokumen SSOT **`docs/TEST_REPORT.md`** dan dikompilasi menjadi dokumen Word resmi **`docs/Laporan_Pengujian_QA.docx`**.
- **Added (Dokumen Formulir UAT Resmi Siap Cetak & Isi)**: Menerbitkan **`docs/Form_UAT_Resmi.docx`** dan **`docs/Form_UAT_Resmi.md`** (beserta template di `.agents/skills/developer-aplikasi-profesional/references/template-form-uat.md`) sebagai dokumen formal uji terima calon pengguna yang memuat lembar verifikasi fitur per-modul, checklist penilaian pengguna, evaluasi usability Apple HIG, kolom saran, serta berita acara pengesahan untuk OPD/stakeholder.
- **Enhanced (Pengayaan Design System Apple HIG & WCAG a11y)**:
  - **Tokens Spacing & Sizing (`tokens/spacing.css`)**: Menambahkan token aksesibilitas ukuran target interaksi (`--target-touch-min: 44px`, `--target-click-min: 24px`, `--target-pointer-md: 32px`), token adaptasi area notch mobile (`--safe-area-*`), serta token Liquid Glass & Dimming Layer (`--glass-regular-bg`, `--glass-clear-bg`, `--glass-border`, `--glass-dimming-layer`).
  - **Tokens Warna & Kontras (`tokens/colors.css`)**: Menambahkan semantic status tokens (`--color-success-*`, `--color-error-*`, `--color-warning-*`, `--color-info-*`) dengan kontras WCAG $\ge 4.5:1$ serta high-visibility focus ring token (`--color-focus-ring`).
  - **Tokens Tipografi & Microcopy (`tokens/typography.css`)**: Menambahkan aturan penulisan *Sentence case* (`.ui-sentence-case`), perataan angka monospaced tabel keuangan (`.ui-tabular-nums`), serta base HTML scalable text support.
  - **Tailwind Config (`tailwind.config.js`)**: Mapping utility class `h-touch-min`, `min-h-touch`, `min-w-touch`, `click-min`, backdrop blur, dan background glass presets.
  - **Dokumentasi & Komponen (`components.md` & `README.md`)**: Menambahkan 4-tier Design Review Rubric (Critical, High, Medium, Low) dan prinsip wajib Apple HIG / WCAG (bebas warna tunggal untuk status, explicit label tanpa diganti placeholder, konfirmasi aksi destruktif).
- **Enhanced (Auto-Launch Aplikasi Live & Sesi Review Modul Bersama Prompter)**: Setelah seluruh modul selesai dibangun dan lolos Quality Gate Audit Kelengkapan Fitur 100%, developer **WAJIB LANGSUNG MENJALANKAN (AUTO-LAUNCH)** seluruh stack aplikasi di background task (tanpa menunggu perintah manual prompter). Developer menyajikan link URL live dan kredensial 4 role dummy sandbox, mengundang prompter memeriksa fungsionalitas modul per modul, serta menanyakan secara eksplisit apakah ada alur/fungsi yang perlu diperbaiki sebelum melangkah ke tahap pengujian QA.
- **Enhanced (ASCII Art Banner Logo Resmi Pemkot Yogyakarta)**: Memperbarui banner pembuka pada skill `pembuat-blueprint-profesional` (`.agents/skills/pembuat-blueprint-profesional/SKILL.md`) dengan ASCII art presisi lambang Pemerintah Kota Yogyakarta yang tertata rapi di tengah (center aligned) lengkap dengan metadata identitas resmi Diskominfo Kota Yogyakarta 2026.

---

## [1.5.0] - 2026-09-02
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead Architect & Developer Specialist Team

### 🚀 Perubahan Terintegrasi
- **Enhanced (Pengaturan Menu Sidebar Drag-and-Drop)**: Standarisasi modul `PRD-SET-04` (Manajemen Menu Sidebar) di mana pengurutan posisi dan hierarki menu **WAJIB menggunakan metode interaktif menggeser / drag-and-drop / drag-to-reorder**, bukan dengan memasukkan nomor urut menu secara manual.
- **Added (Halaman Login Terpisah & 4 Dummy Users Sandbox)**: Menyediakan halaman login tersendiri terpisah dari layout aplikasi utama (`/login` / `login.html`), dilengkapi form SSO Keycloak resmi dan panel testing sandbox yang memuat minimal 4 Dummy User (1 per role: `Superadmin`, `Pengawas`, `Admin`, `Operator`) dengan tombol *1-Click Quick Login*.
- **Enhanced (Real PostgreSQL Database Seeding)**: Pada skill `developer-aplikasi-profesional`, saat aplikasi dibangun secara penuh (bukan mockup), seluruh data dummy **WAJIB dimasukkan langsung ke dalam database real PostgreSQL** via migrasi dan script seeder SQL (`db/migrations/`, `db/seeds/`), bukan sekadar mock hardcode di level frontend atau in-memory.
- **Enhanced (Pengujian E2E, Auto-Fix Mandiri & QA Reporting)**: Pada skill `developer-aplikasi-profesional`, pengujian end-to-end menyeluruh (FE $\leftrightarrow$ API $\leftrightarrow$ DB) dan automated negative testing dieksekusi secara nyata. Jika ditemukan kegagalan/bug, developer **WAJIB langsung memperbaiki root-cause pada kode secara otomatis tanpa harus disuruh** hingga 100% PASS, serta menerbitkan `docs/Laporan_Pengujian_QA.docx` & `docs/TEST_REPORT.md` lengkap dengan screenshot bukti uji di `docs/screenshots/`.
- **Refactored & Separated (Skill Pembuat User Manual)**: Memisahkan tanggung jawab QA testing dari skill dokumentasi; skill kini difokuskan 100% untuk pembuatan Buku Panduan Penggunaan Aplikasi (User Manual) berstandar ISO/IEC/IEEE 26514 dengan penamaan **`pembuat-user-manual-profesional`** (`.agents/skills/pembuat-user-manual-profesional/`) yang menghasilkan `docs/Panduan_Penggunaan_Aplikasi.docx` & `docs/USER_MANUAL.md` dengan screenshot langkah kerja antarmuka per prosedur.

---

## [1.4.0] - 2026-09-02
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead QA, Architect & Design System Team

### 🚀 Perubahan Terintegrasi
- **Renamed & Enhanced**: Mengubah penamaan skill `pembuat-user-manual-profesional` menjadi **`testing-qa-dan-user-manual`** (`.agents/skills/testing-qa-dan-user-manual/`) yang mengintegrasikan Quality Assurance fungsional + negative testing sekaligus penyusunan buku panduan pengguna.
- **Added**: Utility diagnostik & screenshot otomatis **`.agents/scripts/capture_screenshots.py`** yang mendukung pre-flight check (`--check`), penangkapan headless Chrome CLI (1280×800 PNG), dan auto-fallback untuk penjaminan ketersediaan screenshot visual di `docs/screenshots/`.
- **Enhanced**: Kewajiban kompilasi ganda 2 dokumen deliverable formal Word (`.docx`) yang memuat screenshot aplikasi: **`docs/Laporan_Pengujian_QA.docx`** dan **`docs/Panduan_Penggunaan_Aplikasi.docx`** (beserta `docs/TEST_REPORT.md` dan `docs/USER_MANUAL.md`).
- **Enhanced**: Menggantikan seluruh referensi aset logo raster lama (`.jpg` / `.png`) dengan **Logo Resmi Vektor Kota Yogyakarta (`.agents/design-system/assets/logo-jogja.svg`)** beresolusi tinggi, tajam, dan bebas pixelation.
- **Added**: Standarisasi **Brand Unit Terintegrasi (`logo-jogja` + `[Nama Aplikasi]`)** pada `.agents/design-system/components.md` (komponen `AppBrand` untuk React/TypeScript, Vue 3, dan HTML statis), `AGENTS.md`, `01_architecture_clean.md`, serta seluruh skill developer & blueprint.
- **Enhanced**: Standarisasi **5 Modul Pengaturan Sistem Wajib** pada `AGENTS.md`, `02_sso_keycloak_rbac.md`, `components.md`, dan seluruh skills: (1) **Manajemen Pengguna** (Form ID JSS + Nama terisi otomatis + Role, list/tabel user), (2) **Manajemen Role** (Proteksi role aktif tidak boleh dihapus), (3) **Manajemen Hak Akses** (Matriks izin per-role terhadap Menu/Sub-menu dengan 4 aksi Lihat/Tambah/Ubah/Hapus & toggle switch), (4) **Manajemen Menu Sidebar** (Hierarki kategori header, menu/sub-menu, route, icon, badge status), (5) **Manajemen Tema dan Warna Tema** (8 tema terstandarisasi anti-color clash).
- **Enhanced**: Penguatan skill **`pembuat-blueprint-profesional`** dengan: (1) Jaminan rantai keterlacakan tanpa putus (**Traceability Chain `BR-xx` → `PRD-xx` → `SRS-F-xx` → `MOD-xx` → `UI-xx`**) pada Bagian F, (2) Protokol **Anti-Halusinasi AI** yang mewajibkan diagram alur bisnis langkah-demi-langkah dan rincian entitas/tabel per-modul, serta (3) Percabangan mode interaktif di awal pendalaman modul (apakah pengguna ingin mendefinisikan proses bisnis sendiri secara manual atau dibuatkan draft rekomendasi oleh AI).
- **Added**: Master pelacak dan monitoring proyek **`docs/Tasklist_monitor.md`** yang memuat 28 checklist rinci berurutan dari Tahap 1 hingga Tahap 5, progress bar, dan status verifikasi untuk prompter & developer.
- **Enhanced**: Kewajiban implementasi fitur **Log Aktivitas Pengguna (User Activity Log / Audit Trail)** pada setiap Blueprint (`PRD-SET-06`), `AGENTS.md`, dan `02_sso_keycloak_rbac.md` dengan penegakan RBAC eksklusif: **Hanya role `Superadmin` dan `Pengawas` (Read-Only) yang berhak mengakses**, sedangkan role `Admin` dan `Operator` diblokir (HTTP 403 Forbidden).
- **Added & Enhanced (Architectural Robustness)**:
  1. **Auto-Generate TypeScript Client dari OpenAPI**: Wajib men-generate interface frontend langsung dari `docs/swagger.json` (`npx -y openapi-typescript docs/swagger.json -o frontend/src/types/api.ts`) untuk menjamin 100% type-safety dan mencegah type drift.
  2. **Penguncian Skema ERD Global 100%**: Memastikan seluruh tabel, tipe data kolom, constraints, dan foreign keys tuntas di Bagian C.4 `Blueprint.md` sebelum coding modul dimulai.
  3. **Automated Go Negative Test Suite (`backend/tests/negative_test.go`)**: Menyediakan template test matrix otomatis (Type Mismatch, Boundary, Malformed JSON, SQLi, XSS, File Spoofing, dan RBAC Forbidden Gate) yang dieksekusi secara nyata via `go test -v ./tests/...`.
  4. **Banner Pembuka ASCII Resmi**: Menambahkan banner pembuka ASCII Logo Pemkot Yogyakarta dan identitas `DEVTOOL Vibe Coding V.1.11` centered di awal skill `pembuat-blueprint-profesional`.

---

## [1.3.0] - 2026-08-29
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead Architect & Developer Team

### 🚀 Perubahan Terintegrasi
- **Enhanced**: Implementasi **Protokol Eksekusi Modular Bertahap (Iterative Module Pipeline)** pada skill `developer-aplikasi-profesional` yang melarang keras *one-shot batch monolithic generation*, mencegah context exhaustion, kode stub kosong (`// TODO`), dan fitur yang terlewat.
- **Added**: Dokumen Pelacak Progres Modul (`docs/MODULE_PROGRESS.md` & `references/template-module-progress.md`) untuk mengunci traceability `SRS-F-xx` dari `Blueprint.md` dan memvalidasi penyelesaian menyeluruh per modul (DB Migration -> Backend Clean Arch -> Frontend UI Apple HIG -> Verification).
- **Enhanced**: Standarisasi **UI Component Contract (Apple HIG & Design System)** yang mewajibkan seluruh halaman UI mengonsumsi token dari `.agents/design-system/` (Card Squircle `rounded-2xl`, Frosted Glass Navigation, Interactive Data Table dengan search/filter/pagination, Form Modals terstandarisasi, dan Toast Notifications).
- **Added**: **Fase 4: Rencana Implementasi Modular (`MOD-xx`)** pada skill `pembuat-blueprint-profesional` (`SKILL.md` & `references/template-blueprint.md`) yang memetakan `SRS-F-xx` ke modul eksekusi (`MOD-xx`), urutan build & alur dependensi, struktur file/folder, skema tabel PostgreSQL persis, kontrak endpoint REST API, DoR/DoD teknis, dan spesifikasi UI Apple HIG per modul.
- **Added**: **BAGIAN E — SPESIFIKASI UI & DESAIN VISUAL (APPLE HIG)** pada `template-blueprint.md` dan Skema ID `UI-xx` pada `SKILL.md` yang mengunci token tema anti-color clash, reusabilitas komponen UI, matriks 4 state wajib per layar (Loading Skeleton, Empty State, Error Alert, Success Toast), tata letak responsif desktop/mobile, dan offline-first asset policy.
- **Added**: Artefak keluaran ke-5 `docs/MODULE_PROGRESS.md` (`MODULE_STATUS.md`), **Protokol Operasional Anti-Monolith (Slice-by-Slice Prompting)**, dan **Quality Gate Kesiapan Antigravity** pada `pembuat-blueprint-profesional/SKILL.md` untuk menjamin tidak ada modul yang dilompati atau digenerate secara monolitik.

---

## [1.2.0] - 2026-08-28
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead Architect, QA & Security Team

### 🚀 Perubahan Terintegrasi
- **Enhanced**: Standarisasi **Kewajiban Bukti Visual (Screenshot Evidence)** pada seluruh laporan pengujian QA (`docs/TEST_REPORT.md` & `docs/Laporan_Pengujian_QA.docx`), panduan pengguna (`docs/USER_MANUAL.md` & `docs/Panduan_Pengguna_[App].docx`), serta laporan audit keamanan/pentest (`docs/SECURITY_REPORT.md` & `docs/Dokumen_Laporan_Pentest_Resmi.docx`).
- **Enhanced**: Generator dokumen Word (`.agents/scripts/generate_docx.py`) ditingkatkan dengan kemampuan *auto-embed* gambar screenshot markdown (`![alt](path)`) beserta penataan posisi tengah, styling caption otomatis, dan penanganan fallback box.
- **Enhanced**: Skill `security-pentester-profesional` dan rule `04_security_owasp.md` disempurnakan dengan kewajiban menyertakan screenshot tampilan/hasil pengujian PoC kerentanan, hasil scan SAST/SCA, respon terminal/network, serta bukti kontrol keamanan positif.
- **Enhanced**: Penambahan **Kebijakan Offline-First Assets & Dummy Data** pada `03_minio_storage.md`, `pembuat-blueprint-profesional`, dan `AGENTS.md` yang melarang keras penggunaan URL gambar/dummy dari internet (Unsplash, Picsum, DiceBear, mock API online) dan mewajibkan penyimpanan di lokal (`frontend/src/assets/`, `db/seeds/`) atau MinIO lokal.
- **Enhanced**: Standarisasi **Jaminan Konektivitas Antar-Layanan (Pre-Wired Inter-Service Connectivity)** pada `01_architecture_clean.md`, `AGENTS.md`, dan `pembuat-blueprint-profesional` yang menjamin Backend, Frontend, PostgreSQL 16+, MinIO, Redis, dan Keycloak otomatis terhubung via environment, auto-migration startup, auto-bucket MinIO, serta diagnostic endpoint `/api/v1/health`.
- **Added**: Skill baru `developer-aplikasi-profesional` (`.agents/skills/developer-aplikasi-profesional/`) yang memandu: (1) Validasi & instalasi environment (Docker/Nginx/Postgres/Redis/MinIO/Portainer di Docker vs Lokal); (2) Prototyping mockup interaktif (HTML, CSS, JS) berbasis Blueprint; (3) Review & pencatatan revisi mockup ke `docs/MOCKUP_CHANGES.md`; (4) Pembangunan aplikasi produksi utuh (Go + React/Vue + SSO Keycloak + MinIO) terhubung otomatis ke seluruh layanan.
- **Added**: Log Transkrip Wawancara & Evaluasi (`docs/INTERVIEW_LOG.md` & `references/template-interview-log.md`) pada skill `pembuat-blueprint-profesional` untuk merekam seluruh pertanyaan, jawaban narasumber, dan evaluasi gap/traceability terhadap isi `Blueprint.md`.
- **Refined**: Panduan operasional dan diagram alur pada [`README.md`](file:///Users/kominfo/Nextcloud/AntiGravity/DEVTOOLS/README.md) diselaraskan secara presisi ke dalam urutan 5 langkah kerja berurutan: (1) `pembuat-blueprint-profesional`, (2) `pembuat-kak-profesional`, (3) `developer-aplikasi-profesional`, (4) `pembuat-user-manual-profesional`, dan (5) `security-pentester-profesional`.
- **Enhanced**: Standarisasi **Karakter Desain UI Berstandar Apple Human Interface Guidelines (HIG)** pada `AGENTS.md`, `01_architecture_clean.md`, `developer-aplikasi-profesional`, dan `pembuat-blueprint-profesional` yang mencakup: (1) Kepatuhan penuh Apple HIG (*Clarity, Deference, Depth*), (2) Tipografi San Francisco (`SF Pro Display` & `SF Pro Text`), (3) Ruang kosong (*generous whitespace* & 8pt grid system), serta (4) Efek transparansi & *frosted glass* (`backdrop-filter: blur(20px) saturate(180%)`).
- **Added**: Standarisasi **Identitas & Branding Resmi Pemerintah Kota Yogyakarta** pada seluruh aplikasi yang dihasilkan: (1) Logo Resmi Kota Yogyakarta (`assets/logo-pemkot-jogja.png`) wajib tampil pada pojok kiri atas diikuti nama aplikasi, dan (2) Footer wajib berformat `© [Tahun] Pemerintah Kota Yogyakarta`.

---

## [1.1.0] - 2026-08-27
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead Architect & Documentation Team

### 🚀 Perubahan Terintegrasi
- **Added**: Skill baru `pembuat-kak-profesional` untuk penyusunan Dokumen Kerangka Acuan Kerja (KAK) formal berbasis multi-sumber (audio, dokumen pendukung, Blueprint.md, wawancara).
- **Added**: Generator dokumen DOCX otomatis (`.agents/scripts/generate_docx.py`) berstandar resmi Diskominfo Pemkot Yogyakarta (Cover resmi, Kop, Tabel berheader navy, Callout box).
- **Enhanced**: Kebijakan pengujian QA (`05_testing_qa.md` & `template-test-report.md`) dengan 9 kategori **Negative Testing** (Type mismatch misal teks ke integer, boundary violations, malformed payloads, form injection sanitization, RBAC unauthorized access, magic bytes spoofing).
- **Added**: Format dokumen formal DOCX di folder `docs/`: `Dokumen_KAK_Resmi.docx`, `Laporan_Pengujian_QA.docx`, `Dokumen_Laporan_Pentest_Resmi.docx`, `Dokumen_Spesifikasi_API.docx`, dan `Panduan_Pengguna_[App].docx`.
- **Enhanced**: Skill `pembuat-blueprint-profesional` diperkaya dengan pendalaman modul fungsional & alur bisnis, aturan navigasi UI Left Panel Menu (Dashboard/App) vs Top Navbar (Website), serta 4 Modul Pengaturan Sistem standar wajib (User & RBAC, Permission Matrix, UI Color Base & Theme, dan Master Data Terpadu).
- **Added**: Design System dan Pengaturan Sistem Tampilan diperkaya dengan 8 tema terstandarisasi (4 Light + 4 Dark) yang menjamin **Anti-Color Clash** & rasio kontras tinggi (**WCAG AA/AAA Ratio ≥ 4.5:1**), mencegah tumpang tindih warna teks terhadap background (anti-teks putih di atas abu-abu terang / coklat di atas hitam).
- **Refined**: Panduan operasional pada `README.md` disempurnakan dengan menempatkan transisi eksekusi Docker Compose (`docker compose up -d`) secara berurutan tepat setelah pembangunan kode (Langkah 3) sebelum pengujian QA dan Pentest (Langkah 4 & 5).

---

## [1.0.0] - Inisiasi Proyek
### 👤 Pengubah / Author
- **Nama**: Antigravity 2.0 Lead Architect & Developer Team

### 🚀 Perubahan Terintegrasi
- **Added**: Inisialisasi struktur template standar Antigravity 2.0 (Clean Architecture Go + React/Vue).
- **Added**: Konfigurasi SSO JSS Keycloak OIDC (`sso.jogjakota.go.id`) & 4 Role RBAC.
- **Added**: Konfigurasi MinIO Object Storage SDK (Magic Bytes & Presigned URL).
- **Security**: Implementasi guard isolasi login manual hanya untuk sandbox testing.
