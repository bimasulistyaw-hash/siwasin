# 🏛️ RULE: CLEAN ARCHITECTURE, INFRASTRUKTUR & HIGH PERFORMANCE STANDARDS

## 0. ⚡ KONFIRMASI INFRASTRUKTUR — WAJIB TANYA SEBELUM MULAI CODING

**Sebelum membuat kode apapun**, agent WAJIB mengajukan dua pertanyaan konfirmasi kepada prompter:

### Pertanyaan 1 — Mode Deployment Development:
```
🛠️ Aplikasi dan seluruh layanan pendukungnya akan dijalankan menggunakan:

  [A] Docker Compose (semua service dalam kontainer — PostgreSQL, Redis, MinIO, Backend, Frontend)
  [B] Lokal / Native (service dijalankan langsung di mesin tanpa Docker)
  [C] Hybrid (sebagian Docker, sebagian lokal — sebutkan mana yang Docker dan mana yang lokal)

Pilihan Anda? (A / B / C)
```

### Pertanyaan 2 — Kebutuhan Layanan Pendukung:
```
📦 Layanan pendukung apa yang dibutuhkan aplikasi ini?
(Jawab Ya/Tidak untuk masing-masing)

  [ ] Redis    — Apakah aplikasi butuh caching in-memory atau rate limiting berbasis Redis?
               Contoh butuh: API publik frekuensi tinggi, session cache, job queue.
               Contoh TIDAK butuh: CRUD sederhana, aplikasi internal traffic rendah.
  [ ] MinIO    — Apakah aplikasi perlu menyimpan file/dokumen unggahan pengguna?
  [ ] Keycloak — Apakah autentikasi menggunakan SSO JSS Keycloak?

Jawaban Anda?
```

**Aturan keputusan berdasarkan jawaban:**
| Pilihan | Tindakan Agent |
| :--- | :--- |
| Docker Compose (A) | Buat `docker-compose.yml` lengkap sesuai service yang dipilih. |
| Lokal / Native (B) | Buat `.env.example` dengan konfigurasi koneksi lokal. Buat `README.md` yang memandu instalasi manual setiap service di lokal. |
| Hybrid (C) | Buat `docker-compose.yml` hanya untuk service yang di-Docker. Sisanya dikonfigurasi via env lokal. |
| Redis tidak dibutuhkan | **Hapus Redis dari seluruh stack** — tidak ada konfigurasi Redis, tidak ada dependency `go-redis`, tidak ada rate limiting Redis. Gunakan alternatif jika perlu (in-memory rate limiter, IP-based middleware, dll). |
| MinIO tidak dibutuhkan | Hapus MinIO dari stack. File upload (jika ada) dapat disimpan ke filesystem lokal atau diabaikan. |

---

## 1. Database — PostgreSQL 16+ (Selalu Wajib)
- **Database Wajib**: **PostgreSQL 16+** sebagai satu-satunya database relasional utama.
- Driver: `jackc/pgx/v5/pgxpool` dengan parameterized query (`$1, $2, ...`).
- Wajib konfigurasi `MaxConns`, `MinConns`, dan `MaxConnIdleTime`.

---

## 2. Redis — OPSIONAL (Hanya Jika Benar-Benar Dibutuhkan)

Redis **HANYA** digunakan jika minimal satu dari kondisi berikut **terpenuhi**:

| Kondisi | Butuh Redis? |
| :--- | :---: |
| API publik dengan estimasi > 100 request/menit dari satu sumber | ✅ Ya |
| Kebutuhan session cache untuk mengurangi query DB berulang | ✅ Ya |
| Background job queue atau task scheduling | ✅ Ya |
| Rate limiting ketat pada endpoint login / OTP | ✅ Ya |
| Aplikasi internal dengan traffic rendah (< 50 concurrent users) | ❌ Tidak |
| CRUD sederhana tanpa endpoint publik | ❌ Tidak |
| Tidak ada kebutuhan real-time / caching khusus | ❌ Tidak |

**Jika Redis TIDAK dibutuhkan:**
- Hapus seluruh konfigurasi Redis dari `docker-compose.yml`, `.env`, dan `internal/config/`.
- Jangan tambahkan dependency `redis/go-redis` ke `go.mod`.
- Rate limiting (jika diperlukan): gunakan middleware in-memory berbasis IP (`golang.org/x/time/rate`) sebagai alternatif ringan.
- Jangan memaksakan Redis hanya karena ada di template standar.

**Jika Redis dibutuhkan:**
- Gunakan Redis 7 Alpine.
- Implementasikan pola Cache-Aside dengan TTL terukur.
- Invalidate cache saat terjadi mutasi data.

---

