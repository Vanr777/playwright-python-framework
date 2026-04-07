from pages.login_page import LoginPage


def test_successful_login(page):
    # 1. Inisialisasi Page Object
    login_page = LoginPage(page)

    # 2. Buka halaman login
    login_page.navigate("https://the-internet.herokuapp.com/login")

    # 3. Masukkan username & password (kredensial contoh)
    login_page.login("tomsmith", "SuperSecretPassword!")

    # 4. Ambil pesan yang muncul di web
    pesan = login_page.get_message()

    # 5. Cek apakah ada tulisan 'You logged into a secure area!'
    # Ini namanya Assertion (penentu lulus/gagalnya test)
    assert "You logged into a secure area!" in pesan