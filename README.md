
# Web Testing Project

Це проєкт для **автоматизованого тестування веб-сайтів** на Python.
Використав **Playwright** та **pytest**, щоб показати базові навички роботи з браузером і тестами.

---

## Що вміє цей проєкт

* Перевіряє заголовок сторінки
* Клікає на посилання і перевіряє, чи відкрилась правильна сторінка
* Показує, як писати прості тести на Python

---

## Використані технології

* Python 3
* [Playwright](https://playwright.dev/python/) — керування браузером
* [pytest](https://docs.pytest.org/) — запуск тестів

---

## Як запустити

1. Клонувати репозиторій:

```bash
git clone https://github.com/VolodymyrZin/web-testing.git
cd web-testing
```

2. Створити та активувати віртуальне середовище:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# або
source .venv/bin/activate   # Linux / Mac
```

3. Встановити залежності:

```bash
pip install -r requirements.txt
```

4. Запустити тести:

```bash
pytest
```

---

## Структура проєкту

```
web-testing/
│
├── tests/
│   ├── test_the_internet.py   
├── requirements.txt      
└── README.md             
```

---

## Приклад тесту

```python
def test_home_title():
    page.goto("https://the-internet.herokuapp.com/")
    assert page.title() == "The Internet"

def test_form_auth_link():
    page.goto("https://the-internet.herokuapp.com/")
    page.locator("text=Form Authentication").click()
    assert "login" in page.url

```


