from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
  driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID,"ajaxButton")
button.click()

wait = WebDriverWait(driver, 10)

wait.until(
   EC.text_to_be_present_in_element((By.ID, "content"),"Data loaded with AJAX")
)
content = driver.find_element(By. ID, "content")
print(content.text)

except Exception as e:
print(f"Произошла ошибка: {e}")
try:
        driver.get("http://uitestingplayground.com/ajax")
finally:
        driver.quit()
