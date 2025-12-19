from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CartPage:
    """
    Страница корзины, реализующая взаимодействие с элементами на странице.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: Веб-драйвер Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по кнопке 'Перейти к оформлению заказа'")
    def click_checkout(self) -> None:
        """
        Кликает на кнопку с ID 'checkout' и ожидает загрузки страницы.

        :return: None
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        self.wait_for_page_load()

    @allure.step("Ожидание загрузки содержимого корзины")
    def wait_for_page_load(self) -> None:
        """
        Ожидает появления всех элементов с ID 'cart_contents' для загрузки страницы.

        :return: None
        """
        self.wait.until(
            EC.presence_of_all_elements_located((By.ID, "cart_contents"))
        )
