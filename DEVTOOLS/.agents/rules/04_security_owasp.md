# 🛡️ RULE: OWASP TOP 10 COMPLIANCE & SECURITY GATE

## 1. Perlindungan OWASP Top 10
- **A01 Broken Access Control**: Enforce 4 role Keycloak, proteksi Pengawas Read-Only, auto logout idle session (5–10 menit), single active session.
- **A02 Cryptographic Failures**: Wajib SSL/HTTPS, validasi tanda tangan JWT OIDC, enkripsi MinIO SSE-S3.
- **A03 Injection**: Parameterized SQL query wajib (`$1, $2, ...`), sanitasi input, validasi magic bytes.
- **A04 Insecure Design**: Rate limiting wajib ada — gunakan **Redis Token Bucket** *(jika Redis aktif)* atau **in-memory rate limiter** (`golang.org/x/time/rate`) per-IP *(jika Redis tidak digunakan)*. Isolasi auth manual di sandbox testing saja.
- **A05 Security Misconfiguration**: Pasang Security Headers (`Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Strict-Transport-Security`), matikan directory listing.
- **A06 Vulnerable Components**: 0 CVE High/Critical pada Go dependencies dan npm packages.
- **A07 Identification & Auth**: Integrasi SSO JSS Keycloak.
- **A08 Software & Data Integrity**: File upload via MinIO UUID v4 & Presigned URL.
- **A09 Security Logging**: Structured logger (Zap) tanpa pernah mencatat kredensial, token, atau secret ke log.
- **A10 SSRF**: Validasi outbound URL dan whitelist internal service endpoints.

## 2. Automated SAST, DAST, & Security Gate
- Backend Go: Jalankan `gosec ./...` dan `semgrep --config p/owasp-top-10`.
- Dependency Audit: Jalankan `govulncheck ./...` (Go) dan `npm audit` (Frontend).
- DAST & Penetration Testing: Mengacu pada OWASP Top 10, OWASP API Security Top 10, WSTG v4.2, ASVS v4.0, NIST SP 800-115, PTES, OSSTMM 3, CIS Controls v8, dan CVSS v3.1/v4.0.
- **Kewajiban Bukti Visual (Screenshot Evidence Pentest)**:
  - Setiap temuan kerentanan (*Proof of Concept*), pengujian kontrol keamanan (SAST scan, SCA audit, validasi 4-Role RBAC, rate limiting, MinIO magic bytes check, HTTP security headers) **WAJIB** menyertakan screenshot dari tampilan pengujian atau tampilan hasil pengujiannya (terminal output, network tab/response, dialog error, atau bypass evidence).
  - Aset screenshot pentest disimpan di `docs/screenshots/sec-[id]-[deskripsi].png` dan disematkan langsung pada laporan keamanan.
- **Vulnerability Security Gate**: Jika terdeteksi celah tingkat **Medium, High, atau Critical**, build **DIBATALKAN (FAILED)** dan rilis diblokir hingga diperbaiki (Status Retest: RESOLVED).
- Seluruh output hasil pengujian wajib disimpan di folder `docs/`: `docs/SECURITY_REPORT.md`, `docs/Dokumen_Laporan_Pentest_Resmi.docx` (lengkap dengan screenshot bukti pengujian), dan `docs/WSTG_AUDIT_CHECKLIST.md`.
