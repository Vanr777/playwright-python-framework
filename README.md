# Playwright Python Automation Framework

Framework ini dibuat untuk otomasi pengujian UI pada web menggunakan **Playwright** dan **Pytest** dengan pola desain **Page Object Model (POM)**.

## 🚀 Fitur Utama
- **Page Object Model**: Kode modular dan mudah dipelihara.
- **Environment Variables**: Keamanan data menggunakan file `.env`.
- **Parallel Execution**: Menjalankan tes di berbagai browser sekaligus.
- **Headless Mode**: Optimasi kecepatan eksekusi untuk CI/CD.

## 🛠️ Persiapan & Cara Menjalankan Tes

### 1. Install Library
Pastikan kamu sudah menginstal semua library yang dibutuhkan:
```bash
pip install -r requirements.txt
```
### 2. Install Browser Playwright
Lakukan instalasi browser binary agar Playwright bisa berjalan:
```bash
playwright install
````
### 3.**Runing Standard (Headed)**
Menjalankan automation dengan membuka jendela
browser secara visual:
```bash 
pytest --headed
````
### 4.**Running Parallel & Headles
Menjalankan tes secara parallel tanpa membuka
jendela browser:
```bash
pytest -n 2
```

