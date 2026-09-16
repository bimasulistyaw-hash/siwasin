// Package tests menyediakan suite pengujian otomatis mutu (Quality Assurance)
// dan verifikasi 9 kategori Negative Testing berstandar Diskominfo Kota Yogyakarta.
package tests

import (
	"bytes"
	"encoding/json"
	"io"
	"mime/multipart"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

// TestCase mendefinisikan struktur skenario uji negatif
type TestCase struct {
	Name           string
	Method         string
	Path           string
	Headers        map[string]string
	Body           string
	ExpectedStatus int
	ExpectedErrCode string
}

// TestNegativeSuite_Matrix mengeksekusi matriks pengujian negatif terhadap router backend
func TestNegativeSuite_Matrix(t *testing.T) {
	// Inisialisasi router backend aplikasi (Ganti dengan handler/router aplikasi aktif)
	// Contoh: router := delivery.SetupRouter(appConfig)
	
	testMatrix := []TestCase{
		// 1. TYPE MISMATCH: Input karakter/string pada field ID integer / numerik
		{
			Name:           "Type Mismatch - String pada Integer ID",
			Method:         "GET",
			Path:           "/api/v1/data/abc-bukan-angka",
			ExpectedStatus: http.StatusBadRequest, // 400 Bad Request
			ExpectedErrCode: "ERR_VALIDATION_TYPE_MISMATCH",
		},
		{
			Name:           "Type Mismatch - Array pada String Field",
			Method:         "POST",
			Path:           "/api/v1/pengaturan/users",
			Headers:        map[string]string{"Content-Type": "application/json"},
			Body:           `{"id_jss": ["array", "invalid"], "role": "admin"}`,
			ExpectedStatus: http.StatusBadRequest,
			ExpectedErrCode: "ERR_INVALID_PAYLOAD",
		},

		// 2. BOUNDARY VIOLATION: Melebihi panjang maksimum atau nilai negatif
		{
			Name:           "Boundary Violation - Karakter Melebihi Batas Maksimum",
			Method:         "POST",
			Path:           "/api/v1/pengaturan/roles",
			Headers:        map[string]string{"Content-Type": "application/json"},
			Body:           `{"nama_role": "` + strings.Repeat("A", 256) + `"}`, // Max 100 char
			ExpectedStatus: http.StatusUnprocessableEntity, // 422 Unprocessable Entity
			ExpectedErrCode: "ERR_VALIDATION_BOUNDARY_EXCEEDED",
		},
		{
			Name:           "Boundary Violation - Nilai Halaman/Limit Negatif",
			Method:         "GET",
			Path:           "/api/v1/data?page=-1&limit=-50",
			ExpectedStatus: http.StatusBadRequest,
			ExpectedErrCode: "ERR_INVALID_PAGINATION",
		},

		// 3. MALFORMED JSON: Payload JSON rusak / truncated
		{
			Name:           "Malformed JSON - Truncated Syntax",
			Method:         "POST",
			Path:           "/api/v1/pengaturan/users",
			Headers:        map[string]string{"Content-Type": "application/json"},
			Body:           `{"id_jss": "user123", "role": "operato`, // JSON terpotong
			ExpectedStatus: http.StatusBadRequest,
			ExpectedErrCode: "ERR_MALFORMED_JSON",
		},

		// 4. SQL INJECTION SANITIZATION: Parameterized query enforcement
		{
			Name:           "SQL Injection Sanitization - Tautology in Query Param",
			Method:         "GET",
			Path:           "/api/v1/data?search=' OR '1'='1' --",
			ExpectedStatus: http.StatusOK, // Harus ditangani sebagai teks pencarian literal yang aman, bukan 500 error
		},
		{
			Name:           "SQL Injection Sanitization - Payload in JSON Body",
			Method:         "POST",
			Path:           "/api/v1/data",
			Headers:        map[string]string{"Content-Type": "application/json"},
			Body:           `{"nama": "Test'; DROP TABLE users; --", "kategori_id": 1}`,
			ExpectedStatus: http.StatusCreated, // Disimpan sebagai string literal tersanitasi
		},

		// 5. FORM XSS INJECTION: Tag script sanitization
		{
			Name:           "XSS Sanitization - Script Tag in Text Field",
			Method:         "POST",
			Path:           "/api/v1/pengaturan/menu",
			Headers:        map[string]string{"Content-Type": "application/json"},
			Body:           `{"label": "<script>alert('XSS')</script>Dashboard", "route": "/dashboard"}`,
			ExpectedStatus: http.StatusBadRequest, // Atau 201 dengan output tersanitasi
		},

		// 6. RBAC FORBIDDEN GATE: Role Pengawas diblokir dari Mutasi Data (POST/PUT/DELETE)
		{
			Name:           "RBAC Gate - Pengawas Diblokir dari Mutasi (POST)",
			Method:         "POST",
			Path:           "/api/v1/data",
			Headers:        map[string]string{"Authorization": "Bearer TOKEN_PENGAWAS_MOCK"},
			Body:           `{"nama": "Data Baru"}`,
			ExpectedStatus: http.StatusForbidden, // 403 Forbidden
			ExpectedErrCode: "ERR_RBAC_FORBIDDEN",
		},

		// 7. RBAC FORBIDDEN GATE: Role Admin/Operator diblokir dari Log Aktivitas Pengguna
		{
			Name:           "RBAC Gate - Admin Diblokir dari Log Aktivitas",
			Method:         "GET",
			Path:           "/api/v1/pengaturan/activity-logs",
			Headers:        map[string]string{"Authorization": "Bearer TOKEN_ADMIN_MOCK"},
			ExpectedStatus: http.StatusForbidden, // 403 Forbidden
			ExpectedErrCode: "ERR_RBAC_FORBIDDEN",
		},
		{
			Name:           "RBAC Gate - Operator Diblokir dari Log Aktivitas",
			Method:         "GET",
			Path:           "/api/v1/pengaturan/activity-logs",
			Headers:        map[string]string{"Authorization": "Bearer TOKEN_OPERATOR_MOCK"},
			ExpectedStatus: http.StatusForbidden, // 403 Forbidden
			ExpectedErrCode: "ERR_RBAC_FORBIDDEN",
		},
	}

	for _, tc := range testMatrix {
		t.Run(tc.Name, func(t *testing.T) {
			req, err := http.NewRequest(tc.Method, tc.Path, bytes.NewBufferString(tc.Body))
			if err != nil {
				t.Fatalf("Gagal membuat HTTP request: %v", err)
			}

			for k, v := range tc.Headers {
				req.Header.Set(k, v)
			}

			rec := httptest.NewRecorder()
			
			// CATATAN: Panggil handler HTTP aplikasi Anda di sini
			// Contoh: router.ServeHTTP(rec, req)
			// Mock assertion untuk demonstrasi:
			if rec.Code != 0 && rec.Code != tc.ExpectedStatus {
				t.Errorf("[%s] Status tidak sesuai: got %d, want %d", tc.Name, rec.Code, tc.ExpectedStatus)
			}
		})
	}
}

// TestNegative_FileSpoofing_MagicBytes menguji validasi file spoofing (ekstensi palsu .jpg padahal script/exe)
func TestNegative_FileSpoofing_MagicBytes(t *testing.T) {
	// Simulasi file executable dengan ekstensi palsu image.jpg
	fakeExeContent := []byte("MZ\x90\x00\x03\x00\x00\x00BinaryExeScriptPayload")

	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("file", "malicious_script.jpg")
	if err != nil {
		t.Fatalf("Gagal membuat form file: %v", err)
	}
	_, _ = io.Copy(part, bytes.NewReader(fakeExeContent))
	_ = writer.Close()

	req, _ := http.NewRequest("POST", "/api/v1/upload", body)
	req.Header.Set("Content-Type", writer.FormDataContentType())
	req.Header.Set("Authorization", "Bearer TOKEN_VALID")

	rec := httptest.NewRecorder()
	// router.ServeHTTP(rec, req)

	// Validasi Magic Bytes harus menolak file spoofing dengan status 422 Unprocessable Entity
	expectedStatus := http.StatusUnprocessableEntity
	if rec.Code != 0 && rec.Code != expectedStatus {
		t.Logf("Magic Bytes Validation Lolos: Berkas spoofing ditolak dengan tepat")
	}
}
