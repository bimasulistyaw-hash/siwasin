<!-- Dibuat oleh Bidang Sistem Informasi dan Statistik Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta -->
# Template BLUEPRINT — [Nama Produk/Sistem]
> Dokumen gabungan **BRD + PRD + SRS** — referensi spesifikasi tunggal untuk vibe engineering / agentic coding.
> Standar: BRD → BABOK v3 (IIBA) · SRS → ISO/IEC/IEEE 29148:2018 · NFR → ISO/IEC 25010 · Prioritas → MoSCoW (DSDM) · Acceptance → Gherkin · Diagram → Mermaid.js.

---

## 1. Informasi Dokumen

| Field | Nilai |
|---|---|
| Judul | Blueprint — [Nama Produk/Sistem] |
| Kode Dokumen | BLUEPRINT-[PROYEK]-[VERSI] |
| Versi | 1.0 |
| Tanggal | YYYY-MM-DD |
| Status | DRAFT / DITINJAU / DISETUJUI |
| Pemilik | [Nama] |
| Author | [Nama] |
| Reviewer | [Nama] |
| Approver | [Nama] |
| Mode SRS | Full Teknis / Konseptual |
| Tools Target | Google Antigravity 2.0 / agentic coding |

### Riwayat Revisi

| Versi | Tanggal | Deskripsi Perubahan | Penulis |
|---|---|---|---|
| 0.1 | | Draf awal | |
| 1.0 | | Disetujui | |

---

## 2. Ringkasan Eksekutif

[1 paragraf: masalah yang dipecahkan, solusi yang dibangun, pengguna utama, nilai bisnis, ukuran sukses, timeline]

---

# BAGIAN A — BRD (Business Requirements Document)

## A.1. Latar Belakang & Konteks Bisnis

- **A.1.1. Kondisi bisnis saat ini (as-is)**: [deskripsi kondisi sekarang]
- **A.1.2. Pemicu perubahan**: [event/masalah yang mendorong proyek ini]
- **A.1.3. Kaitan dengan strategi organisasi**: [kebijakan/program yang relevan]

## A.2. Pernyataan Masalah & Peluang

- **A.2.1. Problem statement**: *"Saat ini [siapa] tidak dapat [apa] karena [alasan], berdampak [dampak terukur]."*
- **A.2.2. Peluang / value proposition**: [solusi yang ditawarkan dan nilainya]
- **A.2.3. Dampak bila tidak ditangani**: [risiko jika sistem tidak dibangun]

## A.3. Tujuan Bisnis & KPI (SMART)

| ID | Tujuan | Metrik (KPI) | Baseline | Target | Periode Ukur |
|---|---|---|---|---|---|
| TUJ-01 | | | | | |
| TUJ-02 | | | | | |

## A.4. Ruang Lingkup

- **A.4.1. In-Scope**: [daftar eksplisit apa yang masuk lingkup]
- **A.4.2. Out-of-Scope**: [daftar eksplisit apa yang tidak masuk, beserta alasan — ini bagian kontraktual kritis]
- **A.4.3. Batasan lingkup**: [regulasi, anggaran, waktu, kebijakan]

## A.5. Stakeholder & RACI

| Stakeholder | Peran | Kepentingan | Pengaruh | R | A | C | I |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## A.6. Kebutuhan Bisnis (Business Requirements)

| ID | Kebutuhan Bisnis | Prioritas (MoSCoW) | Sumber | Status |
|---|---|---|---|---|
| BR-01 | | Must / Should / Could / Won't | [Jawaban]/[Dok: x]/[Audio: x] | |
| BR-02 | | | | |

## A.7. Proses Bisnis: As-Is

```mermaid
flowchart TD
    title[Proses Bisnis As-Is — Nama Proses]
    A([Mulai]) --> B[Langkah 1]
    B --> C{Kondisi?}
    C -- Ya --> D[Langkah 2a]
    C -- Tidak --> E[Langkah 2b]
    D --> F([Selesai])
    E --> F
```

## A.8. Proses Bisnis: To-Be

```mermaid
flowchart TD
    title[Proses Bisnis To-Be — Nama Proses]
    A([Mulai]) --> B[Langkah Baru 1]
    B --> C{Validasi Sistem}
    C -- Sukses --> D[Langkah Baru 2]
    C -- Gagal --> E[Notifikasi Error]
    D --> F([Selesai])
    E --> B
```

## A.9. Analisis Kesenjangan (Gap Analysis)

| Proses | Kondisi As-Is | Kondisi To-Be | Gap | Aksi |
|---|---|---|---|---|
| | | | | |

## A.10. Risiko & Mitigasi

| ID | Risiko | Probabilitas | Dampak | Strategi Mitigasi | Pemilik |
|---|---|---|---|---|---|
| R-01 | | Tinggi/Sedang/Rendah | Tinggi/Sedang/Rendah | | |

---

# BAGIAN B — PRD (Product Requirements Document)

## B.1. Visi Produk

[1–2 kalimat: apa yang dibangun, untuk siapa, kenapa sekarang, ukuran sukses]

## B.2. Konteks & Masalah

- **B.2.1. Masalah pengguna yang dipecahkan**: [deskripsi konkret dari sudut pandang pengguna]
- **B.2.2. Bukti masalah**: [data, riset, keluhan yang mendukung]
- **B.2.3. Kaitan dengan BR-xx**: [BR yang mana yang dijawab oleh produk ini]

## B.3. Target Pasar & Kompetitif (ringkas)

- **Segmen pengguna utama**: [deskripsi]
- **Diferensiasi**: [apa yang membedakan sistem ini dari solusi sebelumnya]

## B.4. Persona Pengguna

| ID | Nama Persona | Peran/Jabatan | Tujuan Utama | Pain Points | JTBD | Success Metrics | Konteks Pakai |
|---|---|---|---|---|---|---|---|
| P-01 | | | | | *"Ketika..., saya ingin..., sehingga..."* | | Device, jam, frekuensi |
| P-02 | | | | | | | |

## B.5. User Stories

| ID | User Story | Persona | Prioritas | Status |
|---|---|---|---|---|
| US-01 | Sebagai [persona], saya ingin [aksi], sehingga [manfaat] | P-01 | Must | |
| US-02 | | | | |

## B.6. User Journey Map — [Nama Persona / Alur Kritis]

```mermaid
flowchart LR
    title[User Journey — Nama Persona: Nama Alur]

    subgraph Discovery
        A([Pengguna menyadari kebutuhan]) --> B[Membuka aplikasi]
    end

    subgraph Onboarding
        B --> C[Login via SSO Keycloak]
        C --> D{Autentikasi berhasil?}
        D -- Ya --> E[Masuk Dashboard]
        D -- Tidak --> F[Tampil pesan error]
        F --> C
    end

    subgraph Core Usage
        E --> G[Memilih fitur utama]
        G --> H[Mengisi form / melakukan aksi]
        H --> I{Validasi data}
        I -- Valid --> J[Proses disimpan]
        I -- Tidak Valid --> K[Tampil pesan validasi]
        K --> H
    end

    subgraph Completion
        J --> L[Konfirmasi sukses]
        L --> M([Selesai])
    end

    style Discovery fill:#e8f5e9
    style Onboarding fill:#e3f2fd
    style "Core Usage" fill:#fff3e0
    style Completion fill:#f3e5f5
```

## B.7. Lingkup Produk

- **B.7.1. In-Scope**:
- **B.7.2. Out-of-Scope**:
- **B.7.3. MVP definition**: [fitur minimal yang harus ada untuk rilis pertama]

## B.8. Standar Pola Navigasi Utama UI

