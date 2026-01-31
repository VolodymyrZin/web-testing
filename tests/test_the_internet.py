from playwright.sync_api import sync_playwright


def test_home_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # Перевіряємо заголовок сторінки
        assert page.title() == "The Internet"

        browser.close()


def test_form_auth_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # Клікаємо на посилання "Form Authentication"
        page.locator("text=Form Authentication").click()

        # Перевіряємо URL нової сторінки
        assert "login" in page.url

        browser.close()

