import pytest
import allure
from selenium import webdriver
from login_page import LoginPage

@allure.title("Успешный вход в систему")
@allure.description("Тест проверяет вход в систему с валидными данными.")
@allure.feature("Аутентификация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success():
    with allure.step("Инициализация драйвера и открытие страницы авторизации"):
        driver = webdriver.Chrome()
        login_page = LoginPage(driver)

    with allure.step("Открытие страницы входа"):
        login_page.open("https://example.com/login")

    with allure.step("Ввод данных для входа и вход в систему"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверка успешного входа, наличие элемента товаров"):
        # Тут добавьте ассерты или проверяющие шаги
        pass

    driver.quit()
    