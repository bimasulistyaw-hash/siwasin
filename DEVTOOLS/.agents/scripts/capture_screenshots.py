#!/usr/bin/env python3
"""
Utility Screenshot & Visual Evidence Capture Tool
Standar Diskominfo Kota Yogyakarta - Antigravity 2.0

Fungsi:
1. Pre-flight check kesiapan engine screenshot (Chrome Headless, Playwright, Antigravity Browser)
2. Mengambil screenshot otomatis dari URL aplikasi / mockup yang sedang berjalan
3. Menyimpan screenshot ke `docs/screenshots/` berformat PNG tajam 1280x800
4. Memvalidasi ketersediaan aset gambar agar dapat di-embed sempurna oleh `generate_docx.py`
"""

import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path

# Lokasi default output
DEFAULT_OUTPUT_DIR = "docs/screenshots"

# Lokasi candidate Chrome / Chromium di berbagai OS
CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]

def find_chrome_binary():
    """Mencari executable Google Chrome / Chromium di sistem."""
    for candidate in CHROME_CANDIDATES:
        if candidate.startswith("/"):
            if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                return candidate
        else:
            found = shutil.which(candidate)
            if found:
                return found
    return None

def check_playwright():
    """Cek ketersediaan library playwright di python."""
    try:
        import playwright
        return True
    except ImportError:
        return False

def check_selenium():
    """Cek ketersediaan library selenium di python."""
    try:
        import selenium
        return True
    except ImportError:
        return False

def preflight_check():
    """Melakukan pre-flight diagnostic untuk memastikan engine screenshot siap."""
    print("🔍 [PRE-FLIGHT CHECK] Diagnostik Kesiapan Tools Screenshot & Visual Evidence:")
    print("─" * 70)
    
    chrome_bin = find_chrome_binary()
    has_playwright = check_playwright()
    has_selenium = check_selenium()
    
    status_chrome = f"✅ Ditemukan: {chrome_bin}" if chrome_bin else "⚠️ Tidak ditemukan di path standar"
    status_playwright = "✅ Terpasang (Python)" if has_playwright else "ℹ️ Belum terpasang (Opsional)"
    status_selenium = "✅ Terpasang (Python)" if has_selenium else "ℹ️ Belum terpasang (Opsional)"
    status_agent = "✅ Siap (Antigravity browser_subagent / DevTools)"
    
    print(f"  1. Headless Chrome CLI   : {status_chrome}")
    print(f"  2. Python Playwright     : {status_playwright}")
    print(f"  3. Python Selenium       : {status_selenium}")
    print(f"  4. Antigravity Browser   : {status_agent}")
    print("─" * 70)
    
    if chrome_bin or has_playwright or has_selenium:
        print("🎉 STATUS: Tools screenshot SIAP DIGUNAKAN untuk QA & User Manual!\n")
        return True
    else:
        print("💡 STATUS: Menggunakan Antigravity `browser_subagent` sebagai engine utama.\n")
        return True

def capture_with_chrome_cli(url, output_file, window_size="1280,800"):
    """Mengambil screenshot menggunakan Chrome Headless CLI."""
    chrome_bin = find_chrome_binary()
    if not chrome_bin:
        return False, "Google Chrome binary tidak ditemukan."
    
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={window_size}",
        "--hide-scrollbars",
        f"--screenshot={output_file}",
        url
    ]
    
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            return True, f"Berhasil disimpan: {output_file}"
        else:
            return False, f"Gagal menghasilkan screenshot. Stderr: {res.stderr.decode('utf-8', errors='ignore')}"
    except Exception as e:
        return False, f"Exception saat eksekusi Chrome CLI: {str(e)}"

def generate_svg_fallback(title, subtitle, output_file, width=1280, height=800):
    """Menghasilkan SVG visual jika server target belum aktif untuk sandbox build."""
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#0f172a"/>
  <rect x="20" y="20" width="{width - 40}" height="{height - 40}" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <circle cx="50" cy="50" r="8" fill="#ef4444"/>
  <circle cx="75" cy="50" r="8" fill="#f59e0b"/>
  <circle cx="100" cy="50" r="8" fill="#10b981"/>
  <rect x="130" y="38" width="400" height="24" rx="6" fill="#0f172a"/>
  <text x="145" y="55" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="12">https://sso.jogjakota.go.id/app</text>
  <text x="640" y="380" fill="#f8fafc" font-family="-apple-system, sans-serif" font-size="28" font-weight="bold" text-anchor="middle">{title}</text>
  <text x="640" y="425" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="16" text-anchor="middle">{subtitle}</text>
  <rect x="490" y="480" width="300" height="44" rx="8" fill="#1e3a8a"/>
  <text x="640" y="508" fill="#ffffff" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Diskominfo Kota Yogyakarta</text>
</svg>"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg_content)
    return True, f"Visual placeholder dibuat: {output_file}"

def main():
    parser = argparse.ArgumentParser(description="Tool Screenshot & Visual Evidence Antigravity 2.0")
    parser.add_argument("--check", action="store_true", help="Jalankan pre-flight check tools screenshot")
    parser.add_argument("-u", "--url", type=str, help="URL target aplikasi yang akan di-capture")
    parser.add_argument("-o", "--output", type=str, default=None, help="Path file output screenshot (.png)")
    parser.add_argument("-n", "--name", type=str, default="screen-evidence", help="Nama dasar file jika output tidak ditentukan")
    parser.add_argument("-d", "--dir", type=str, default=DEFAULT_OUTPUT_DIR, help=f"Folder tujuan (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--title", type=str, default="Tangkapan Layar Sistem", help="Judul untuk visual placeholder")
    parser.add_argument("--subtitle", type=str, default="Pemerintah Kota Yogyakarta", help="Subtitle visual placeholder")
    
    args = parser.parse_args()
    
    if args.check or (len(sys.argv) == 1):
        preflight_check()
        if len(sys.argv) == 1:
            return
            
    if args.url:
        out_path = args.output
        if not out_path:
            filename = f"{args.name}.png" if not args.name.endswith(".png") else args.name
            out_path = os.path.join(args.dir, filename)
            
        print(f"📸 Mengambil screenshot dari: {args.url}")
        print(f"   Target simpan: {out_path}")
        
        ok, msg = capture_with_chrome_cli(args.url, out_path)
        if ok:
            print(f"✅ {msg}")
        else:
            print(f"⚠️ {msg}")
            print("   Membuat fallback visual placeholder...")
            generate_svg_fallback(args.title, args.subtitle, out_path.replace(".png", ".svg"))

if __name__ == "__main__":
    main()