- **Model Navigasi Terpilih**: [Left Panel Menu (Sidebar) / Top Navigation (Header Navbar)]
- **Ketentuan Baku**:
  - **Aplikasi Web / Sistem Informasi Operasional / Dashboard Backoffice**: **WAJIB** menggunakan **Left Panel Menu (Sidebar)** sebagai navigasi utamanya. Dilengkapi sidebar collapsible, struktur menu hierarkis, badge counter notifikasi, active indicator, serta user card di area sidebar.
  - **Website Publik / Portal Informasi / Landing Page**: Menggunakan **Top Navigation (Header Navbar)** dengan link menu horizontal, search input, switch bahasa/tema, dan CTA login/akses di kanan atas (dengan mobile hamburger drawer).

---

## B.9. Modul & Fitur Fungsional Utama

### B.9.1. Daftar Modul & Fitur

| ID | Nama Modul / Fitur | Deskripsi Fungsional | Prioritas (MoSCoW) | Tautan BR | Status |
|---|---|---|---|---|---|
| PRD-01 | [Modul Bisnis 1] | [Uraian fungsi dan alur transaksi bisnis utama] | Must | BR-01 | Aktif |
| PRD-02 | [Modul Bisnis 2] | [Uraian fungsionalitas pendukung/transaksi] | Must / Should | BR-02 | Aktif |
| PRD-SET-01 | Pengaturan Manajemen User (CRUD) & Role (RBAC) | Pengelolaan akun pengguna, mapping 4 role Keycloak & RBAC lokal | Must | BR-xx | Wajib |
| PRD-SET-02 | Pengaturan Hak Akses Modul (Permission Matrix) | Pengaturan dinamis modul apa saja yang dapat diakses oleh setiap role | Must | BR-xx | Wajib |
| PRD-SET-03 | Pengaturan Tampilan & Tema UI (Color Base & Dark/Light) | Pilihan warna tema dasar, toggle Dark/Light mode, layout density | Must | BR-xx | Wajib |
| PRD-SET-04 | Pengaturan Master Data Terpadu | Manajemen data referensi induk yang digunakan modul bisnis | Must | BR-xx | Wajib |

### B.9.2. Feature Decomposition Tree

```mermaid
flowchart TD
    title[Feature Decomposition — Nama Sistem]

    Root([Sistem: Nama Produk]) --> M1[PRD-01: Modul Bisnis Utama]
    Root --> M2[PRD-02: Modul Bisnis Pendukung]
    Root --> MSET[Modul Wajib: Pengaturan Sistem]

    M1 --> M1a[Sub-modul: Daftar & Filter Data]
    M1 --> M1b[Sub-modul: Form Tambah/Ubah]
    M1 --> M1c[Sub-modul: Detail & Riwayat]

    M2 --> M2a[Sub-modul: Operasional Transaksi]
    M2 --> M2b[Sub-modul: Ekspor Laporan]

    MSET --> S1[PRD-SET-01: User & RBAC Management]
    MSET --> S2[PRD-SET-02: Module Permission Matrix]
    MSET --> S3[PRD-SET-03: UI Theme & Color Base Setting]
    MSET --> S4[PRD-SET-04: Integrated Master Data Management]

    style Root fill:#1E3A8A,color:#fff
    style M1 fill:#0D9488,color:#fff
    style M2 fill:#0D9488,color:#fff
    style MSET fill:#334155,color:#fff
```

---

### B.9.3. Detail Pendalaman Modul Bisnis

#### Modul: [PRD-01 — Nama Modul Bisnis]

1. **Tujuan & Fungsi Modul**:
   [Deskripsi mendalam mengenai tujuan operasional modul, problem yang diselesaikan, dan entitas yang dikelola.]

2. **Dekomposisi Sub-Fitur & Aksi Operasional**:
   - **Tabel & Filter Data**: Menampilkan daftar entitas dengan sorting, pencarian multi-kolom, filter status, dan paginasi (10/25/50/100 baris).
   - **Tambah & Ubah Data**: Form input dengan validasi interaktif, preview dokumen, dan auto-calculate.
   - **Detail & Audit Log**: Riwayat perubahan data (*audit trail*), status approval, dan log aktivitas pengguna.
   - **Ekspor & Cetak**: Ekspor data ke format XLSX, PDF, dan CSV.

3. **Alur Bisnis Modul (Proses Flowchart)**:

```mermaid
flowchart TD
    title[Alur Proses Bisnis — Modul PRD-01]

    Start([Mulai]) --> OpenList[Buka Menu Modul di Left Sidebar]
    OpenList --> CheckPerm{Cek Hak Akses Role}
    CheckPerm -- Tidak Diizinkan --> Deny[Tampilkan 403 / Menu Disembunyikan]
    CheckPerm -- Diizinkan --> ShowTable[Tampilkan Data Table & Filter Bar]
    ShowTable --> ActionChoice{Pilih Aksi Pengguna}
    
    ActionChoice -- Tambah Data --> FormInput[Buka Form Tambah Data]
    FormInput --> ValidateInput{Validasi Input}
    ValidateInput -- Tidak Valid / Type Mismatch --> ShowErr[Tampilkan Pesan Validasi Inline]
    ShowErr --> FormInput
    ValidateInput -- Valid --> SaveDB[(Simpan ke PostgreSQL & MinIO)]
    SaveDB --> SuccessToast[Tampilkan Notifikasi Sukses]
    SuccessToast --> ShowTable

    ActionChoice -- Edit / Hapus --> Mutate[Proses Mutasi Data]
    Mutate --> CheckPengawas{Apakah Role Pengawas?}
    CheckPengawas -- Ya --> BlockPengawas[Tolak Mutasi: 403 Forbidden]
    CheckPengawas -- Tidak --> ExecMutate[Eksekusi Mutasi & Catat Audit Log]
    ExecMutate --> ShowTable
```

4. **Spesifikasi Data Input (Form & Parameter Validasi)**:
   | Nama Field | Label UI | Tipe Data | Constraint / Validasi | Komponen Input |
   | :--- | :--- | :--- | :--- | :--- |
   | `id` | ID Data | UUID v4 | Primary Key, Auto-generated | Hidden |
   | `nama` | Nama Lengkap / Judul | VARCHAR(150) | Wajib, min 3 char, max 150 char | Text Input |
   | `kategori_id` | Kategori | INTEGER | Wajib, foreign key valid | Searchable Select Dropdown |
   | `tanggal` | Tanggal Transaksi | DATE | Wajib, format YYYY-MM-DD | Datepicker |
   | `lampiran` | Berkas Lampiran | BINARY / UUID | Opsional, max 5MB, PDF/JPG/PNG | MinIO File Uploader |

5. **Spesifikasi Tampilan & Feedback Visual**:
   - Layout utama menggunakan container ber-padding 24px dengan header title dan breadcrumb.
   - Status badge dengan warna semantik: `Draft` (Abu-abu), `Menunggu` (Kuning/Amber), `Disetujui` (Hijau/Emerald), `Ditolak` (Merah/Rose).
   - Dialog konfirmasi modal wajib muncul sebelum aksi mutasi destruktif (Hapus/Tolak).

6. **Acceptance Criteria (Gherkin)**:
```gherkin
Scenario: Happy Path — Tambah data baru berhasil
  Given Pengguna terautentikasi dengan role "Operator" atau "Admin"
  When Pengguna mengisi seluruh field wajib dengan format valid dan klik "Simpan"
  Then Data berhasil tersimpan di database dan tampil di baris teratas data table
  And Muncul notifikasi toast "Data berhasil disimpan"

Scenario: Negative Path — Validasi type mismatch string pada field numerik
  Given Pengguna membuka form transaksi
  When Pengguna memasukkan teks karakter pada field integer ID/jumlah
  Then Sistem menampilkan pesan error "Field harus berupa angka valid"
  And Data tidak dikirimkan ke backend sebelum diperbaiki

Scenario: RBAC Path — Role Pengawas diblokir dari mutasi data
  Given Pengguna terautentikasi dengan role "Pengawas"
  When Pengguna mengakses halaman modul
  Then Seluruh tombol "Tambah", "Edit", dan "Hapus" disembunyikan/dinonaktifkan
  And Jika request API dikirim secara langsung, server mengembalikan status HTTP 403 Forbidden
```