## 3. MinIO Object Storage — OPSIONAL (Hanya Jika Ada Fitur Upload)

MinIO **HANYA** digunakan jika aplikasi memiliki fitur unggah file/dokumen oleh pengguna.

**Jika MinIO TIDAK dibutuhkan:** Hapus dari stack. Tidak perlu konfigurasi bucket, access key, atau presigned URL.

**Jika MinIO dibutuhkan:** Ikuti `rules/03_minio_storage.md` sepenuhnya.

---

## 4. Jaminan Konektivitas Antar-Layanan (Docker & Lokal/Native)

Aplikasi yang dibangun **WAJIB terhubung secara otomatis (pre-wired & verified)** dengan seluruh layanan pendukungnya:

### 4.1 Matriks Konektivitas & Pengkabelan Environment (Wiring)
| Layanan | Mode Docker Compose | Mode Lokal (Native) | Mekanisme Inisialisasi Otomatis |
| :--- | :--- | :--- | :--- |
| **PostgreSQL 16+** | `DB_HOST=postgres`<br>`DB_PORT=5432` | `DB_HOST=localhost`<br>`DB_PORT=5432` | Koneksi `pgxpool` otomatis, eksekusi migrasi skema SQL (`db/migrations/`) saat backend boot. |
| **MinIO Storage** *(jika aktif)* | `MINIO_ENDPOINT=minio:9000`<br>`MINIO_USE_SSL=false` | `MINIO_ENDPOINT=localhost:9000`<br>`MINIO_USE_SSL=false` | MinIO Go SDK otomatis mengecek & membuat bucket default (`MINIO_BUCKET_NAME`) saat startup jika belum ada. |
| **Redis Cache** *(jika aktif)* | `REDIS_HOST=redis`<br>`REDIS_PORT=6379` | `REDIS_HOST=localhost`<br>`REDIS_PORT=6379` | Client Redis otomatis melakukan `Ping(ctx)` saat startup; fallback aman jika koneksi gagal. |
| **SSO Keycloak** | `KEYCLOAK_URL=https://sso.jogjakota.go.id` *(atau container keycloak)* | `KEYCLOAK_URL=https://sso.jogjakota.go.id` | Discovery OIDC `.well-known/openid-configuration` & caching JWKS public keys. |
| **Frontend ↔ Backend** | `VITE_API_URL=http://localhost:8080/api/v1` | `VITE_API_URL=http://localhost:8080/api/v1` | Axios/Fetch pre-configured instance dengan interceptor Bearer Token & error handler. |

### 4.2 Endpoint Health Check Otomatis (`/api/v1/health`)
Backend **WAJIB** menyediakan endpoint `/api/v1/health` untuk memvalidasi status koneksi seluruh layanan pendukung:
```json
{
  "status": "UP",
  "timestamp": "2026-08-28T14:30:00+07:00",
  "checks": {
    "database": { "status": "CONNECTED", "latency_ms": 1.2 },
    "storage": { "status": "CONNECTED", "bucket": "dokumen-app" },
    "cache": { "status": "CONNECTED", "type": "redis" },
    "auth": { "status": "CONFIGURED", "provider": "keycloak-jss" }
  }
}
```

### 4.3 Standar Orkestrasi Docker Compose (`docker-compose.yml`)
- **Single Network**: Semua service berada dalam satu user-defined bridge network `app-network`.
- **Health Checks & Dependency Ordering**: Backend menggunakan `depends_on` dengan `condition: service_healthy` untuk memastikan database dan MinIO sudah siap menerima koneksi sebelum backend menjalankan migrasi dan menyala:
```yaml
version: '3.8'

networks:
  app-network:
    driver: bridge

volumes:
  pgdata:
  miniodata:
  redisdata:

services:
  postgres:
    image: postgres:16-alpine
    container_name: app_postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${DB_USER:-appuser}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-appsecret}
      POSTGRES_DB: ${DB_NAME:-appdb}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./backend/db/migrations:/docker-entrypoint-initdb.d
    networks:
      - app-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-appuser} -d ${DB_NAME:-appdb}"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: app_redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  minio:
    image: minio/minio:latest
    container_name: app_minio
    restart: unless-stopped
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: ${MINIO_ACCESS_KEY:-minioadmin}
      MINIO_ROOT_PASSWORD: ${MINIO_SECRET_KEY:-miniopassword}
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - miniodata:/data
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 5s
      timeout: 3s
      retries: 5

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: app_backend
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      minio:
        condition: service_healthy
    env_file:
      - .env
    ports:
      - "8080:8080"
    networks:
      - app-network

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: app_frontend
    restart: unless-stopped
    depends_on:
      - backend
    ports:
      - "3000:80"
    networks:
      - app-network
```

