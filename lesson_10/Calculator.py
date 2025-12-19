from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalculatorPage:
    """
    Класс для взаимодействия с страницей калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализация объекта страницы калькулятора.

        :param driver: webdriver, экземпляр Selenium WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 30)

    @allure.step("Открытие страницы по URL: {url}")
    def open(self, url: str) -> None:
        """
        Открывает страницу калькулятора по указанному URL.

        :param url: URL страницы
        :type url: str
        :return: None
        """
        self.driver.get(url)
        self.driver.maximize_window()

    @allure.step("Установка задержки: {delay}")
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку ввода.

        :param delay: Значение задержки (строка)
        :type delay: str
        :return: None
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Клик по кнопке с текстом: {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку по её тексту.

        :param button_text: Текст кнопки
        :type button_text: str
        :return: None
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    @allure.step("Ожидание появления текста: {expected_text}")
    def wait_for_result(self, expected_text: str) -> None:
        """
        Ждет, пока текст `expected_text` появится в элементе с селектором '.screen'.

        :param expected_text: Ожидаемый текст
        :type expected_text: str
        :return: None
        """
        self.waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), expected_text))

    @allure.step("Получение текста результата")
    def get_result(self) -> str:
        """
        Получает текст из элемента с селектором '.screen'.

        :return: Текст результата
        :rtype: str
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text


import pytest
import allure
from calculator_page import CalculatorPage

@allure.title("Тест проверки сложения")
@allure.description("Проверка правильности выполнения операции сложения в калькуляторе.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_addition():
    # Предполагается, что драйвер и URL передаются или создаются заранее
    driver = ...  # Инициализация WebDriver
    page = CalculatorPage(driver)
    with allure.step("Открываем страницу калькулятора"):
        page.open("http://example.com")
    with allure.step("Вводим задержку '1'"):
        page.set_delay("1")
    with allure.step("Кликаем кнопку '+'"):
        page.click_button("+")
    with allure.step("Проверяем результат равен '3'"):
        page.wait_for_result("3")
        result = page.get_result()
        with allure.step(f"Проверяем, что результат '{result}' равен '3'"):
            assert result == "3"
    driver.quit()
