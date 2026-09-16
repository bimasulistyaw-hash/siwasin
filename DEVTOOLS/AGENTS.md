# 🌌 ANTIGRAVITY 2.0 - WORKSPACE CONTEXT & CODING OS
> **Standar Resmi Pengembangan Perangkat Lunak - Diskominfo Kota Yogyakarta**

---

## 🎯 PRINSIP UTAMA & SINGLE SOURCE OF TRUTH (SSOT)

1. **Blueprint Sebagai Acuan Utama (`Blueprint.md`) & Penguncian Skema ERD Global**:
   - Setiap pengembangan fitur, penulisan kode, dan pengujian **WAJIB** berpedoman pada `Blueprint.md` (atau `docs/Blueprint.md`) yang dihasilkan dari skill `pembuat-blueprint-profesional`.
   - `Blueprint.md` memuat seluruh penomoran traceability: Kebutuhan Bisnis (`BR-xx`), Fitur Produk (`PRD-xx`), Functional Requirements (`SRS-F-xx`), Non-Functional Requirements (`SRS-NF-xx`), Modul Implementasi Teknis (`MOD-xx`), dan Spesifikasi Layar UI (`UI-xx`).
   - **Quality Gate Penguncian Skema ERD**: Seluruh skema tabel database (termasuk tipe data PostgreSQL, constraints, dan relasi Foreign Key global) **WAJIB tuntas 100% di Blueprint.md Bagian C.4 (ERD)** sebelum implementasi modul pertama (`MOD-01`) mulai dicoding, guna mencegah *migration drift* dan dependensi siklik.
   - **Quality Gate Audit Kelengkapan Fitur & Penelusuran Ulang (100% Completeness Audit)**: Sebelum beralih ke tahap pengujian QA, Developer **WAJIB meneliti ulang (audit rekonsiliasi)** seluruh kebutuhan fungsional (`SRS-F-xx`) dan modul (`MOD-xx`) dari `Blueprint.md` terhadap tabel database, backend handlers, dan antarmuka frontend. Dilarang keras menyisakan fungsi yang tertinggal, kode stub kosong (`// TODO`), atau tombol antarmuka yang belum terhubung ke API backend. Status pelacak `docs/MODULE_PROGRESS.md` wajib terverifikasi tuntas 100%.

2. **Kerangka Acuan Kerja (KAK) Terstandarisasi (`docs/Dokumen_KAK_Resmi.docx`)**:
   - Setiap inisiasi pengadaan / proyek sistem informasi dilengkapi dengan Dokumen KAK formal dari skill `pembuat-kak-profesional`, diekstrak dari rekaman suara, dokumen acuan, DPA, Renstra, dan Blueprint.
   - Dokumen KAK resmi disimpan di `docs/Dokumen_KAK_Resmi.docx` dan `docs/KAK.md`.

3. **Konfirmasi Mode Infrastruktur & Jaminan Konektivitas Layanan Terpadu**:
   - **WAJIB** menanyakan kepada prompter sebelum membuat kode: apakah stack aplikasi dijalankan via **Docker Compose**, **Lokal/Native**, atau **Hybrid**.
   - **WAJIB** menanyakan apakah layanan pendukung benar-benar dibutuhkan: **Redis**, **MinIO**, dan **Keycloak** — ikuti jawaban prompter.
   - **Auto-Wiring & Health Checks (`/api/v1/health`)**: Baik berjalan di Docker maupun Native Lokal, aplikasi yang dibangun **WAJIB terhubung langsung secara otomatis** dengan seluruh layanan pendukung (PostgreSQL 16+, MinIO, Redis, Keycloak SSO, Webserver/Frontend), dilengkapi eksekusi migrasi skema SQL otomatis saat startup, auto-create bucket MinIO, serta verifikasi endpoint diagnostic `/api/v1/health`.
   - Docker Compose direkomendasikan untuk konsistensi lingkungan, tetapi **tidak diwajibkan** jika prompter memilih mode lokal.
   - Database utama **selalu** PostgreSQL 16+ (tidak berubah).

4. **High Concurrency & High Performance**:
   - Backend dibangun dengan **Go (Golang)** menerapkan **Clean Architecture** (Latency < 200ms).
   - Database: **PostgreSQL 16+** dengan connection pooling (`pgxpool`).
   - Caching & Rate Limiting: **Redis 7+** *(opsional — hanya jika dibutuhkan: API publik frekuensi tinggi, session cache, atau job queue. Untuk CRUD sederhana / traffic rendah, Redis dapat dihilangkan)*.
   - Frontend: **React (Vite)** atau **Vue 3 (Vite)** dengan UI **Tailwind CSS** atau **Metronic Bootstrap**.

