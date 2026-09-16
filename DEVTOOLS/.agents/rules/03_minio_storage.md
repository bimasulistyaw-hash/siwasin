# 📦 RULE: MINIO OBJECT STORAGE & FILE UPLOAD PROTOCOL

## 1. Larangan Penyimpanan Lokal
- Dilarang keras menyimpan file unggahan pengguna di folder lokal web server (seperti `/uploads`, `/storage`, atau static root).
- Seluruh file statis dan dokumen wajib dialirkan ke **MinIO Object Storage**.

## 2. Validasi Multi-Lapis Sisi Server
1. **Magic Bytes MIME Validation**: Validasi biner header berkas (magic bytes) di backend Go sebelum menerima file, jangan hanya mempercayai ekstensi file dari client.
2. **File Size Limit**: Batasi ukuran maksimal unggahan sesuai tipe file.
3. **Pengacakan Nama Berkas (UUID v4)**:
   ```go
   objectName := fmt.Sprintf("%s/%s_%d%s", module, uuid.New().String(), time.Now().Unix(), ext)
   ```

## 3. Akses Privat via Presigned URL
- Berkas sensitif/dokumen perizinan tidak boleh memiliki URL publik permanen.
- Gunakan **MinIO Presigned GET URL** dengan masa kedaluwarsa singkat (**5–15 menit**) saat pengguna meminta unduhan.
- Aktifkan Server-Side Encryption (SSE-S3) pada bucket MinIO.

## 4. Modul Manajemen Pengaturan Aplikasi (App Configuration)
Sediakan antarmuka konfigurasi terpusat untuk:
- Koneksi Keycloak: `Server URL`, `Realm`, `Client ID`, `Client Secret`, `Redirect URI`.
- Koneksi MinIO: `Endpoint`, `Access Key`, `Secret Key`, `Bucket Name`, `Port`, `UseSSL`.
- Konfigurasi tersimpan terenkripsi di **database PostgreSQL** (bukan di Redis, karena Redis bersifat opsional).

---

## 5. Kebijakan Offline-First: Penyimpanan Gambar & Dummy Data di Lokal / MinIO

Aplikasi yang dihasilkan **WAJIB dapat dijalankan secara mandiri (offline/isolated)** tanpa ketergantungan koneksi internet publik:

1. **Larangan Keras URL Gambar Eksternal dari Internet**:
   - **DILARANG** menggunakan URL gambar dari internet seperti `https://picsum.photos`, `https://images.unsplash.com`, `https://via.placeholder.com`, `https://placehold.co`, `https://api.dicebear.com`, Cloudinary, Imgur, LoremFlickr, atau CDN eksternal lainnya.
   - Semua aset visual (logo, icon SVG, avatar placeholder, thumbnail, banner, ilustrasi) **WAJIB** disimpan secara lokal di dalam folder proyek frontend (`frontend/public/images/`, `frontend/src/assets/`) atau menggunakan kode SVG lokal / data URI Base64.

2. **Penyimpanan Gambar Sampel / Media Pengguna ke MinIO Lokal**:
   - Jika aplikasi membutuhkan gambar profil pengguna, dokumen lampiran, atau foto produk dalam status terisi (seeding), file aset tersebut **WAJIB disemai (seeded)** langsung ke dalam bucket **MinIO lokal** (`http://localhost:9000` / container `minio`) saat inisialisasi lingkungan.
   - Dilarang membuat link database yang mengarah ke domain luar internet.

3. **Sentralisasi Dummy Data (Mock Data) di Repositori Lokal**:
   - Seluruh data awal/dummy (Master Data, User Seed, Transaksi Contoh) wajib disediakan dalam bentuk file lokal:
     - **Database Seed SQL**: `db/seeds/01_seed_data.sql` atau file migration seeder.
     - **Frontend Mock Fixtures**: `frontend/src/mocks/` atau `frontend/src/data/`.
   - **DILARANG** memanggil mock API online (seperti JSONPlaceholder, FakeStoreAPI, MockAPI.io, Reqres.in).
