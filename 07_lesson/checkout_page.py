from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_id):
        add_button = self.driver.find_element(By.ID, item_id)
        add_button.click()

    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Wait for the cart page to load
        self.waiter.until(EC.presence_of_element_located((By.ID, "checkout")))

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Wait for the checkout form to load
        self.waiter.until(EC.presence_of_element_located((By.ID, "first-name")))

    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)

    def continue_checkout(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        # Wait for the summary page to load
        self.waiter.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    def get_total_amount(self):
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        return total_text.replace("Total: $", "")
