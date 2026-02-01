def test_home_title(page):
    # Перевіряємо заголовок сторінки
    assert page.title() == "The Internet"


def test_form_auth_link(page):
    # Клікаємо на посилання "Form Authentication"
    page.locator("text=Form Authentication").click()
    # Перевіряємо URL нової сторінки
    assert "login" in page.url
