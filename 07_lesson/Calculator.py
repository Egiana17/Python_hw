# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 30)

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    def wait_for_result(self, expected_text):
        self.waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), expected_text))

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
    