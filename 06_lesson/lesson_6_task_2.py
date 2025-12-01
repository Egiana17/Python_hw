from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("Skypro")

driver.find_element(By.CSS_SELECTOR,"#updatingButton").click()

wait = WebDriverWait(driver, 10)
updated_button = wait.until(
    EC.text_to_be_present_in_element((BY.CSS_SELECTOR, "#updatingButton"), "Skypro")
)

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
txt = content.text

print(txt)

driver.quit()
