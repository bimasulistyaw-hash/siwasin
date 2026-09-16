# 📊 Pelacak Progres Pembangunan Modul Aplikasi (Traceability & Quality Gate)

> Dokumen ini melacak siklus pembangunan aplikasi secara bertahap per modul untuk menjamin seluruh kebutuhan pada `Blueprint.md` terimplementasi 100% tanpa ada fitur yang terlewat atau kode stub kosong (`// TODO`).

---

## 🎯 DAFTAR MODUL & STATUS IMPLEMENTASI

| No | Nama Modul | ID Blueprint (`SRS-F-xx`) | DB Migration & Seeds | Backend Clean Arch | Frontend UI & Apple HIG | Verifikasi Kompilasi & API | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **0** | **Core Base & Auth** | `SRS-F-01`, `SRS-F-02` | [ ] | [ ] | [ ] | [ ] | ⏳ In Progress |
| **1** | **Pengaturan Sistem & Master Data** | `SRS-F-03`, `SRS-F-04` | [ ] | [ ] | [ ] | [ ] | ⏸️ Pending |
| **2** | **[Modul Bisnis 1]** | `SRS-F-05`, `SRS-F-06` | [ ] | [ ] | [ ] | [ ] | ⏸️ Pending |
| **3** | **[Modul Bisnis 2]** | `SRS-F-07`, `SRS-F-08` | [ ] | [ ] | [ ] | [ ] | ⏸️ Pending |
| **4** | **Manajemen User & RBAC 4 Role** | `SRS-F-09`, `SRS-F-10` | [ ] | [ ] | [ ] | [ ] | ⏸️ Pending |

---

## 📝 CATATAN EKSEKUSI PER MODUL

### Modul 0: Core Base & Auth
- [ ] Database Schema: tabel user, roles, audit logs, uuid extension.
- [ ] Backend: Setup fiber/gin router, SSO Keycloak JWT interceptor, RBAC middleware, `/api/v1/health`, Swagger UI.
- [ ] Frontend: Inisiasi React/Vue + Vite + Tailwind, Sidebar Frosted Glass, Topbar Logo Pemkot Jogja, Base Theme Switcher.
- [ ] Uji: `go build ./...` sukses, diagnostic health check mengembalikan status `UP`.

### Modul 1: [Nama Modul]
- [ ] Database Migration & Seed SQL: `backend/db/migrations/00000X_create_[modul].up.sql`.
- [ ] Backend Clean Architecture:
  - `internal/domain/[modul].go`
  - `internal/repository/[modul]_postgres.go`
  - `internal/usecase/[modul]_usecase.go`
  - `internal/delivery/http/[modul]_handler.go`
- [ ] Frontend UI Apple HIG (100% Real API Connected):
  - Data Table dengan live search debounce, filter multi-kategori, pagination (Request API GET).
  - Action Modal Form (Tambah/Ubah) dengan validasi field & preview upload MinIO (Request API POST/PUT).
  - Modal konfirmasi hapus data (Request API DELETE).
  - Toast feedback notification.
- [ ] Uji: Kompilasi `go build ./...` & `npm run build` bebas error.

---

## 🔍 QUALITY GATE: AUDIT KELENGKAPAN FITUR (ANTI-TERTINGGAL)
> **Wajib Diverifikasi Sebelum Beralih ke Tahap Pengujian QA**

| No | ID SRS-F | Fitur / Kebutuhan Bisnis | Tabel DB SQL | Endpoint API Backend | Komponen UI Frontend | Status Koneksi API | Verifikasi Audit |
| :-: | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| 1 | `SRS-F-01` | Autentikasi SSO Keycloak & Login Terpisah | `users`, `roles` | `POST /api/v1/auth/login` | `pages/Login.tsx` | 100% Real API | [ ] Terverifikasi |
| 2 | `SRS-F-02` | Sandbox 4 Role Quick Login | `users`, `roles` | `POST /api/v1/auth/quick-login` | `pages/Login.tsx` | 100% Real API | [ ] Terverifikasi |
| 3 | `SRS-F-03` | [Fitur Bisnis Modul 1] | `[tabel]` | `GET/POST /api/v1/[resource]` | `pages/[Page].tsx` | 100% Real API | [ ] Terverifikasi |
| 4 | `SRS-F-04` | [Fitur Bisnis Modul 2] | `[tabel]` | `GET/POST /api/v1/[resource]` | `pages/[Page].tsx` | 100% Real API | [ ] Terverifikasi |
| 5 | `SRS-F-05` | Pengaturan Menu Drag-and-Drop | `menus` | `PUT /api/v1/menus/reorder` | `pages/MenuSetting.tsx` | 100% Real API | [ ] Terverifikasi |
| 6 | `SRS-F-06` | Log Aktivitas Pengguna (Audit Trail) | `activity_logs` | `GET /api/v1/activity-logs` | `pages/ActivityLogs.tsx` | 100% Real API | [ ] Terverifikasi |

> **Pernyataan Quality Gate Audit**:
> - [ ] Seluruh ID `SRS-F-xx` dari `Blueprint.md` telah tertelusuri 100% tanpa ada yang tertinggal.
> - [ ] Tidak ada kode stub kosong (`// TODO`), array dummy palsu di frontend, atau tombol UI yang belum memanggil API backend.
> - [ ] Sistem siap untuk dilanjutkan ke tahap penyusunan skenario pengujian QA.