5. **Otentikasi Terpusat SSO JSS Keycloak & Halaman Login Terpisah 4 Role Dummy**:
   - Seluruh otentikasi produksi wajib menggunakan **OpenID Connect (OIDC)** Keycloak JSS.
   - **Halaman Login Terpisah (`/login`)**: Sistem menyediakan halaman login tersendiri terpisah dari layout aplikasi utama.
   - **4 User Dummy Pengujian (Sandbox)**: Untuk kemudahan pengujian fungsional dan RBAC sandbox (`APP_ENV=testing`), disediakan minimal 4 akun dummy (1 per role):
     1. `Superadmin`: `superadmin@jogjakota.go.id` (Full Access)
     2. `Pengawas`: `pengawas@jogjakota.go.id` (Read-Only & Log Audit)
     3. `Admin`: `admin@jogjakota.go.id` (User & App Settings)
     4. `Operator`: `operator@jogjakota.go.id` (Daily Business Transactions)
     Dilengkapi tombol *1-Click Quick Login* pada halaman login sandbox. Login manual di produksi dilarang keras.

6. **Sentralisasi minimal ada 4 Role RBAC di Keycloak**:
   - **`Superadmin`**: Full Access seluruh modul & konfigurasi sistem (termasuk akses Log Aktivitas Pengguna).
   - **`Pengawas`**: Read-Only setara Superadmin (hanya method `GET`, pemantauan dashboard analitik, dan akses penuh audit **Log Aktivitas Pengguna**; dilarang mutasi data).
   - **`Admin`**: Manajemen User (RBAC mapping) & Pengaturan Aplikasi (dilarang mengakses Log Aktivitas Pengguna).
   - **`Operator`**: Operasional transaksi harian & modul bisnis (dilarang mengakses Log Aktivitas Pengguna).

7. **Direct-to-Real Full-Stack (Tanpa Mockup) & Real Database PostgreSQL Seeding**:
   - **Bebas Kode Buangan (Tanpa Mockup Statis)**: Dilarang keras membuat prototipe/mockup web statis terpisah dengan data dummy in-memory / array palsu di JavaScript. Pengembangan aplikasi **WAJIB langsung membangun aplikasi nyata (Direct-to-Real Full-Stack)**: Backend Go Clean Architecture + Frontend React/Vue (Vite).
   - **Real Database Dummy Data Seeding**: Seluruh data awal dan data dummy pengujian **WAJIB dimasukkan langsung ke dalam real database PostgreSQL** melalui script migrasi/seeder SQL (`db/migrations/`, `db/seeds/`), BUKAN di-hardcode di frontend atau in-memory.
   - **100% Real API Auto-Wiring**: Seluruh antarmuka frontend **WAJIB terhubung langsung secara nyata ke Backend API Go** via HTTP calls (Axios/Fetch) sejak pertama kali dibangun.
   - **Auto-Launch Aplikasi Live & Prompter Review**: Setelah semua modul dan fungsi selesai dibangun serta diaudit kelengkapannya, developer **WAJIB LANGSUNG MENJALANKAN (AUTO-LAUNCH) aplikasi secara otomatis di background task tanpa menunggu instruksi manual prompter**. Segera berikan URL aplikasi live beserta 4 akun dummy sandbox, minta prompter memeriksa fungsionalitas modul per modul, dan tanyakan secara eksplisit apakah ada alur/fungsi yang perlu diperbaiki sebelum lanjut ke QA testing.
   - **Decoupled Storage (MinIO Storage)**: Dilarang keras menyimpan file unggahan di folder lokal server (`/uploads`, `/storage`). Seluruh berkas wajib diunggah ke **MinIO Object Storage** dengan validasi *Magic Bytes* (header biner), nama acak *UUID v4*, dan akses privat via *Presigned URL* (masa aktif 5–15 menit).
   - **Offline-First & Local Assets**: Dilarang menggunakan URL gambar/dummy dari internet. Seluruh aset antarmuka dan seed media disimpan di lokal atau MinIO.

