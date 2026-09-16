# 📖 DOKUMEN SPESIFIKASI API & INTEGRASI SISTEM SIWASIN
> **Spesifikasi Antarmuka Layanan (API) untuk Pengembang & System Integration**

---

## 1. Informasi Layanan API

| Parameter | Nilai |
|---|---|
| Nama Sistem | SIWASIN (Sistem Informasi Pengawasan Internal) |
| Base URL (Staging) | `http://localhost:8080/api/v1` |
| Swagger UI | `http://localhost:8080/swagger/index.html` |
| Skema Autentikasi | OAuth 2.0 / OpenID Connect (OIDC) Bearer JWT Keycloak JSS |
| Format Data | JSON (`application/json`) |

---

## 2. Endpoints Utama SIWASIN

### 2.1 Autentikasi & Health Diagnostic
- `GET /health` : Verifikasi konektivitas DB, MinIO, Redis, dan Keycloak.
- `POST /auth/login` : Login SSO JSS & 1-Click Sandbox Login (Returns JWT Token & User Context).

### 2.2 Modul Risk Mapping OPD (Sekretariat)
- `GET /risk-mappings` : List riwayat penilaian risiko OPD per periode semester/tahun.
- `POST /risk-mappings` : Input skor parameter audit kinerja & kalkulasi gradasi risiko otomatis.

### 2.3 Modul Perencanaan PKPT
- `GET /pkpt` : List perencanaan PKPT Global & Tim (Filter: Mandatori / Non-Mandatori).
- `POST /pkpt` : Tambah draf PKPT terhubung dengan Master Tujuan, Sasaran, Output, dan Obrik OPD.

### 2.4 Modul Surat Tugas & Approval Inspektur
- `GET /surat-tugas` : List Surat Tugas penugasan audit.
- `POST /surat-tugas` : Buat usulan Surat Tugas (Enforce Enforce HP `<= 16 HP`, status `WAITING_INSPEKTUR`).
- `POST /surat-tugas/{id}/approve` : Approval pimpinan Inspektur (Restricted Inspektur Only).

### 2.5 Modul Realisasi & Restricted Laporan Pengawasan
- `POST /realisasi/{id}/laporan` : Upload berkas LHP ke MinIO Storage (Magic Bytes Check).
- `GET /laporan/{id}/download` : Generate Presigned URL download LHP (Restricted: Inspektur, Sekretaris, Irban, Eselon IVB SIMPEG).

### 2.6 Modul Dashboard & Matriks Evaluasi
- `GET /dashboard/evaluasi-triwulanan` : Matriks komparasi realisasi vs perencanaan PKPT.
- `GET /settings/activity-logs` : Log aktivitas pengguna (Restricted: Superadmin & Pengawas).

---
*Spesifikasi API ini diterbitkan oleh Diskominfo Kota Yogyakarta untuk panduan integrasi sistem.*
