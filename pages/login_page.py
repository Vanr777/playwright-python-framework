class LoginPage:
    def __init__(self, page):
        self.page = page
        # Ini namanya Locator (Alamat elemen di web)
        self._username = page.locator("#username")
        self._password = page.locator("#password")
        self._login_btn = page.locator("button[type='submit']")
        self._message = page.locator("#flash")

    def navigate(self, url):
        self.page.goto(url)

    def login(self, user, pwd):
        self._username.fill(user)
        self._password.fill(pwd)
        self._login_btn.click()

    def get_message(self):
        return self._message.inner_text()