---

## 5. Backend Clean Architecture (Go)
- **Domain Layer** (`internal/domain/`): Entity structs murni & interfaces. Dilarang impor framework eksternal.
- **Usecase Layer** (`internal/usecase/`): Business logic. Bergantung hanya pada domain interfaces.
- **Repository Layer** (`internal/repository/`): Akses data PostgreSQL (+ Redis jika aktif). Parameterized query wajib.
- **Delivery Layer** (`internal/delivery/http/`): HTTP handler, DTO, validasi, routing.

---

## 6. High Concurrency & Low Latency (< 200ms)
- **PostgreSQL Connection Pool**: `pgxpool` dengan `MaxConns`, `MinConns`, `MaxConnIdleTime`.
- **Redis Cache-Aside** *(hanya jika Redis aktif)*: Cache data referensi dengan TTL. Invalidate saat mutasi.
- **In-Memory Rate Limiter** *(alternatif tanpa Redis)*: `golang.org/x/time/rate` berbasis per-IP.
- **Frontend**: Code splitting, lazy loading, kompresi assets untuk FCP < 1.2 detik.

---

## 7. Format Respon JSON Standar
```json
// Sukses
{ "success": true, "status": 200, "message": "Data berhasil diproses.", "data": { ... } }

// Gagal
{ "success": false, "status": 400, "message": "Pesan deskriptif penyebab kegagalan.", "data": null }
```

---

## 8. Otomatisasi Halaman & Dokumentasi Swagger API (OpenAPI)

Saat Backend Agent membuat atau memperbarui API, halaman Swagger UI dan spesifikasinya **WAJIB dibuat dan disinkronkan secara otomatis**:

1. **Anotasi Global Otomatis (`cmd/api/main.go`)**:
   ```go
   // @title           [Nama Sistem] RESTful API
   // @version         1.0.0
   // @description     Dokumentasi Resmi API Sistem Informasi Diskominfo Kota Yogyakarta
   // @host            localhost:8080
   // @BasePath        /api/v1
   // @securityDefinitions.apikey BearerAuth
   // @in              header
   // @name            Authorization
   // @description     Masukkan token JWT dengan format: Bearer <token>
   ```

2. **Mounting Router Swagger UI Otomatis (`internal/delivery/http/router.go`)**:
   - Router HTTP **WAJIB** mendaftarkan handler Swagger UI sehingga otomatis aktif dan dapat diakses langsung pada:
     `http://localhost:8080/swagger/index.html`
   - Gunakan wrapper standar:
     - Fiber: `app.Get("/swagger/*", swagger.HandlerDefault)` (`github.com/gofiber/swagger`)
     - Gin: `r.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))` (`github.com/swaggo/gin-swagger`)
     - Chi/Echo/Standard HTTP: `httpSwagger.WrapHandler` (`github.com/swaggo/http-swagger`)

3. **Anotasi Handler Per-Endpoint Otomatis**:
   - Setiap fungsi controller/handler di `internal/delivery/http/` **WAJIB** langsung menyertakan blok anotasi:
   ```go
   // GetList godoc
   // @Summary      Mendapatkan daftar data
   // @Description  Mengambil seluruh data referensi dengan filter & pagination
   // @Tags         [Nama Modul]
   // @Accept       json
   // @Produce      json
   // @Param        page query int false "Nomor halaman" default(1)
   // @Param        limit query int false "Jumlah data per halaman" default(10)
   // @Success      200 {object} response.StandardSuccess
   // @Failure      400 {object} response.StandardError
   // @Failure      401 {object} response.StandardError
   // @Failure      403 {object} response.StandardError
   // @Router       /api/v1/[resource] [get]
   // @Security     BearerAuth
   ```

4. **Eksekusi Otomatisasi Generate (`Makefile` & Dockerfile)**:
   - Target `make swagger` atau `make docs` otomatis mengeksekusi:
     ```bash
     swag init -g cmd/api/main.go -o docs/ --parseDependency --parseInternal
     cp -r docs/swagger.* backend/docs/ 2>/dev/null || true
     python3 .agents/scripts/generate_docx.py -i docs/swagger.yaml -o docs/Dokumen_Spesifikasi_API.docx -t "SPESIFIKASI API" --title "Dokumen Spesifikasi API Developer Eksternal" --app "[NamaApp]"
     ```
   - Dalam Dockerfile multi-stage development, `swag init` otomatis dijalankan sebelum kompilasi binary `api` sehingga artefak `docs/swagger.json`, `docs/swagger.yaml`, dan halaman `/swagger/index.html` selalu terbarui secara konsisten.

