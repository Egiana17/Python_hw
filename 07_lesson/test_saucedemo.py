from selenium import webdriver
from login_page import LoginPage
from checkout_page import CheckoutPage


def test_saucedemo_checkout():
    driver = webdriver.Firefox()
    try:
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.open("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Add items to cart
        checkout_page = CheckoutPage(driver)
        checkout_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
        checkout_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        checkout_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")

        # Step 3: Proceed to checkout
        checkout_page.go_to_cart()
        checkout_page.proceed_to_checkout()

        # Step 4: Fill checkout form
        checkout_page.fill_checkout_form("Иван", "Петров", "123456")
        checkout_page.continue_checkout()

        # Step 5: Verify total amount
        total_amount = checkout_page.get_total_amount()
        expected_total = "58.29"
        assert total_amount == expected_total, f"Expected: ${expected_total}, Got: ${total_amount}"

        print(f"Test passed! Total amount: ${total_amount}")
    finally:
        driver.quit()
        