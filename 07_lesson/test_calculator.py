# test_calculator.py
from selenium import webdriver
from Calculator import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    try:
        calculator = CalculatorPage(driver)
        calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator.set_delay("1")

        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

        calculator.wait_for_result("15")
        result = calculator.get_result()

        assert result == "15", f"Expected result to be 15 but got {result}"
    finally:
        driver.quit()
