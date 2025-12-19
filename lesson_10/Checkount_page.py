from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CheckoutPage:
    """
    Страница оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: Веб-драйвер Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Добавление товара с ID '{item_id}' в корзину")
    def add_item_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по идентификатору кнопки.

        :param item_id: Идентификатор элемента для добавления товара.
        :type item_id: str
        :return: None
        """
        add_button = self.driver.find_element(By.ID, item_id)
        add_button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины, кликая по иконке.

        :return: None
        """
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        self.waiter.until(EC.presence_of_element_located((By.ID, "checkout")))

    @allure.step("Переход к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """
        Переходит к странице оформления заказа, нажимая кнопку.

        :return: None
        """
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        self.waiter.until(EC.presence_of_element_located((By.ID, "first-name")))

    @allure.step("Заполнение формы оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет поля формы оформления заказа.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Продолжение оформления заказа")
    def continue_checkout(self) -> None:
        """
        Нажимает кнопку продолжить и ожидает страницу с итоговой суммой.

        :return: None
        """
        self.driver.find_element(By.ID, "continue").click()
        self.waiter.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    @allure.step("Получение итоговой суммы заказа")
    def get_total_amount(self) -> str:
        """
        Возвращает строку с общей суммой заказа.

        :return: Общая сумма в виде строки.
        :rtype: str
        """
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        return total_text.replace("Total: $", "")