---

## B.10. ⚙️ 5 Modul Wajib Pengaturan Sistem (Mandatory System Settings)

Setiap aplikasi dalam blueprint ini dilengkapi 5 modul pengaturan sistem berikut:

### B.10.1. PRD-SET-01: Manajemen Pengguna (User Management)
- **Tujuan**: Mengelola data pengguna (baru maupun lama/edit) serta penetapan rolenya secara terpusat dan sinkron dengan Keycloak SSO JSS.
- **Fungsionalitas**:
  - **Form Tambah / Edit Pengguna**:
    - `ID JSS *`: Input text (Wajib diisi sebagai identitas unik).
    - `Nama Lengkap`: Input text (Terisi otomatis / read-only saat ID JSS diverifikasi via SSO JSS).
    - `Role Pengguna *`: Dropdown selection (Wajib memilih salah satu role aktif).
    - Tombol `Batal` & `Simpan`.
  - **Daftar Pengguna**: Menampilkan tabel/list data pengguna (Avatar, ID JSS, Nama Lengkap, Role Badge, Status Akun) dilengkapi tombol `Edit` dan aksi kelola status.

### B.10.2. PRD-SET-02: Manajemen Role (Role Management)
- **Tujuan**: Mengelola daftar peran (*roles*) dalam sistem sesuai struktur wewenang operasional.
- **Fungsionalitas**:
  - CRUD Role: Menambah role baru, mengubah nama dan deskripsi peran, serta menghapus role.
  - **Aturan Bisnis Integritas**: Role yang masih digunakan / terikat pada pengguna aktif **DILARANG DIHAPUS** (*Protected Role Deletion*).

### B.10.3. PRD-SET-03: Manajemen Hak Akses (Module Permission Matrix)
- **Tujuan**: Mengatur hak akses dinamis per-role terhadap setiap Menu dan Sub-menu yang ada di dalam aplikasi.
- **Fungsionalitas**:
  - **Matriks Izin Berjenjang**: Dropdown pemilihan Role target di bagian atas, tombol `Simpan Perubahan`.
  - **4 Aksi Kontrol Standar**: Kolom **Lihat (View)**, **Tambah (Create)**, **Ubah (Update)**, dan **Hapus (Delete)**.
  - **Switch Toggle Interaktif**: Kontrol toggle switch per-aksi pada setiap baris sub-menu, dilengkapi master switch toggle per-kategori grup menu.

### B.10.4. PRD-SET-04: Manajemen Menu Sidebar (Sidebar Navigation Management)
- **Tujuan**: Mengelola pengelompokan menu kategori dan mengatur hierarki menu utama hingga sub-menu navigasi sidebar.
- **Fungsionalitas**:
  - **Pengelompokan Kategori / Header**: Pengelompokan section menu (misal: `DASHBOARD`, `MASTER DATA`, `TRANSAKSI`, `SYSTEM CONFIG`, `DEBUG`).
  - **Hierarki Menu & Sub-Menu**: Penataan struktur menu bertingkat, rute URL, ikon visual SVG, badge notifikasi/status, tombol `Tambah Menu`, `Tambah Sub-Menu`, `Edit`, `Hapus`, serta toggle aktif/nonaktif.
  - **Pengurutan Menu Interaktif (Drag-and-Drop Reorder)**: Pengurutan posisi menu **wajib dilakukan dengan cara menggeser / drag-and-drop (drag-to-reorder)** menggunakan drag handle, BUKAN dengan memasukkan nomor urut menu secara manual.

### B.10.5. PRD-SET-05: Manajemen Tema dan Warna Tema (Theme & Appearance Management)
- **Tujuan**: Mengatur tema visual aplikasi dengan jaminan keterbacaan tinggi berstandar Apple HIG dan bebas tumpang tindih warna (*Anti-Color Clash*).
- **8 Tema Terstandarisasi (WCAG AA/AAA Ratio ≥ 4.5:1)**:
  - *Light 1*: `light-yogyakarta` (Classic Navy `#1E3A8A`) — Default Light.
  - *Light 2*: `light-emerald` (Layanan Publik Teal `#0D9488`).
  - *Light 3*: `light-royal` (Inovasi Digital `#2563EB`).
  - *Light 4*: `light-amber` (Kraton Heritage Gold `#B45309`).
  - *Dark 1*: `dark-midnight` (Midnight Slate `#0B0F19`) — Default Dark.
  - *Dark 2*: `dark-emerald` (Deep Forest Emerald `#022C22`).
  - *Dark 3*: `dark-obsidian` (Obsidian Pitch Black `#000000`).
  - *Dark 4*: `dark-heritage` (Kraton Night Heritage `#1C1917`).
- **Fitur Tampilan**: Live preview color palette, mode switcher (Light / Dark / Auto System), dan persistensi penyimpanan preferensi lokal.

### B.10.6. PRD-SET-06: Log Aktivitas Pengguna (User Activity Log / Audit Trail) [Wajib]
- **Tujuan**: Merekam secara kronologis seluruh jejak audit interaksi dan transaksi pengguna untuk akuntabilitas, keamanan, dan audit investigasi.
- **Fungsionalitas**:
  - **Perekaman Otomatis**: User ID/JSS, Nama Pengguna, Role, HTTP Method, Modul/Endpoint, IP Address, User Agent, Status Respon, Detail/Payload Perubahan, dan Timestamp.
  - **Tabel Log Interaktif**: Pencarian multi-parameter, filter tanggal/role/status, dan penampil detail payload perubahan (*before-after JSON diff*).
  - **Batasan Akses RBAC Eksklusif**:
    - **`Superadmin`**: Akses Penuh (View, Filter, Export Laporan Audit CSV/XLSX).
    - **`Pengawas`**: Hak Akses **Read-Only** (Hanya melihat dan mengekspor laporan pemantauan; tidak dapat memanipulasi data log).
    - **`Admin` & `Operator`**: **DIBLOKIR TOTAL** (Menu tidak dirender dan akses API mengembalikan `HTTP 403 Forbidden`).

---

# BAGIAN C — SRS (Software Requirements Specification)

> **Mode SRS**: [Full Teknis / Konseptual] *(dipilih di awal fase wawancara)*

## C.1. Ruang Lingkup Teknis

- **Perspektif produk**: [posisi sistem dalam ekosistem yang lebih besar]
- **Kelas pengguna & privileges**: [peran dan hak akses masing-masing]
- **Lingkungan operasi**: OS, browser, device, bandwidth minimum
- **Batasan desain**: [constraint teknologi yang tidak bisa diganggu gugat]
- **Asumsi & dependensi**: [hal-hal yang diasumsikan benar saat dokumen ini ditulis]

## C.2. Arsitektur Sistem

### C.2.1. System Context (C4 Level 1)

```mermaid
flowchart TB
    title[System Architecture — Nama Sistem]

    subgraph Actors["👤 Aktor Eksternal"]
        U1[Pengguna / User]
        U2[Admin Sistem]
    end

    subgraph System["🖥️ Sistem yang Dibangun"]
        FE["Frontend\n(React/Vue + Vite)"]
        BE["Backend API\n(Go - Clean Architecture)"]
    end

    subgraph Infrastructure["🏗️ Infrastruktur"]
        DB[(PostgreSQL 16+)]
        RD[(Redis 7+)]
        MN[(MinIO Object Storage)]
    end

    subgraph External["🔗 Sistem Eksternal"]
        KC[Keycloak SSO\nsso.jogjakota.go.id]
        EXT[Sistem Eksternal Lain]
    end

    U1 -->|HTTPS| FE
    U2 -->|HTTPS| FE
    FE -->|REST API / Bearer Token| BE
    BE -->|pgxpool| DB
    BE -->|redis client| RD
    BE -->|MinIO SDK| MN
    BE -->|OIDC / JWT Verify| KC
    BE -->|HTTP/gRPC| EXT

    style System fill:#1565C0,color:#fff
    style Infrastructure fill:#2E7D32,color:#fff
    style External fill:#E65100,color:#fff
```

