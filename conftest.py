import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    ---Добавляем параметр ---language для выбора языка
    parser.addoption("--language", action="store", default="en", help="Choose language: en, fr, es, etc.")

@pytest.fixture(scope="function")
def browser(request):
   ---Настраиваем браузер с нужным языком
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