8. **Karakter Desain UI Berstandar Apple Human Interface Guidelines (HIG) & Pola Navigasi**:
   - **Kepatuhan Apple HIG**: Mengacu resmi pada [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) dengan prinsip *Clarity, Deference, dan Depth*, sudut membulat halus (*continuous squircle radius* `rounded-2xl` / 14–20px), dan micro-interactions responsif.
   - **Tipografi San Francisco (SF Pro)**: Font utama menggunakan `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Inter, sans-serif` dengan kerning/letter-spacing proporsional (`tracking-tight` pada heading) dan hierarki bobot tegas (Medium 500 / Semibold 600).
   - **Ruang Kosong (Whitespace) & Layout Longgar**: Antarmuka bersih, lega, tidak sesak dengan sistem grid 8pt (padding `p-6` / `p-8`, gap `gap-6` / `gap-8`) agar fokus pengguna tertuju penuh pada konten.
   - **Efek Transparansi & Vibrancy (Frosted Glass)**: Menambahkan efek blur latar belakang yang halus (`backdrop-filter: blur(20px) saturate(180%)`) pada navbar, sidebar, modal sheet, dan kartu melayang, dipadukan warna transparan (`bg-white/75` atau `bg-slate-900/80`) dan bayangan lembut berlapis.
   - **Pola Navigasi Terstandarisasi**: **Left Panel Menu (Sidebar Navigation)** collapsible untuk backoffice/dashboard operasional; **Top Navigation (Header Navbar)** transparan dengan CTA login untuk portal publik/landing page.
   - **Identitas & Branding Resmi Pemkot Yogyakarta (Wajib di Setiap Aplikasi)**:
     - **Pojok Kiri Atas (Top-Left) & Sidebar**: **WAJIB** menampilkan Logo Resmi Vektor Pemerintah Kota Yogyakarta (`assets/logo-jogja.svg` / `.agents/design-system/assets/logo-jogja.svg`, tinggi 36–44px) dipadukan langsung dengan **Nama Aplikasi** (dan deskripsi/nama OPD terkait) dalam satu kesatuan brand unit yang rapi, tajam, dan responsif (tanpa raster/jpg buram).
     - **Footer Resmi**: **WAJIB** menyertakan footer di bagian bawah antarmuka dengan format teks terstandarisasi:
       `© [Tahun] Pemerintah Kota Yogyakarta` *(misal: `© 2026 Pemerintah Kota Yogyakarta`)*.

9. **5 Modul Pengaturan Sistem (System Settings) + Fitur Wajib Log Aktivitas Pengguna**:
   - **Manajemen Pengguna (User Management)**: Pengelolaan user baru/lama (edit) beserta rolenya. Form input: ID JSS (wajib), Nama Lengkap (terisi otomatis dari sinkronisasi SSO JSS), Role Pengguna (dropdown select role). Menampilkan daftar pengguna dan rolenya dalam bentuk list/tabel responsif dilengkapi tombol Edit dan status.
   - **Manajemen Role (Role Management)**: Menambah, mengubah, dan menghapus role dalam sistem. Aturan bisnis mutlak: **Role yang masih digunakan (memiliki relasi pengguna aktif) DILARANG DIHAPUS**.
   - **Manajemen Hak Akses (Module Permission Matrix)**: Pengaturan dinamis matriks hak akses per role terhadap Menu & Sub-menu yang ada di aplikasi. Menyediakan 4 aksi kontrol standar per modul: **Lihat (View)**, **Tambah (Create)**, **Ubah (Update)**, dan **Hapus (Delete)** dengan switch toggle interaktif per-fitur dan per-kategori grup.
   - **Manajemen Menu Sidebar (Sidebar Navigation Hierarchy)**: Pengelompokan menu (kategori/grup header, e.g. DASHBOARD, MASTER DATA, TRANSAKSI, SYSTEM CONFIG) serta pengaturan hierarki menu utama dan sub-menu, URL route, ikon SVG, badge status, tombol tambah menu/sub-menu, toggle aktif/nonaktif, dan **pengurutan posisi menu WAJIB dilakukan dengan cara menggeser / drag-and-drop (drag-to-reorder), bukan dengan memasukkan nomor urut manual**.
   - **Manajemen Tema dan Warna Tema (Theme & Appearance Management)**: Pengaturan tampilan dengan 8 tema terstandarisasi yang sudah disiapkan (4 Light + 4 Dark Themes, Anti-Color Clash WCAG AA/AAA Ratio ≥ 4.5:1, Apple HIG).
   - **Log Aktivitas Pengguna (User Activity Log / Audit Trail) [WAJIB]**: Setiap blueprint dan aplikasi **WAJIB** menyediakan fitur pemantauan rekam jejak aktivitas (User ID/JSS, Nama, Role, Aksi/Method, Modul/Endpoint, IP Address, Timestamp, Status & Detail). **Aturan Akses RBAC**: Fitur ini **HANYA BISA DIAKSES OLEH ROLE `Superadmin` DAN `Pengawas`** (`Pengawas` bersifat Read-Only). Role `Admin` dan `Operator` diblokir (HTTP 403 Forbidden).

