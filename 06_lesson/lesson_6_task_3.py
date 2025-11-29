from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(https://bonigarcia.dev/selenium-webdriver-java/loading-images.html)

images = WebDriverWait(driver, timeout: 60).until(
EC.visibility_of_oll_elements_located(By.CLASS_NAME, "loading-images"))


third_image_src = images[2].get_attribute('src')

print(third_image_srcird)

driver.quit()
