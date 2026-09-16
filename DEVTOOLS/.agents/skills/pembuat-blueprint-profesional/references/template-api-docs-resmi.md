# 📑 DOKUMEN SPESIFIKASI API & INTEGRASI SISTEM (UNTUK DEVELOPER EKSTERNAL)

---

## LEMBAR KONTROL DOKUMEN

| Metadata | Keterangan |
| :--- | :--- |
| **Nama Sistem / API** | [Nama Sistem] API Gateway & RESTful Service |
| **Versi API** | `v1.0.0` |
| **Base URL Staging** | `https://api-staging.jogjakota.go.id/[nama-app]` |
| **Base URL Production** | `https://api.jogjakota.go.id/[nama-app]` |
| **Swagger UI Interaktif** | `https://api.jogjakota.go.id/[nama-app]/swagger/index.html` |
| **Spesifikasi Berkas** | `docs/swagger.json`, `docs/swagger.yaml`, `docs/Dokumen_Spesifikasi_API.docx` |
| **Pengelola API** | Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta |
| **Target Pengguna** | Developer Eksternal, Tim Integrasi Antar-OPD, Vendor Pihak Ketiga |

---

## 1. 🌐 PENDAHULUAN & STANDAR INTEGRASI

Dokumen ini ditujukan bagi programmer dan developer eksternal yang akan melakukan integrasi sistem dengan layanan [Nama Aplikasi]. Seluruh endpoint API mengikuti kaidah arsitektur RESTful murni dengan format pertukaran data JSON.

### 1.1 Standar Protokol & Komunikasi
- **Protokol**: HTTPS (TLS 1.3 wajib pada lingkungan produksi).
- **Format Payload**: `application/json; charset=utf-8`.
- **Standar Waktu**: ISO 8601 UTC / RFC 3339 (`YYYY-MM-DDTHH:mm:ssZ`).
- **Idempotency**: Seluruh endpoint `GET`, `PUT`, `DELETE` bersifat idempoten.

---

## 2. 🔐 AUTENTIKASI & OTORISASI (SSO KEYCLOAK JSS)

Seluruh endpoint protected mewajibkan penyertaan Bearer Token JWT pada Header HTTP:

```http
Authorization: Bearer <access_token_jwt>
```

### 2.1 Alur Autentikasi Eksternal (Client Credentials / OIDC)
1. Developer mengajukan `client_id` dan `client_secret` kepada Tim Keamanan Informasi Diskominfo Kota Yogyakarta.
2. Melakukan request token ke Keycloak JSS Auth Server:
   - **Token Endpoint**: `https://sso.jogjakota.go.id/auth/realms/jogjakota/protocol/openid-connect/token`
   - **Grant Type**: `client_credentials` atau `authorization_code`.

### 2.2 Hak Akses Berbasis Role (RBAC)
| Role | Deskripsi Wewenang |
| :--- | :--- |
| **Superadmin** | Full access ke seluruh endpoint dan parameter konfigurasi. |
| **Admin** | Manajemen pengguna, pemetaan hak akses, dan pengaturan operasional. |
| **Operator** | Transaksi operasional harian (CRUD data bisnis). |
| **Pengawas** | Akses pemantauan *Read-Only* (hanya method `GET`). Mutasi data akan menghasilkan `403 Forbidden`. |

---

## 3. 📦 STANDAR STRUKTUR RESPONSE JSON

### 3.1 Respons Sukses (HTTP 200 / 201)
```json
{
  "code": "SUCCESS",
  "message": "Operasi data berhasil diproses.",
  "data": {
    "id": "a5e8f0a3-2c1b-4f9e-8c3d-1a2b3c4d5e6f",
    "nama": "Contoh Data",
    "created_at": "2026-08-27T08:00:00Z"
  }
}
```

### 3.2 Respons Sukses dengan Paginasi (HTTP 200)
```json
{
  "code": "SUCCESS",
  "message": "Daftar data berhasil diambil.",
  "data": [ ... ],
  "meta": {
    "page": 1,
    "limit": 10,
    "total_items": 150,
    "total_pages": 15
  }
}
```

### 3.3 Respons Kesalahan Standar (HTTP 4xx / 5xx)
```json
{
  "code": "ERR_VALIDATION",
  "message": "Format input data tidak valid.",
  "errors": [
    {
      "field": "limit",
      "message": "limit must be an integer between 1 and 100"
    }
  ],
  "trace_id": "7f9a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c"
}
```

---

## 4. 🛑 DAFTAR KODE KESALAHAN HTTP (HTTP STATUS CODES)