10. **Quality Assurance Komprehensif: Wajib Skenario Pengujian Sebelum Testing, Kepatuhan Eksekusi 100%, Auto-Fix Mandiri, Laporan QA & Dokumen Form UAT Resmi**:
    - **Wajib Penyusunan Skenario Pengujian Terlebih Dahulu (Pre-Execution Test Scenarios)**: Sebelum melakukan eksekusi testing apa pun, Developer/QA **WAJIB menyusun skenario pengujian tertulis secara lengkap** yang mencakup:
      1. **Positive Testing (Happy Path)**: Alur transaksi normal, input valid, transisi state yang benar, dan respons sukses (HTTP 200/201).
      2. **Negative Testing (9 Kategori Matriks Pengujian Negatif)**: Type mismatch (string pada integer), boundary & overflow, malformed JSON, missing mandatory fields, form payload injection (SQLi/XSS), format/regex invalid, otentikasi/RBAC forbidden gate (Pengawas dilarang mutasi, Admin/Operator dilarang akses log audit), konflik data/duplikasi, dan file upload terlarang / spoofing Magic Bytes.
      Setiap skenario wajib mendefinisikan Test Case ID (`TC-POS-xxx`, `TC-NEG-xxx`), fitur terkait (`SRS-F-xx`), prakondisi (*Given*), langkah/payload aksi (*When*), dan hasil yang diharapkan (*Expected Result / Then*).
    - **Kepatuhan Mutlak Eksekusi Terhadap Skenario (Strict Scenario Compliance & 100% Traceability)**:
      - Eksekusi pengujian **WAJIB 100% konsisten berpedoman pada skenario yang telah dibuat**. Dilarang mengubah alur uji, mengurangi beban uji, atau memanipulasi *Expected Result* di tengah jalan demi meluluskan pengujian.
      - Parameter input, method HTTP, dan payload saat pengujian wajib persis mengikuti skenario (*When*), dan assertion respon wajib mencocokkan kriteria ekspektasi (*Then*). Setiap ketidaksesuaian wajib dinyatakan ❌ FAIL.
    - **Eksekusi Pengujian Menyeluruh (Test Execution)**: Memverifikasi konektivitas penuh Frontend $\leftrightarrow$ Backend API $\leftrightarrow$ PostgreSQL Database & MinIO Storage, serta menjalankan automated negative test suite Go (`backend/tests/negative_test.go`).
    - **Self-Healing / Auto-Fix Loop (Maksimal 3 Kali Percobaan)**: Jika ditemukan error atau kegagalan pengujian, Developer **WAJIB langsung memperbaiki sumber masalah pada kode sumber secara otomatis tanpa harus disuruh** hingga maksimal 3 kali percobaan perbaikan.
    - **Eskalasi ke Prompter**: Jika setelah 3x perbaikan masih gagal, tanyakan kepada prompter apakah ingin melanjutkan perbaikan (Ya) atau lewati (Skip). Jika di-skip, lanjutkan pengerjaan dan tetap catat kegagalan sebagai defect di dokumen hasil pengujian QA.
    - **Penuangan Hasil ke Dokumen Laporan Pengujian QA Lengkap Screenshot**: Seluruh hasil pengujian aktual (*Actual Result*), status kelulusan (✅ Pass / ❌ Fail), log kegagalan/defect, dan tangkapan layar bukti visual di `docs/screenshots/` **WAJIB dituangkan secara terstruktur** ke dalam **`docs/TEST_REPORT.md`** dan diterbitkan sebagai dokumen Word resmi **`docs/Laporan_Pengujian_QA.docx`**.
    - **Penyediaan Formulir UAT Resmi Calon Pengguna (`docs/Form_UAT_Resmi.docx`)**: Selain laporan internal teknis QA, sistem **WAJIB menyediakan Formulir UAT Resmi** berformat Word (`docs/Form_UAT_Resmi.docx` & `docs/Form_UAT_Resmi.md`) siap pakai yang memuat lembar verifikasi fitur bisnis, checklist penerimaan pengguna ([ ] Sesuai / [ ] Belum Sesuai), evaluasi usability/kerapian UI, catatan masukan, dan lembar berita acara pengesahan untuk diisi langsung oleh calon pengguna / OPD.

