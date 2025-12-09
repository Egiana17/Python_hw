from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_cheсkout(self):

        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

add_product_to_cart(self, product_name) 
go_to_cart(self)