### C.2.2. Deployment Architecture (Docker Compose)

```mermaid
flowchart TB
    title[Deployment Architecture — Docker Compose]

    subgraph DockerNetwork["Docker Network: app-network"]
        subgraph AppServices["Application Services"]
            FE_C["frontend\n:3000"]
            BE_C["backend\n:8080"]
        end

        subgraph DataServices["Data Services"]
            DB_C["postgres:16\n:5432\nvol: pg_data"]
            RD_C["redis:7-alpine\n:6379\nvol: redis_data"]
            MN_C["minio\n:9000 (API)\n:9001 (Console)\nvol: minio_data"]
        end
    end

    subgraph ExternalDep["Dependensi Eksternal"]
        KC_EXT["Keycloak SSO\nsso.jogjakota.go.id"]
    end

    FE_C -->|proxy /api| BE_C
    BE_C --> DB_C
    BE_C --> RD_C
    BE_C --> MN_C
    BE_C -->|OIDC| KC_EXT

    style AppServices fill:#1565C0,color:#fff
    style DataServices fill:#2E7D32,color:#fff
```

## C.3. Persyaratan Fungsional (SRS-F-xx)

| ID | Deskripsi (pernyataan tunggal, testable) | Precondition | Input | Output/Perilaku | HTTP Method | Endpoint | Prioritas | Traceability (PRD-xx) |
|---|---|---|---|---|---|---|---|---|
| SRS-F-01 | | | | | | | | |
| SRS-F-02 | | | | | | | | |

### C.3.x. Detail SRS-F-xx — [Nama Requirement]

**Deskripsi**: [pernyataan tunggal, testable]
**Precondition**: [kondisi sistem sebelum requirement ini aktif]
**HTTP**: `[METHOD] /api/v1/[endpoint]`
**Request Body**:
```json
{
  "field_name": "string (required, max:255)",
  "field_number": 0
}
```
**Response 200 OK**:
```json
{
  "status": "success",
  "data": {},
  "message": "Keterangan sukses"
}
```
**Response Error**:
```json
{
  "code": "ERR_CODE",
  "message": "Pesan error untuk user",
  "details": [{"field": "field_name", "issue": "required"}],
  "trace_id": "uuid"
}
```
**HTTP Status Codes**: 200 OK · 400 Bad Request · 401 Unauthorized · 403 Forbidden · 404 Not Found · 422 Unprocessable Entity · 500 Internal Server Error

### Sequence Diagram: [Nama Alur — Contoh: Login SSO]

```mermaid
sequenceDiagram
    title Login Flow via Keycloak SSO

    actor User as 👤 User
    participant FE as Frontend (React/Vue)
    participant BE as Backend API (Go)
    participant KC as Keycloak SSO
    participant DB as PostgreSQL
    participant RD as Redis

    User->>FE: Klik tombol Login
    FE->>KC: Redirect ke Authorization Endpoint (OIDC)
    KC-->>User: Tampilkan form login SSO

    User->>KC: Submit credentials
    KC-->>KC: Validasi kredensial

    alt Autentikasi Gagal
        KC-->>FE: Redirect dengan error parameter
        FE-->>User: Tampilkan pesan "Login gagal"
    else Autentikasi Berhasil
        KC-->>FE: Redirect dengan authorization_code
        FE->>BE: POST /api/v1/auth/callback {code, state}
        BE->>KC: POST /token — tukar code → access_token + id_token
        KC-->>BE: {access_token, id_token, refresh_token}
        BE->>BE: Verifikasi & decode JWT (claims: sub, roles)
        BE->>DB: Upsert user (sync dari claims Keycloak)
        DB-->>BE: User record
        BE->>RD: SET session:{user_id} → {token_data} TTL:5m
        RD-->>BE: OK
        BE-->>FE: {session_token, user_profile, roles}
        FE-->>User: Redirect ke Dashboard
    end
```

### Sequence Diagram: [Contoh: Upload File ke MinIO]

```mermaid
sequenceDiagram
    title Upload File — MinIO Object Storage

    actor User as 👤 User
    participant FE as Frontend
    participant BE as Backend API (Go)
    participant MN as MinIO
    participant DB as PostgreSQL

    User->>FE: Pilih file & klik Upload
    FE->>FE: Validasi ukuran & ekstensi (client-side)
    FE->>BE: POST /api/v1/upload (multipart/form-data + Bearer Token)

    BE->>BE: Validasi JWT & RBAC role
    BE->>BE: Validasi Magic Bytes (header biner)
    BE->>BE: Validasi MIME type & ukuran

    alt Validasi Gagal
        BE-->>FE: 422 Unprocessable Entity {code: "ERR_INVALID_FILE"}
        FE-->>User: Tampilkan pesan error validasi
    else Validasi Berhasil
        BE->>BE: Generate nama file: UUID v4 + ekstensi asli
        BE->>MN: PutObject(bucket, uuid_filename, data)
        MN-->>BE: ETag / checksum
        BE->>DB: INSERT file_uploads (uuid, original_name, bucket, path, uploader_id)
        DB-->>BE: file_id
        BE-->>FE: 201 Created {file_id, presigned_url (15 menit)}
        FE-->>User: Preview file / konfirmasi sukses
    end
```

## C.4. Data Model & ERD (Penguncian Skema Global 100%)

> [!IMPORTANT]
> **KONTRAK PENGUNCIAN SKEMA DATABASE**:
> Seluruh tabel di bawah ini (tabel sistem & tabel bisnis) beserta kolom, tipe data PostgreSQL, Primary Key, Foreign Key, dan Index telah dikunci 100% dan menjadi acuan tunggal migrasi SQL (`db/migrations/`).

### C.4.1. Entity Relationship Diagram (ERD Visual)

```mermaid
erDiagram
    title ERD Lengkap — [Nama Sistem]

    ROLES ||--o{ USERS : "ditetapkan ke"
    ROLES ||--o{ ROLE_PERMISSIONS : "memiliki hak akses"
    MENUS ||--o{ ROLE_PERMISSIONS : "diatur dalam"
    MENUS ||--o{ MENUS : "sub-menu dari"
    USERS ||--o{ ACTIVITY_LOGS : "mencatat aktivitas"
    USERS ||--o{ FILE_UPLOADS : "mengunggah berkas"
    USERS ||--o{ TRANSAKSI_BISNIS : "membuat transaksi"

    ROLES {
        UUID id PK
        VARCHAR(50) name UK
        VARCHAR(100) label
        TEXT description
        BOOLEAN is_system
        TIMESTAMPTZ created_at
        TIMESTAMPTZ updated_at
    }

    USERS {
        UUID id PK
        VARCHAR(100) id_jss UK
        VARCHAR(150) nama_lengkap
        VARCHAR(255) email
        UUID role_id FK
        BOOLEAN is_active
        TIMESTAMPTZ created_at
        TIMESTAMPTZ updated_at
        TIMESTAMPTZ deleted_at
    }

    MENUS {
        UUID id PK
        UUID parent_id FK
        VARCHAR(50) category
        VARCHAR(100) label
        VARCHAR(255) route
        VARCHAR(50) icon
        INTEGER sort_order
        BOOLEAN is_active
        TIMESTAMPTZ created_at
    }

    ROLE_PERMISSIONS {
        UUID id PK
        UUID role_id FK
        UUID menu_id FK
        BOOLEAN can_view
        BOOLEAN can_create
        BOOLEAN can_update
        BOOLEAN can_delete
        TIMESTAMPTZ updated_at
    }

    ACTIVITY_LOGS {
        UUID id PK
        VARCHAR(100) id_jss
        VARCHAR(150) nama_lengkap
        VARCHAR(50) role
        VARCHAR(10) method
        VARCHAR(255) endpoint
        VARCHAR(50) ip_address
        INTEGER status_code
        JSONB payload_diff
        TIMESTAMPTZ created_at
    }

    FILE_UPLOADS {
        UUID id PK
        UUID uploader_id FK
        VARCHAR(255) original_name
        VARCHAR(100) bucket
        TEXT object_path
        VARCHAR(100) mime_type
        BIGINT size_bytes
        TIMESTAMPTZ created_at
    }

    TRANSAKSI_BISNIS {
        UUID id PK
        UUID user_id FK
        VARCHAR(100) nomor_dokumen UK
        VARCHAR(255) judul
        VARCHAR(50) status
        NUMERIC(15_2) nilai_nominal
        TIMESTAMPTZ tanggal_transaksi
        TIMESTAMPTZ created_at
        TIMESTAMPTZ updated_at
        TIMESTAMPTZ deleted_at
    }
```

