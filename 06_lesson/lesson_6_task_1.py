from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID,"ajaxButton")

button.click()

wait = WebDriverWait(driver, 20, poll_frequency=0.1)
try:
    txt = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    
    if "Data loaded with AJAX get request." in txt.text:
        print("AJAX запрос успешно выполнен!")
    else:
        print("Ошибка загрузки данных.")
except Exception as e:
    try:
     driver.get("http://uitestingplayground.com/ajax")
    finally:
    driver.quit()