11. **OWASP Top 10 Compliance & Automated Security Audit (Lengkap Bukti Visual Screenshot)**:
    - Menjalankan SAST (`gosec`, `semgrep`), SCA (`govulncheck`, `npm audit`), dan DAST Pentest standar internasional (WSTG, ASVS).
    - **Bukti Visual (Screenshot Evidence Pentest)**: Setiap temuan kerentanan (*PoC*) dan kontrol keamanan positif wajib menyertakan tangkapan layar tampilan pengujian/hasil respon di folder `docs/screenshots/`.
    - Vulnerability gatekeeper memblokir build jika ada temuan Medium/High/Critical. Laporan resmi disimpan di `docs/Dokumen_Laporan_Pentest_Resmi.docx` dan `docs/SECURITY_REPORT.md`.

12. **Wajib Dokumentasi, Swagger UI & Auto-Generate TypeScript Client dari OpenAPI**:
    - Setiap pembuatan API **OTOMATIS** mengonfigurasi Swagger UI pada route `/swagger/index.html` dan menyematkan anotasi `swaggo/swag` di `main.go` serta seluruh HTTP handlers.
    - Artefak spesifikasi OpenAPI `docs/swagger.json`, `docs/swagger.yaml`, dan dokumen developer `docs/Dokumen_Spesifikasi_API.docx` dihasilkan dan disinkronkan secara otomatis.
    - **Auto-Generate TypeScript Client**: Frontend **WAJIB** men-generate interface/types client langsung dari `docs/swagger.json` (via `npx -y openapi-typescript docs/swagger.json -o frontend/src/types/api.ts`) untuk menjamin konsistensi tipe data 100% type-safe antara backend dan frontend.

13. **Standar Seluruh Dokumen Output Berformat DOCX di Folder `docs/`**:
    - Seluruh dokumen deliverable wajib dihasilkan dalam format `.docx` formal siap cetak/distribusi dengan styling resmi Diskominfo Pemkot Yogyakarta menggunakan utilitas `.agents/scripts/generate_docx.py`.

14. **Pembaruan Otomatis & Portabel Task List Monitoring (`docs/Tasklist_monitor.md`)**:
    - Setiap skill (Langkah 1 s.d 5) **WAJIB secara otomatis memperbarui** status `[ ]` menjadi `[x]`, persentase kemajuan, dan status tahapan pada file `docs/Tasklist_monitor.md` setiap kali sebuah sub-tugas diselesaikan.
    - Lokasi file bersifat **relatif terhadap direktori root proyek aktif** (`docs/Tasklist_monitor.md`), sehingga bekerja otomatis di lingkungan sistem operasi atau path folder mana pun tanpa hardcoded absolute path. Jika file belum ada, skill wajib menginisialisasinya secara otomatis.

---

## 🏛️ STRUKTUR DIREKTORI PROYEK STANDAR

