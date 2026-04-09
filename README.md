# Playwright Python Automation Framework

Framework ini dibuat untuk otomasi pengujian UI pada web menggunakan **Playwright** dan **Pytest** dengan pola desain **Page Object Model (POM)**.

## 🚀 Fitur Utama
- **Page Object Model**: Kode modular dan mudah dipelihara.
- **Environment Variables**: Keamanan data menggunakan file `.env`.
- **Parallel Execution**: Menjalankan tes di berbagai browser sekaligus.
- **Headless Mode**: Optimasi kecepatan eksekusi untuk CI/CD.

## 🛠️ Cara Menjalankan Tes

### 1. Running Standard (Headed)
Membuka browser secara visual untuk debugging:
```bash
pytest --headed