from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
search_field = "#username"
search_input_username_username = driver.find_element(By.XPATH, '//*[@id="username"]')
search_input_username_username.send_keys("tomsmith")
search_input_password = driver.find_element(By.XPATH, '//*[@id="password"]')
search_input_password.send_keys("SuperSecretPassword!")
search_input = driver.find_element(By.XPATH, '//*[@id="login"]/button')
search_input.click()

element = driver.find_element`find_element(By.ID, ...)`
print(element.text)
driver.quit()
sleep(10)
