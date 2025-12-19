import allure
import pytest

@allure.title("Добавление товара в корзину")
@allure.description("Проверка добавления выбранного товара в корзину.")
@allure.feature("Корзина")
@allure.severity(allure.severity_level.NORMAL)
def test_add_product_to_cart():
    with allure.step("Инициализация драйвера и страницы магазина"):
        driver = webdriver.Chrome()
        page = MainShopPage(driver)

    with allure.step("Ожидание полной загрузки страницы"):
        page.wait_for_page_load()

    with allure.step("Добавление товара 'Sauce Labs Bike Light' в корзину"):
        page.add_product_to_cart("Sauce Labs Bike Light")

    with allure.step("Проверка того, что товар добавлен в корзину"):
        # Здесь можно добавить проверку, например, наличие элемента или счетчика
        pass

    driver.quit()
    