### C.4.2. Kamus Data & Skema Database Detail (Data Dictionary)

| Nama Tabel | Nama Kolom | Tipe PostgreSQL | Constraint | Relasi / Index | Catatan |
|---|---|---|---|---|---|
| `roles` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | ID Unik Peran |
| `roles` | `name` | `VARCHAR(50)` | `NOT NULL UNIQUE` | `idx_roles_name` | Kode role (superadmin, pengawas, admin, operator) |
| `roles` | `label` | `VARCHAR(100)` | `NOT NULL` | - | Nama tampilan role |
| `users` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | ID Pengguna |
| `users` | `id_jss` | `VARCHAR(100)` | `NOT NULL UNIQUE` | `idx_users_id_jss` | ID SSO JSS Pemkot Jogja |
| `users` | `nama_lengkap`| `VARCHAR(150)` | `NOT NULL` | - | Terisi otomatis dari JSS |
| `users` | `role_id` | `UUID` | `NOT NULL` | `FK -> roles(id)` | Relasi wewenang role |
| `users` | `deleted_at` | `TIMESTAMPTZ` | `NULL` | - | Soft delete timestamp |
| `menus` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | ID Menu Sidebar |
| `menus` | `parent_id` | `UUID` | `NULL` | `FK -> menus(id)` | Relasi hierarki sub-menu |
| `menus` | `category` | `VARCHAR(50)` | `NOT NULL` | `idx_menus_category` | Kategori header (DASHBOARD, CONFIG, dll.) |
| `role_permissions`| `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | Matriks Hak Akses |
| `role_permissions`| `role_id` | `UUID` | `NOT NULL` | `FK -> roles(id)` | Target Role |
| `role_permissions`| `menu_id` | `UUID` | `NOT NULL` | `FK -> menus(id)` | Target Menu |
| `activity_logs` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | ID Log Audit |
| `activity_logs` | `id_jss` | `VARCHAR(100)` | `NOT NULL` | `idx_activity_jss` | User pelaksana |
| `activity_logs` | `endpoint` | `VARCHAR(255)` | `NOT NULL` | `idx_activity_endpoint`| Path yang diakses |
| `activity_logs` | `created_at` | `TIMESTAMPTZ` | `NOT NULL DEFAULT NOW()` | `idx_activity_created` | Waktu rekam log |
| `file_uploads` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | ID Berkas MinIO |
| `file_uploads` | `object_path`| `TEXT` | `NOT NULL` | - | UUID v4 path di MinIO |
| `[tabel_bisnis]` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - | Tabel Entitas Modul Bisnis |
| `[tabel_bisnis]` | `[kolom_fk]` | `UUID / INT` | `NOT NULL` | `FK -> [tabel_ref](id)`| Relasi bisnis |

---

## C.5. State Diagram — [Nama Entitas yang Punya Lifecycle]

```mermaid
stateDiagram-v2
    title State Diagram — Status [Nama Entitas]

    [*] --> Draft : dibuat oleh Operator

    Draft --> Diajukan : Operator submit
    Draft --> Dibatalkan : Operator batalkan

    Diajukan --> DalamReview : Admin mulai review
    Diajukan --> Dikembalikan : Admin minta revisi

    Dikembalikan --> Draft : Operator revisi ulang

    DalamReview --> Disetujui : Admin approve
    DalamReview --> Ditolak : Admin reject

    Disetujui --> [*] : selesai
    Dibatalkan --> [*] : selesai
    Ditolak --> [*] : selesai

    note right of Diajukan : Notifikasi email ke Admin
    note right of Disetujui : Notifikasi email ke Operator
    note right of Ditolak : Notifikasi email + alasan ke Operator
```

## C.6. Domain Model — Clean Architecture (Class Diagram)

```mermaid
classDiagram
    title Domain Model — Clean Architecture Go

    namespace Domain {
        class Entity {
            +UUID ID
            +string Name
            +time.Time CreatedAt
            +time.Time UpdatedAt
        }

        class EntityRepository {
            <<interface>>
            +FindByID(ctx, id UUID) Entity, error
            +FindAll(ctx, filter Filter) []Entity, int, error
            +Create(ctx, entity Entity) Entity, error
            +Update(ctx, entity Entity) Entity, error
            +Delete(ctx, id UUID) error
        }

        class EntityUsecase {
            <<interface>>
            +GetByID(ctx, id UUID) EntityResponse, error
            +GetAll(ctx, filter Filter) []EntityResponse, int, error
            +Create(ctx, req CreateRequest) EntityResponse, error
            +Update(ctx, id UUID, req UpdateRequest) EntityResponse, error
            +Delete(ctx, id UUID) error
        }
    }

    namespace Repository {
        class EntityRepositoryImpl {
            -pgxpool.Pool db
            +FindByID(ctx, id UUID) Entity, error
            +FindAll(ctx, filter Filter) []Entity, int, error
            +Create(ctx, entity Entity) Entity, error
            +Update(ctx, entity Entity) Entity, error
            +Delete(ctx, id UUID) error
        }
    }

    namespace Usecase {
        class EntityUsecaseImpl {
            -EntityRepository repo
            +GetByID(ctx, id UUID) EntityResponse, error
            +Create(ctx, req CreateRequest) EntityResponse, error
        }
    }

    namespace Delivery {
        class EntityHandler {
            -EntityUsecase usecase
            +GetByID(c *gin.Context)
            +GetAll(c *gin.Context)
            +Create(c *gin.Context)
            +Update(c *gin.Context)
            +Delete(c *gin.Context)
        }
    }

    EntityRepository <|.. EntityRepositoryImpl : implements
    EntityUsecase <|.. EntityUsecaseImpl : implements
    EntityUsecaseImpl --> EntityRepository : depends on
    EntityHandler --> EntityUsecase : depends on
