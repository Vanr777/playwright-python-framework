from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage


def test_successful_login(page):
    """
    Skenario: Login dengan kredensial yang benar dari config
    """
    # 1. Inisialisasi Page Object (Halaman Login)
    login_page = LoginPage(page)

    # 2. Buka URL yang diambil dari Config (File .env)
    page.goto(BASE_URL)

    # 3. Jalankan aksi login menggunakan data dari Config (File .env)
    login_page.login(USERNAME, PASSWORD)

    # 4. Validasi (Assertion)
    # Memastikan elemen sukses login muncul (sesuaikan selector dengan website Anda)
    # Contoh untuk HerokuApp:
    assert page.is_visible("div.flash.success")
    assert "You logged into a secure area!" in page.inner_text("div.flash.success")


def test_failed_login(page):
    """
    Skenario: Login gagal dengan password salah
    """
    login_page = LoginPage(page)

    page.goto(BASE_URL)

    # Menggunakan username benar tapi password diketik manual (salah) untuk tes negatif
    login_page.login(USERNAME, "PasswordSalah123!")

    # Memastikan pesan error muncul
    assert page.is_visible("div.flash.error")
    assert "Your password is invalid!" in page.inner_text("div.flash.error")