```text
├── AGENTS.md                       # Master Context & Instructions (File ini)
├── Blueprint.md                    # Single Source of Truth Kebutuhan Teknis (dari Skill Blueprint)
├── docker-compose.yml              # Standard Orchestration Running Lokal (App + DB + Cache + Storage)
├── .env.example                    # Template Environment Variables Docker
├── .agents/
│   ├── rules/                      # Aturan modular Antigravity 2.0
│   │   ├── 01_architecture_clean.md# Arsitektur, Docker, PostgreSQL, & Concurrency
│   │   ├── 02_sso_keycloak_rbac.md # SSO Keycloak, 4 Role RBAC & 4 Dummy Users
│   │   ├── 03_minio_storage.md     # MinIO Object Storage
│   │   ├── 04_security_owasp.md    # Security & OWASP Top 10
│   │   └── 05_testing_qa.md        # QA & Testing Policy (Positive & Negative Testing)
│   ├── scripts/
│   │   ├── generate_docx.py        # Utility Generator DOCX Resmi Pemkot Yogyakarta
│   │   └── capture_screenshots.py  # Utility Pre-Flight & Screenshot Visual Capture CLI
│   └── skills/
│       ├── developer-aplikasi-profesional/  # Skill Developer (Infra, Real DB Seed, Direct-to-Real Full App, Audit Kelengkapan, QA)
│       ├── pembuat-kak-profesional/         # Skill Penyusunan KAK Formal (Audio/Doc/Blueprint)
│       ├── pembuat-blueprint-profesional/   # Skill Wawancara BRD+PRD+SRS
│       ├── pembuat-user-manual-profesional/ # Skill Penyusunan User Manual Resmi DOCX + Screenshots
│       └── security-pentester-profesional/  # Skill Pentest & Security Audit Internasional
├── backend/                        # Go (Golang) Backend Service (Clean Architecture)
│   ├── Dockerfile                  # Multi-stage Dockerfile Backend Go
│   ├── cmd/api/main.go             # Entrypoint backend
│   ├── internal/
│   │   ├── config/                 # Konfigurasi Env, Keycloak, MinIO, DB, Redis
│   │   ├── delivery/http/          # HTTP Handlers, Routers, DTOs
│   │   ├── domain/                 # Entity models, Repository & Usecase Interfaces
│   │   ├── repository/             # Data Access (PostgreSQL & Redis)
│   │   ├── usecase/                # Business Logic (User, Auth, MinIO Upload, Settings)
│   │   └── middleware/             # Keycloak JWT, RBAC Gate, Rate Limiter, CORS
│   ├── pkg/                        # Utility: Logger (Zap), MinIO Client, SSO Keycloak Client
│   ├── db/migrations/              # Database Migration SQL
│   ├── db/seeds/                   # Real PostgreSQL Dummy Data Seeds
│   ├── tests/                      # Unit & Integration Testing (min. 85% coverage, Positive & Negative)
│   ├── Makefile                    # Standardized Operational Commands
│   └── go.mod
├── frontend/                       # React / Vue Frontend Service
│   ├── Dockerfile                  # Dockerfile Frontend Client
│   ├── src/
│   │   ├── assets/                 # Icons, Images, Styles
│   │   ├── components/             # Reusable UI (Apple HIG Design System, Drag-to-Reorder Sidebar)
│   │   ├── pages/                  # Views (Login Terpisah, Dashboard, User Management, Modul Bisnis)
│   │   ├── services/               # API Callers (Axios with Keycloak Bearer Token)
│   │   ├── store/                  # Auth & App State (Zustand / Pinia)
│   │   └── utils/                  # Keycloak Adapter & Helper Functions
│   ├── public/
│   └── package.json
├── docs/                           # Dokumentasi Resmi & Deliverables Lengkap
│   ├── Tasklist_monitor.md         # Master Checklist Monitoring 5 Tahapan Kerja (Prompter & Developer)
│   ├── Dokumen_KAK_Resmi.docx      # [DOCX 1] Dokumen Kerangka Acuan Kerja (KAK) Resmi
│   ├── KAK.md                      # Dokumen KAK versi Markdown
│   ├── Dokumen_Blueprint_Resmi.docx# Dokumen Formal Kesepakatan Scope & Arsitektur
│   ├── INTERVIEW_LOG.md            # Catatan Transkrip Wawancara (Tanya-Jawab) & Evaluasi
│   ├── MODULE_PROGRESS.md          # Pelacak Status & Progres Pembangunan Per-Modul (Quality Gate)
│   ├── Laporan_Pengujian_QA.docx   # [DOCX 2] Laporan Pengujian QA (Fungsional & Negative Testing + Screenshot)
│   ├── TEST_REPORT.md              # Laporan Pengujian Fungsional & Teknis (Markdown + Screenshot)
│   ├── Form_UAT_Resmi.docx         # [DOCX 3] Formulir Uji Terima Pengguna (User Acceptance Testing - UAT) Resmi
│   ├── Form_UAT_Resmi.md           # Formulir UAT versi Markdown
│   ├── Dokumen_Laporan_Pentest_Resmi.docx # [DOCX 4] Laporan Resmi Audit Keamanan Pentest (Lengkap Screenshot)
│   ├── SECURITY_REPORT.md          # Laporan Teknis Pentest OWASP (Markdown + Screenshot)
│   ├── WSTG_AUDIT_CHECKLIST.md     # Lembar Kerja Checklist Audit Keamanan WSTG/ASVS
│   ├── Dokumen_Spesifikasi_API.docx# [DOCX 5] Spesifikasi API untuk Developer Eksternal / Mitra
│   ├── swagger.json                # Spesifikasi OpenAPI/Swagger format JSON
│   ├── swagger.yaml                # Spesifikasi OpenAPI/Swagger format YAML
│   ├── Panduan_Penggunaan_Aplikasi.docx # [DOCX 6] Panduan Penggunaan / User Manual Resmi (Lengkap Screenshot)
│   ├── USER_MANUAL.md              # Panduan Pengguna versi Markdown (Lengkap Screenshot)
│   ├── CHANGELOG.md                # Log Perubahan Aplikasi
│   └── screenshots/                # Aset Screenshot Tampilan Aplikasi & Bukti Pengujian
└── README.md
```