5. **Auto-Generate TypeScript Client dari OpenAPI (`docs/swagger.json`)**:
   - Frontend **WAJIB** men-generate model interface dan HTTP client types langsung dari `docs/swagger.json` via command:
     ```bash
     npx -y openapi-typescript docs/swagger.json -o frontend/src/types/api.ts
     ```
   - Dilarang membuat manual TypeScript interfaces yang rawan *type drift* / mismatch terhadap struct DTO backend Go.

---

## 9. Karakter Desain UI Berstandar Apple Human Interface Guidelines (HIG)

Setiap antarmuka pengguna (Frontend React/Vue) **WAJIB** memiliki karakter modern berkelas dunia mengacu standar Apple:

1. **Kepatuhan Penuh Apple Human Interface Guidelines (HIG)**:
   - Mengacu resmi pada [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) dengan 3 pilar: *Clarity* (konten mudah dipahami), *Deference* (UI tidak mendominasi konten), dan *Depth* (dimensi berlapis yang elegan).
   - Bentuk komponen menggunakan sudut membulat halus (*continuous squircle* `rounded-2xl` / `rounded-3xl` / 14–20px).
   - Micro-interactions halus dengan durasi transisi 150–250ms ease-out dan tactile active response (`active:scale-[0.98]`).

2. **Tipografi San Francisco (SF Pro)**:
   - Primary Font Stack: `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Inter, sans-serif`.
   - Proporsi Kerning & Weight: Heading tegas dengan letter-spacing rapat (`tracking-tight` / `-0.02em` s.d `-0.03em`), subheadline berbobot Medium 500, dan body teks Regular 400 dengan line-height nyaman (`leading-relaxed` / 1.5–1.65).

3. **Penerapan Ruang Kosong (Generous Whitespace & 8pt Grid)**:
   - Layout lega, bersih, dan tidak sesak agar fokus pengguna tertuju penuh pada data & tindakan utama.
   - Spacing konsisten berbasis 8pt grid system: padding kartu `p-6` s.d `p-8`, gap antar section `gap-6` s.d `gap-8`, dan margin halaman yang longgar.
   - Hindari garis pemisah (*dividers*) tebal; gunakan kontras background halus atau border super-tipis transparan (`border border-white/10` atau `border-black/[0.05]`).

4. **Efek Transparansi & Vibrancy / Frosted Glass**:
   - Terapkan efek blur latar belakang (*frosted glass*) pada komponen mengambang (navbar, sidebar, modal sheet, popover, dan floating card):
     ```css
     backdrop-filter: blur(20px) saturate(180%);
     -webkit-backdrop-filter: blur(20px) saturate(180%);
     ```
   - Warna latar semi-transparan: `bg-white/75` s.d `bg-white/85` pada Light Mode, dan `bg-slate-900/80` s.d `bg-black/75` pada Dark Mode.
   - Multi-layer diffused drop shadow: `0 8px 32px 0 rgba(0, 0, 0, 0.08)`.

5. **Pilihan 8 Tema UI Anti-Color Clash (4 Light + 4 Dark)**:
   - Seluruh komponen terikat pada semantic color tokens (`.agents/design-system/tokens/colors.css`) yang menjamin rasio kontras tinggi (**WCAG AA/AAA Ratio ≥ 4.5:1**), anti-teks putih di atas abu-abu terang atau coklat di atas hitam.

6. **Identitas & Branding Resmi Pemkot Yogyakarta (Wajib di Seluruh Aplikasi)**:
   - **Logo di Pojok Kiri Atas (Top-Left) & Sidebar**:
     - Setiap aplikasi **WAJIB** memuat Logo Resmi Vektor Pemerintah Kota Yogyakarta (`assets/logo-jogja.svg` / `.agents/design-system/assets/logo-jogja.svg`) pada pojok kiri atas (di Header Navbar atau Sidebar Navigation).
     - Di samping logo vektor, sertakan **Nama Aplikasi** (dan deskripsi singkat/unit kerja) dengan tipografi SF Pro Semibold yang tegas, proporsional, dan anti-blur (vektor SVG murni menggantikan format gambar raster/jpg/png lama).
     - Ukuran logo standar: tinggi 36px s.d 44px dengan aspect ratio terkunci (`h-9` s.d `h-11`, `w-auto` / `aspect-[184/255]`).
   - **Footer Terstandarisasi**:
     - Setiap halaman aplikasi **WAJIB** menyertakan footer di bagian bawah layout:
       ```html
       <footer class="app-footer">
         <p>&copy; <span id="year">2026</span> Pemerintah Kota Yogyakarta</p>
       </footer>
       ```
     - Format teks wajib: `© [Tahun] Pemerintah Kota Yogyakarta` (menggunakan tahun berjalan dinamis).
