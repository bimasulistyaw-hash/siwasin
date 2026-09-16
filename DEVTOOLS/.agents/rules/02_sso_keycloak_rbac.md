# 🔑 RULE: SSO JSS KEYCLOAK & 4-ROLE RBAC

## 1. Otentikasi Terpusat SSO JSS Keycloak & Sandbox 4 Dummy Users
1. **Produksi**: Wajib menggunakan OpenID Connect (OIDC) / OAuth2 via Keycloak JSS.
2. **JWT Signature Verification**: Setiap HTTP request wajib divalidasi tanda tangan kriptografisnya via JWKS Keycloak dan dicek masa aktifnya di middleware Go (`internal/delivery/http/middleware`).
3. **Halaman Login Terpisah (`/login`)**:
   - Sistem menyediakan halaman login tersendiri terpisah dari layout aplikasi utama.
4. **4 Role Dummy Users untuk Testing Sandbox (`APP_ENV=testing` & `ENABLE_TEST_AUTH=true`)**:
   - Disediakan minimal 4 user dummy bawaan (1 per role) untuk mempermudah pengujian:
     - `Superadmin`: `superadmin@jogjakota.go.id` (Full Access)
     - `Pengawas`: `pengawas@jogjakota.go.id` (Read-Only & Audit Log)
     - `Admin`: `admin@jogjakota.go.id` (User & App Settings)
     - `Operator`: `operator@jogjakota.go.id` (Daily Business Operations)
   - Dilengkapi tombol *1-Click Quick Login* pada halaman login sandbox.
   - Dilarang keras aktif atau memiliki backdoor di lingkungan produksi (`APP_ENV=production`).

## 2. 4 Hierarki Role RBAC Keycloak
Hak akses dievaluasi dari claim token Keycloak (`realm_access.roles` / `resource_access`):
- **`Superadmin`**: Full access ke seluruh modul, konfigurasi aplikasi, dan data.
- **`Pengawas`**: Hak akses **Read-Only** setara Superadmin. Hanya boleh request method `GET` (dashboard analitik, audit log, laporan). Ditolak (HTTP 403) jika mencoba `POST`, `PUT`, `DELETE`.
- **`Admin`**: Manajemen User (RBAC mapping) dan Pengaturan Koneksi Aplikasi.
- **`Operator`**: Mengoperasionalkan transaksi harian dan modul bisnis spesifik.

## 3. 5 Modul Pengaturan Sistem (System Settings) Wajib

Setiap aplikasi wajib menyediakan antarmuka (UI) dan API terpadu untuk 5 modul pengaturan sistem:

1. **Manajemen Pengguna (User Management)**:
   - **Form Tambah/Edit Pengguna**:
     - `ID JSS *`: Input text (Wajib diisi).
     - `Nama Lengkap`: Input text (Terisi otomatis saat ID JSS diverifikasi via SSO JSS / disabled/read-only).
     - `Role Pengguna *`: Dropdown selection (Wajib memilih salah satu role aktif).
     - Tombol `Batal` & `Simpan`.
   - **Daftar Pengguna**: Tabel/list interaktif menampilkan Avatar, ID JSS, Nama Lengkap, Role Badge, Status Aktif, serta tombol aksi `Edit` dan `Hapus/Nonaktifkan`.

2. **Manajemen Role (Role Management)**:
   - Menambah, mengubah nama/deskripsi, dan mengurangi role dalam sistem.
   - **Aturan Bisnis Integritas**: Role yang masih terikat dengan pengguna aktif **DILARANG DIHAPUS** (*Protected Role Deletion* — tolak dengan pesan: *"Role sedang digunakan oleh X pengguna aktif"*).

3. **Manajemen Hak Akses (Module Permission Matrix)**:
   - Matriks kontrol hak akses dinamis per-role terhadap seluruh Menu & Sub-menu.
   - **4 Aksi Standar per Modul**: `Lihat (View)`, `Tambah (Create)`, `Ubah (Update)`, dan `Hapus (Delete)`.
   - Toggle switch interaktif per-aksi di setiap baris sub-menu, dilengkapi master switch toggle per-kategori grup menu dan tombol `Simpan Perubahan`.

4. **Manajemen Menu Sidebar (Sidebar Navigation Management)**:
   - Pengelompokan grup header (Category/Section, misal: `DASHBOARD`, `MASTER DATA`, `TRANSAKSI`, `SYSTEM CONFIG`, `DEBUG`).
   - Manajemen struktur pohon menu (Menu Utama, Sub-Menu bersarang), rute URL, ikon SVG, badge status, serta toggle aktif/nonaktif.
   - **Pengurutan Posisi Menu (Drag-and-Drop Reorder)**: Pengurutan posisi menu **WAJIB menggunakan metode interaktif menggeser / drag-and-drop / drag-to-reorder**, BUKAN dengan memasukkan nomor urut menu secara manual.

5. **Manajemen Tema dan Warna Tema (Theme & Color Scheme Management)**:
   - Pengaturan 8 tema terstandarisasi (4 Light + 4 Dark Themes, WCAG AA/AAA Ratio ≥ 4.5:1, Anti-Color Clash).
   - Mode switcher: Light / Dark / Auto OS, live preview color swatch, dan penyimpanan preferensi pengguna via `localStorage` / user profile.

## 4. Fitur Wajib Log Aktivitas Pengguna (User Activity Log / Audit Trail)

Setiap aplikasi wajib mengimplementasikan pencatatan riwayat audit aktivitas pengguna secara otomatis:
1. **Atribut Rekam Jejak**: User ID (JSS), Nama Pengguna, Role, HTTP Method (GET/POST/PUT/DELETE), Modul/Endpoint Path, Alamat IP, User-Agent, Status Respon (200/400/403/500), Payload/Deskripsi Perubahan, dan Timestamp presisi.
2. **Matriks Hak Akses Eksklusif**:
   - **`Superadmin`**: Memiliki izin penuh melihat seluruh log aktivitas dan melakukan ekspor laporan audit.
   - **`Pengawas`**: Memiliki izin **Read-Only** untuk memantau, mencari, memfilter, dan melihat detail log aktivitas (dilarang menghapus data log).
   - **`Admin` & `Operator`**: **DIBLOKIR TOTAL** dari menu dan endpoint log aktivitas. Request langsung ke API audit log wajib ditolak middleware dengan respon **`HTTP 403 Forbidden`**.