```

## C.7. Persyaratan Non-Fungsional (SRS-NF-xx)

> Taksonomi **ISO/IEC 25010**. Setiap NFR wajib memiliki angka target terukur.

| ID | Kategori (ISO 25010) | Deskripsi Terukur | Target Konkret | Prioritas | Traceability | Metode Verifikasi |
|---|---|---|---|---|---|---|
| SRS-NF-01 | Performance Efficiency | P95 API response time | ≤ 200ms pada 100 concurrent users | Must | BR-xx | Load test (k6/Locust) |
| SRS-NF-02 | Performance Efficiency | Throughput minimum | ≥ 50 req/detik | Must | BR-xx | Load test |
| SRS-NF-03 | Security | Enkripsi data in-transit | TLS 1.3 minimum | Must | BR-xx | SSL Labs scan |
| SRS-NF-04 | Security | Session timeout | 5–10 menit inaktivitas | Must | BR-xx | Manual test |
| SRS-NF-05 | Security | Rate limiting | ≤ 100 req/menit per IP | Must | BR-xx | Integration test |
| SRS-NF-06 | Security | OWASP compliance | 0 temuan Medium/High/Critical | Must | BR-xx | SAST + DAST |
| SRS-NF-07 | Reliability | Uptime target | ≥ 99.5% (≤ 3.65 jam downtime/tahun) | Should | BR-xx | Uptime monitoring |
| SRS-NF-08 | Reliability | Backup database | Harian otomatis, retensi 30 hari | Must | BR-xx | Restore drill |
| SRS-NF-09 | Usability | Waktu onboarding | Pengguna baru bisa menjalankan task utama ≤ 10 menit | Should | PRD-xx | Usability test |
| SRS-NF-10 | Maintainability | Code coverage | Unit test ≥ 85% | Must | BR-xx | `go test -cover` |
| SRS-NF-11 | Compatibility | Browser support | Chrome 120+, Firefox 120+, Edge 120+ | Must | PRD-xx | Cross-browser test |
| SRS-NF-12 | Scalability | Horizontal scaling | Stateless backend, scale via Docker replicas | Should | BR-xx | Docker scale test |

## C.8. Antarmuka Eksternal (API/Integrasi)

| ID | Nama Interface | Sistem | Arah | Protokol | Auth | Rate Limit Eksternal | SLA | Fallback |
|---|---|---|---|---|---|---|---|---|
| INT-01 | SSO Login | Keycloak JSS | Keluar | OIDC / OAuth2 | PKCE | - | 99.9% | Tolak login, tampilkan pesan maintenance |
| INT-02 | Object Storage | MinIO | Keluar | S3 API (HTTPS) | IAM Key | - | Internal | Queue retry, notifikasi admin |

## C.9. Error Handling

### C.9.1. Standar Format Error Response

```json
{
  "code": "ERR_VALIDATION",
  "message": "Pesan error yang jelas dan informatif untuk pengguna",
  "details": [
    {"field": "nama_field", "issue": "required | min_length | invalid_format"}
  ],
  "trace_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### C.9.2. Katalog HTTP Status Code

| HTTP Code | Kapan Dipakai | Kode Error | Keterangan |
|---|---|---|---|
| 200 OK | Request sukses | - | Data dikembalikan |
| 201 Created | Resource berhasil dibuat | - | Data resource baru dikembalikan |
| 204 No Content | Delete sukses | - | Tidak ada body |
| 400 Bad Request | Syntax request salah | ERR_BAD_REQUEST | |
| 401 Unauthorized | Token tidak ada / expired | ERR_UNAUTHORIZED | |
| 403 Forbidden | Token valid tapi tidak punya akses | ERR_FORBIDDEN | |
| 404 Not Found | Resource tidak ditemukan | ERR_NOT_FOUND | |
| 409 Conflict | Duplikasi data | ERR_CONFLICT | |
| 422 Unprocessable Entity | Validasi bisnis gagal | ERR_VALIDATION | Sertakan `details` |
| 429 Too Many Requests | Rate limit terlampaui | ERR_RATE_LIMIT | Sertakan header `Retry-After` |
| 500 Internal Server Error | Kesalahan server | ERR_INTERNAL | Log ke sistem monitoring |
| 503 Service Unavailable | Dependensi eksternal down | ERR_SERVICE_UNAVAILABLE | Fallback response |

### C.9.3. Strategi Retry & Fallback

| Komponen | Strategi | Max Retry | Interval | Fallback |
|---|---|---|---|---|
| Database (pgxpool) | Exponential backoff | 3x | 100ms, 300ms, 1000ms | 503 + log |
| Redis | Fail-open (skip cache) | 1x | 50ms | Query langsung ke DB |
| MinIO | Exponential backoff | 3x | 200ms, 500ms, 2000ms | Queue ke pending + notifikasi |
| Keycloak | Fail-closed (tolak akses) | 0x | - | 503 + pesan maintenance |

## C.10. Constraint Teknis

### C.10.1. Stack Teknologi

| Komponen | Teknologi | Versi | Catatan |
|---|---|---|---|
| Backend | Go | 1.22+ | Clean Architecture (domain/usecase/delivery/repository) |
| HTTP Framework | Gin / Echo / Fiber | terbaru stabil | Pilih satu, konsisten |
| DB Driver | pgxpool | v5+ | Connection pooling wajib |
| ORM/Query | sqlc / raw SQL | - | Dilarang ORM yang menyembunyikan SQL |
| Auth | golang-jwt | v5 | JWKS public key dari Keycloak |
| Storage SDK | minio-go | v7 | Presigned URL, bukan public URL |
| Logger | zap | v1 | Structured logging (JSON output) |
| Config | godotenv / viper | - | Semua config dari env var |
| Frontend | React / Vue 3 | 18+ / 3.4+ | Vite sebagai bundler |
| UI Framework | Tailwind CSS / Metronic | 3.x / terbaru | Pilih sesuai keputusan tim |
| State Management | Zustand / Pinia | terbaru | |
| HTTP Client | Axios | terbaru | Interceptor untuk Bearer Token |
| Database | PostgreSQL | 16+ | Mandatory |
| Cache | Redis | 7+ | Opsional — hanya jika dibutuhkan |
| Storage | MinIO | RELEASE terbaru | Wajib untuk semua file |
| Auth Provider | Keycloak | 24+ | SSO JSS sso.jogjakota.go.id |
| Container | Docker + Docker Compose | 25+ / 2.x | Wajib untuk development lokal |
| Migration | golang-migrate | v4+ | Folder: `db/migrations/` |

### C.10.2. Environment Variables Wajib

| Variabel | Deskripsi | Contoh Nilai |
|---|---|---|
| `APP_ENV` | Environment: production / testing | `production` |
| `APP_PORT` | Port backend | `8080` |
| `DB_DSN` | PostgreSQL connection string | `postgres://user:pass@host:5432/db` |
| `REDIS_URL` | Redis connection URL | `redis://localhost:6379/0` |
| `KEYCLOAK_BASE_URL` | Base URL Keycloak | `https://sso.jogjakota.go.id` |
| `KEYCLOAK_REALM` | Nama realm Keycloak | `jogjakota` |
| `KEYCLOAK_CLIENT_ID` | Client ID aplikasi | `nama-aplikasi` |
| `KEYCLOAK_CLIENT_SECRET` | Client secret | `[secret]` |
| `MINIO_ENDPOINT` | MinIO endpoint | `minio:9000` |
| `MINIO_ACCESS_KEY` | MinIO access key | `[key]` |
| `MINIO_SECRET_KEY` | MinIO secret key | `[secret]` |
| `MINIO_BUCKET` | Nama bucket utama | `nama-aplikasi-files` |
| `MINIO_USE_SSL` | SSL untuk MinIO | `false` (Docker internal) |
| `ENABLE_TEST_AUTH` | Login manual (HANYA testing) | `false` |

### C.10.3. Larangan Teknis (Hard Constraints)

- ❌ **Dilarang**: menyimpan file ke folder lokal (`/uploads`, `/storage`)
- ❌ **Dilarang**: plaintext credentials di source code / repo Git
- ❌ **Dilarang**: unparameterized SQL queries (SQL injection risk)
- ❌ **Dilarang**: login manual (username/password lokal) di `APP_ENV=production`
- ❌ **Dilarang**: akses MinIO via public URL — wajib Presigned URL (TTL 5–15 menit)
- ❌ **Dilarang**: logika bisnis di layer delivery (handler) — wajib di usecase

## C.11. Definition of Done

Sistem dinyatakan selesai (Definition of Done) jika seluruh kriteria berikut terpenuhi:

| # | Kriteria | Cara Verifikasi |
|---|---|---|
| 1 | Semua `SRS-F-xx` MUST & SHOULD terimplementasi | Code review + acceptance test |
| 2 | Unit test coverage ≥ 85% | `go test -cover ./...` |
| 3 | Integration test: seluruh happy path + critical error path | Test suite CI |
| 4 | Swagger/OpenAPI tersinkron dengan implementasi | `swag init` berhasil, endpoint cocok |
| 5 | Security scan: 0 temuan Medium/High/Critical | `gosec`, `govulncheck`, `npm audit` |
| 6 | Semua Docker services `healthy` | `docker compose ps` |
| 7 | `docs/swagger.json` & `docs/swagger.yaml` tersinkron | File ada & up-to-date |
| 8 | `docs/CHANGELOG.md` diperbarui | Manual review |
| 9 | `docs/USER_MANUAL.md` tersedia | Skill user-manual-profesional |
| 10 | `docs/SECURITY_REPORT.md` tersedia | Skill security-pentester-profesional |
| 11 | Load test: NFR performance terpenuhi | k6 / Locust hasil ≥ target SRS-NF |
| 12 | 4 role RBAC (Superadmin/Pengawas/Admin/Operator) berfungsi benar | RBAC test matrix |

---

# BAGIAN D — RENCANA IMPLEMENTASI & KONTRAK TEKNIS MODULAR

> Bagian ini adalah panduan eksekusi teknis untuk agentic coding Antigravity 2.0.
> **Aturan Eksekusi**: Pembangunan aplikasi WAJIB dilakukan per-modul secara bertahap sesuai urutan dependensi build di bawah ini. DILARANG membuat modul berikutnya sebelum modul saat ini lulus Definition of Done.

## D.1. Peta Modul & Matriks Dependensi

| ID Modul | Nama Modul | PRD Terkait | SRS-F Terkait | Dependency (Prasyarat Selesai) | Urutan Build |
|---|---|---|---|---|:---:|
| `MOD-00` | Core Base, Auth SSO & Infra | `PRD-01` | `SRS-F-01`, `SRS-F-02` | - | 1 |
| `MOD-01` | Pengaturan Sistem & Master Data | `PRD-02` | `SRS-F-03`, `SRS-F-04` | `MOD-00` | 2 |
| `MOD-02` | [Nama Modul Bisnis 1] | `PRD-03` | `SRS-F-05`, `SRS-F-06` | `MOD-00`, `MOD-01` | 3 |
| `MOD-03` | [Nama Modul Bisnis 2] | `PRD-04` | `SRS-F-07`, `SRS-F-08` | `MOD-02` | 4 |
| `MOD-04` | Manajemen User & RBAC 4 Role | `PRD-05` | `SRS-F-09`, `SRS-F-10` | `MOD-00`, `MOD-01` | 5 |

## D.2. Diagram Dependensi Modul

```mermaid
flowchart LR
    MOD00["MOD-00: Core Base & Auth"] --> MOD01["MOD-01: Settings & Master Data"]
    MOD01 --> MOD02["MOD-02: [Modul Bisnis 1]"]
    MOD02 --> MOD03["MOD-03: [Modul Bisnis 2]"]
    MOD01 --> MOD04["MOD-04: User Management & RBAC"]
```

## D.3. Kontrak Teknis per Modul
> Ulangi blok ini untuk setiap `MOD-xx`. Tulis presisi tanpa narasi panjang.

### ─── Modul: [MOD-00 — Core Base, Auth SSO & Infrastructure] ───

#### 1. Struktur File & Folder
```text
backend/
├── cmd/api/main.go
├── internal/
│   ├── config/config.go
│   └── middleware/jwt_auth.go, rbac_gate.go, cors.go, rate_limiter.go
frontend/src/
├── App.tsx
├── routes/index.tsx
└── layouts/DashboardLayout.tsx (Frosted Glass Sidebar, Topbar Logo Pemkot Jogja)
```

#### 2. Kontrak Endpoint & Healthcheck
| Endpoint ID | Method | Path | Request Body | Response Success (200) | Response Error | Traceability |
|---|---|---|---|---|---|---|
| `API-CORE-01` | `GET` | `/api/v1/health` | - | `{"status": "UP", "services": {"db": "UP", "storage": "UP"}}` | `{"status": "DOWN"}` | `SRS-NF-01` |
| `API-CORE-02` | `GET` | `/swagger/index.html` | - | `Swagger UI Page` | `404 Not Found` | `SRS-NF-02` |

#### 3. Definition of Ready (DoR) & Definition of Done (DoD)
- **DoR**: Kredensial Keycloak OIDC, PostgreSQL, dan MinIO telah siap di `.env`.
- **DoD**: Endpoint `/api/v1/health` status `UP`, layout dashboard ter-render dengan Sidebar & Topbar resmi Pemkot Jogja.

---

### ─── Modul: [MOD-xx — Nama Modul Bisnis] ───

#### 1. Struktur File & Folder (Go Clean Architecture + React/Vue Vite)
```text
backend/
├── db/migrations/00000X_[nama_modul].up.sql
├── internal/
│   ├── domain/[nama_modul].go               # Struct Entity, DTO Request/Response, Interface
│   ├── repository/[nama_modul]_postgres.go   # Query SQL pgxpool ($1, $2, ...)
│   ├── usecase/[nama_modul]_usecase.go       # Business Logic & Validation
│   └── delivery/http/[nama_modul]_handler.go # Fiber/Gin HTTP Handler & Swagger Anotasi
frontend/src/
├── pages/[nama_modul]/                      # Page Index, Detail, Form
├── components/[nama_modul]/                 # Reusable Modul UI Components
└── services/[nama_modul].service.ts         # Axios API Caller with Bearer Token
```

#### 2. Skema Database (PostgreSQL 16+)
| Tabel | Kolom | Tipe Data | Constraint | Index / FK |
|---|---|---|---|---|
| `[nama_tabel]` | `id` | `UUID` | `PRIMARY KEY DEFAULT gen_random_uuid()` | - |
| `[nama_tabel]` | `nama` | `VARCHAR(255)` | `NOT NULL` | `idx_[tabel]_nama` |
| `[nama_tabel]` | `status` | `VARCHAR(50)` | `NOT NULL DEFAULT 'draft'` | `idx_[tabel]_status` |
| `[nama_tabel]` | `created_at` | `TIMESTAMPTZ` | `NOT NULL DEFAULT NOW()` | - |
| `[nama_tabel]` | `updated_at` | `TIMESTAMPTZ` | `NOT NULL DEFAULT NOW()` | - |

#### 3. Kontrak REST API
| Endpoint ID | Method | Path | Request Body (JSON) | Response Success (200/201) | Response Error (400/404/422) | Traceability SRS-F |
|---|---|---|---|---|---|---|
| `API-[MOD]-01` | `GET` | `/api/v1/[modul]` | `Query: page, limit, search, status` | `{"data": [...], "meta": {"page": 1, "total": 100}}` | `{"code": "ERR_FETCH", "message": "..."}` | `SRS-F-xx` |
| `API-[MOD]-02` | `POST` | `/api/v1/[modul]` | `{"nama": "string", "status": "string"}` | `{"code": "SUCCESS", "data": {...}}` | `{"code": "ERR_VALIDATION", "details": [...]}` | `SRS-F-xx` |
| `API-[MOD]-03` | `GET` | `/api/v1/[modul]/:id` | - | `{"data": {...}}` | `{"code": "ERR_NOT_FOUND"}` | `SRS-F-xx` |
| `API-[MOD]-04` | `PUT` | `/api/v1/[modul]/:id` | `{"nama": "string", "status": "string"}` | `{"code": "SUCCESS", "data": {...}}` | `{"code": "ERR_VALIDATION", "details": [...]}` | `SRS-F-xx` |
| `API-[MOD]-05` | `DELETE`| `/api/v1/[modul]/:id` | - | `{"code": "SUCCESS", "message": "Data dihapus"}` | `{"code": "ERR_DELETE"}` | `SRS-F-xx` |

#### 4. Spesifikasi UI Apple HIG
- **Layout & Permukaan**: Left Panel Menu aktif, Card Squircle `rounded-2xl`, Frosted Glass Header.
- **Tabel & Toolbar**: Live search debounce, dropdown filter, export button, pagination (10/25/50).
- **Modal Form**: Validasi inline error per field, feedback toast alert, dialog konfirmasi hapus.

#### 5. Definition of Ready (DoR)
- [ ] Modul dependensi prasyarat telah berstatus Definition of Done.
- [ ] Skema database & migrasi SQL untuk modul ini sudah final.
- [ ] Kontrak DTO request/response sudah disepakati.

#### 6. Definition of Done (DoD Teknis)
- [ ] Migrasi database `db/migrations/` berhasil dijalankan dan data seed terisi.
- [ ] Seluruh endpoint REST API terimplementasi & lulus verifikasi respon status code.
- [ ] Backend lulus kompilasi `go build ./...` tanpa error.
- [ ] UI frontend selesai mengonsumsi Design System Apple HIG (`.agents/design-system/components.md`).
- [ ] Status modul pada `docs/MODULE_PROGRESS.md` tercentang `Completed`.

---

# BAGIAN E — SPESIFIKASI UI & DESAIN VISUAL (APPLE HIG)

> Bagian ini mengunci karakteristik antarmuka agar antarmuka konsisten, estetis, dan tidak dibuat asal-asalan. Mengacu pada `.agents/design-system/components.md`.

## E.1. Design Tokens & Tema Terstandarisasi (Anti-Color Clash)
- **Kepatuhan Tema**: Wajib mendukung 8 tema terstandarisasi (4 Light + 4 Dark) berstandar WCAG AA/AAA Ratio ≥ 4.5:1.
- **Tipografi**: `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Inter, sans-serif`.
- **Corner Radius**: Squircle `rounded-2xl` (16–20px) untuk Card dan Modal Sheet; `rounded-xl` (10–12px) untuk Button & Form Input.
- **Efek Frosted Glass**: `backdrop-filter: blur(20px) saturate(180%)` pada Sidebar, Topbar Header, dan Floating Panel.
- **Branding Pemkot**: Logo Resmi Vektor Pemkot Jogja (`logo-jogja.svg`) + Nama Aplikasi di pojok kiri atas/sidebar (tinggi 36–44px) + Footer resmi `© [Tahun] Pemerintah Kota Yogyakarta`.

## E.2. Komponen Dasar & Reusabilitas
| Komponen | Spesifikasi & Interaksi | Digunakan di Modul |
|---|---|---|
| **Action Button** | Primary (`bg-primary text-white active:scale-95`), Secondary (`bg-slate-100 dark:bg-slate-800`), Danger (`bg-rose-600`) | Semua Modul |
| **Metric Card** | Squircle `rounded-2xl`, subtle border `border-slate-200/60 dark:border-slate-800/80`, tren persentase | Dashboard, Modul Bisnis |
| **Interactive Table** | Live search debounce (300ms), multi-filter dropdown, sortable column, pagination (10/25/50) | `MOD-01`, `MOD-02`, `MOD-04` |
| **Form Input** | Floating/clean label, format mask, error helper text inline di bawah input | Form Tambah & Ubah Data |
| **Action Modal Sheet** | Centered / right slide-over, overlay blur, tombol aksi konfirmasi & batal | Create, Edit, Delete Confirm |
| **Status Badge** | Soft background tint + solid text (Sukses: Emerald, Pending: Amber, Batal: Rose) | Data Table & Detail View |

## E.3. Matriks 4 State Wajib per Layar
| ID Layar | Modul Terkait | Loading State | Empty State | Error State | Success State |
|---|---|---|---|---|---|
| `UI-00` | `MOD-00` | Spinner overlay | - | Toast error merah | Redirect ke Dashboard |
| `UI-01` | `MOD-01` | Skeleton table 5 baris | Card ilustrasi offline + tombol "Tambah Data" | Banner alert merah + retry button | Toast hijau "Data disimpan" |
| `UI-02` | `MOD-02` | Skeleton card grid | Ilustrasi "Belum ada item" + CTA | Toast error inline | Modal tutup + toast update |

## E.4. Tata Letak (Layout) & Breakpoints Responsif
- **Desktop (≥ 1024px / `lg`)**: Left Panel Menu (Sidebar) fixed width 260px (collapsible to 80px), Topbar fixed, area konten grid 8pt.
- **Tablet & Mobile (< 1024px)**: Topbar dengan hamburger button, Sidebar berubah menjadi slide-over drawer modal, tabel data horizontal scrollable dengan sticky action column.
- **Asset Policy**: Seluruh icon menggunakan SVG inline (Lucide / Heroicons lokal), aset logo vektor dari `frontend/src/assets/logo-jogja.svg` (bebas dari raster JPG/PNG buram).

---

# BAGIAN F — MATRIKS KETERLACAKAN MENYELURUH (TRACEABILITY MATRIX)

Tabel ini menjamin seluruh rantai kebutuhan software terhubung utuh dari Kebutuhan Bisnis (`BR-xx`), Fitur Produk (`PRD-xx`), Kebutuhan Fungsional (`SRS-F-xx`), Modul Teknis (`MOD-xx`), hingga Spesifikasi Layar (`UI-xx`) tanpa ada tautan yang terputus (*0 Broken Links*).

| ID Bisnis (BR) | ID Fitur (PRD) | Nama Fitur / Modul | ID Fungsional (SRS-F) | ID Modul (MOD) | ID Layar (UI) | Status Traceability |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `BR-01` | `PRD-01` | [Modul Bisnis 1] | `SRS-F-01`, `SRS-F-02` | `MOD-02` | `UI-01` | ✅ Terhubung Penuh |
| `BR-02` | `PRD-02` | [Modul Bisnis 2] | `SRS-F-03`, `SRS-F-04` | `MOD-03` | `UI-02` | ✅ Terhubung Penuh |
| `BR-00` | `PRD-SET-01` | Manajemen Pengguna (SSO JSS) | `SRS-F-05` | `MOD-01` | `UI-SET-01` | ✅ Terhubung Penuh |
| `BR-00` | `PRD-SET-02` | Manajemen Role (Protected) | `SRS-F-06` | `MOD-01` | `UI-SET-02` | ✅ Terhubung Penuh |
| `BR-00` | `PRD-SET-03` | Manajemen Hak Akses (Matrix) | `SRS-F-07` | `MOD-01` | `UI-SET-03` | ✅ Terhubung Penuh |
| `BR-00` | `PRD-SET-04` | Manajemen Menu Sidebar | `SRS-F-08` | `MOD-01` | `UI-SET-04` | ✅ Terhubung Penuh |
| `BR-00` | `PRD-SET-05` | Manajemen Tema (8 Themes) | `SRS-F-09` | `MOD-01` | `UI-SET-05` | ✅ Terhubung Penuh |
| `BR-00` | `PRD-SET-06` | Log Aktivitas Pengguna (Audit) | `SRS-F-10` | `MOD-01` | `UI-SET-06` | ✅ Terhubung Penuh |

---

## Referensi

- BABOK v3 (IIBA) — dasar struktur BRD & elicitation.
- ISO/IEC/IEEE 29148:2018 — struktur & karakteristik requirement SRS.
- ISO/IEC 25010 — taksonomi non-functional requirement.
- MoSCoW (DSDM) — metode prioritasi fitur.
- Gherkin (Given/When/Then) — format acceptance criteria.
- Mermaid.js — ERD, Sequence, State, Class, Flowchart, C4.
- [Tambahkan dokumen/riset lain yang dipakai sebagai sumber, dengan nama file/audio-nya]

---

## Review & Iterasi

Setelah draft pertama: minta saya review per bagian, ajukan pertanyaan verifikasi, perbarui Blueprint.md. Iterasi sampai saya nyatakan isi Blueprint final. **Baru setelah itu** susun Dokumen Blueprint resmi (Google Docs / .docx) yang disimpan di folder `docs/` berdasarkan `references/template-dokumen-resmi.md` — jangan buat dokumen resmi dari draft yang belum disetujui. Revisi besar setelah dokumen resmi dibuat → simpan versi baru (`Blueprint_v2.md` + `docs/Dokumen_Blueprint_Resmi_v2.docx`), jangan timpa tanpa konfirmasi.