---

## 👥 ORKESTRASI PERAN SUB-AGEN

| Peran Sub-Agen | Tanggung Jawab Utama | Batasan & Kontrol |
| :--- | :--- | :--- |
| **Lead Architect Agent** | Memvalidasi model domain, Clean Architecture, Docker Compose, dan memastikan `Blueprint.md` terpenuhi. | Menolak penggabungan jika logika bisnis bocor ke handler, tanpa kontainerisasi Docker, atau ada upload lokal. |
| **KAK Specialist Agent** | Menyusun Kerangka Acuan Kerja formal (`pembuat-kak-profesional`) dari rekaman audio, dokumen Renstra/DPA, dan Blueprint. Menghasilkan `docs/Dokumen_KAK_Resmi.docx`. | Wajib mencantumkan pagu/HPS, kualifikasi 7 tenaga ahli, jadwal milestone, dan lembar pengesahan PPK. |
| **Developer Agent (Go + React/Vue + QA)** | Membangun RESTful API Go & Frontend, Real PostgreSQL Data Seeding, Halaman Login Terpisah (4 Dummy Users), Sidebar Drag-and-Drop Reorder, Swagger UI, **Auto-Launch Aplikasi Live segera setelah modul lengkap dibangun tanpa menunggu prompter**, **Mengundang Prompter mereview aplikasi modul per modul**, **Penyusunan Skenario Pengujian (Positif & Negatif) sebelum testing**, **Kepatuhan Eksekusi 100% terhadap Skenario**, E2E Testing FE-API-DB, **Auto-Fix Mandiri saat ada bug/failure**, menuangkan hasil uji ke `docs/Laporan_Pengujian_QA.docx` & `docs/TEST_REPORT.md` + Screenshots, serta **menyediakan Formulir UAT Resmi (`docs/Form_UAT_Resmi.docx`)**. | Wajib parameterized queries, validasi DTO, coverage minimal 85%, real DB seeds, auto-launch live stack, perancangan skenario pengujian komprehensif, kepatuhan eksekusi skenario mutlak, dan penanganan auto-fix mandiri. |
| **Documentation Agent** | Menyusun User Manual & Panduan Penggunaan Aplikasi resmi (`pembuat-user-manual-profesional`) berstandar ISO/IEC/IEEE 26514, disertai screenshot nyata per prosedur aplikasi yang sedang diterangkan cara penggunaannya. Menghasilkan `docs/Panduan_Penggunaan_Aplikasi.docx` & `docs/USER_MANUAL.md`. | Wajib menyertakan screenshot ber-caption dari `docs/screenshots/` dan instruksi langkah bernomor. |
| **Security Agent (Pentester)** | Audit SAST (`gosec`, `semgrep`), SCA (`govulncheck`, `npm audit`), DAST & Pentest mengacu standar internasional (OWASP Top 10, OWASP API Top 10, WSTG v4.2, ASVS v4.0, NIST SP 800-115, PTES, OSSTMM 3, CIS Controls, CVSS v3.1/v4.0). | **Security Gatekeeper**: Blokir build jika ada temuan Medium/High/Critical. Wajib menyusun seluruh output laporan pengujian di folder `docs/` (`docs/SECURITY_REPORT.md`, `docs/Dokumen_Laporan_Pentest_Resmi.docx`, `docs/WSTG_AUDIT_CHECKLIST.md`) lengkap dengan screenshot bukti pengujian/PoC dari `docs/screenshots/`. |