| Kode HTTP | Error Code | Keterangan & Tindakan Developer |
| :---: | :--- | :--- |
| `200 OK` | `SUCCESS` | Request berhasil dieksekusi. |
| `201 Created` | `SUCCESS_CREATED` | Resource baru berhasil dibuat. |
| `400 Bad Request` | `ERR_BAD_REQUEST` | Payload JSON rusak, type mismatch (misal teks pada field integer), atau missing mandatory fields. |
| `401 Unauthorized` | `ERR_UNAUTHORIZED` | Token tidak disertakan, token kedaluwarsa, atau tanda tangan tidak valid. |
| `403 Forbidden` | `ERR_FORBIDDEN` | Role tidak memiliki hak akses (misal Pengawas mencoba POST/PUT/DELETE). |
| `404 Not Found` | `ERR_NOT_FOUND` | Data atau endpoint yang dituju tidak ditemukan. |
| `409 Conflict` | `ERR_DUPLICATE` | Pelanggaran constraint unik (data sudah ada). |
| `422 Unprocessable` | `ERR_VALIDATION` | Data gagal validasi aturan logika bisnis. |
| `429 Too Many Req` | `ERR_RATE_LIMIT` | Melampaui kuota pemanggilan (maks 60 req/menit per IP). |
| `500 Server Error` | `ERR_INTERNAL` | Terjadi kesalahan internal pada server (laporkan `trace_id` ke admin). |

---

## 5. 📂 RINCIAN ENDPOINT API (API CATALOG)

### 5.1 Modul Autentikasi & Profil Pengguna

#### `GET /api/v1/auth/profile`
Mengambil data profil pengguna yang sedang terautentikasi berdasarkan JWT token.
- **Headers**: `Authorization: Bearer <token>`
- **Response 200 OK**:
```json
{
  "code": "SUCCESS",
  "message": "Profil berhasil dimuat.",
  "data": {
    "user_id": "uuid-v4",
    "username": "operator1",
    "nama_lengkap": "Operator Diskominfo",
    "email": "operator@jogjakota.go.id",
    "role": "Operator"
  }
}
```

---

### 5.2 Modul Bisnis Utama `[PRD-01]`

#### `GET /api/v1/[resource]`
Mengambil daftar data dengan dukungan filter, pencarian, dan paginasi.
- **Headers**: `Authorization: Bearer <token>`
- **Query Parameters**:
  - `page` *(integer, default 1)*: Nomor halaman.
  - `limit` *(integer, default 10, max 100)*: Jumlah data per halaman.
  - `search` *(string, optional)*: Kata kunci pencarian.
  - `status` *(string, optional)*: Filter status data.

#### `POST /api/v1/[resource]`
Membuat data transaksi baru.
- **Headers**: `Authorization: Bearer <token>`, `Content-Type: application/json`
- **Request Body (JSON)**:
```json
{
  "nama": "String (wajib, max 100 char)",
  "kategori_id": 1,
  "keterangan": "String (opsional)",
  "file_attachment_uuid": "uuid-v4-dari-minio"
}
```

---

### 5.3 Modul Object Storage MinIO

#### `POST /api/v1/storage/presigned-url`
Meminta URL presigned untuk upload langsung berkas ke MinIO storage.
- **Request Body**:
```json
{
  "filename": "dokumen_pendukung.pdf",
  "content_type": "application/pdf",
  "size_bytes": 1048576
}
```
- **Response 200 OK**:
```json
{
  "code": "SUCCESS",
  "data": {
    "upload_url": "https://minio.jogjakota.go.id/bucket/uuid-v4?X-Amz-Signature=...",
    "file_uuid": "uuid-v4",
    "expires_in_seconds": 600
  }
}
```

---

## 6. 🛡️ KEAMANAN & BATASAN PENGGUNAAN (RATE LIMIT & BEST PRACTICES)

1. **Rate Limiting**: Setiap client dibatasi maksimal 60 request per menit. Jika terlampaui, sistem merespons dengan HTTP `429 Too Many Requests`.
2. **Penanganan Token Expired**: Client wajib memperbarui token menggunakan Refresh Token sebelum kedaluwarsa.
3. **Data Sanitization**: Seluruh input teks secara otomatis disaring terhadap karakter berbahaya (SQL Injection, XSS tags).
4. **Bantuan & Dukungan Teknis**: Untuk bantuan integrasi dan pelaporan issue, hubungi Helpdesk Diskominfo Kota Yogyakarta via email `diskominfo@jogjakota.go.id`.
