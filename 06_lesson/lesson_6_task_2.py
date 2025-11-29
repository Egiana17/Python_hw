from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=Chromeservice(ChromeDriverManager().install()))

driver.get(http://uitestingplayground.com/textinput)

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.sens_keys("Skypro")

driver.find_element(By.CSS_SELECTOR,"#updatingButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
txt = content.find_element(By.TAG_NAME,"#updatingButton" ).text

print(txt)

driver.quit()
