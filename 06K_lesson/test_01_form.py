Import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.adge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumdriverManager
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buttons():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=EdgeService(options))
    driver.get( https://bonigarcia.dev/selenium-webdriver-java/data-types.html)
               
    wait = WebdriverWait(driver, 7)
   
   first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='First name']")))
   first_name.send_keys('Иван')
   first_name.click()

   last_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='Last name']")))
   last_name.send_keys('Петров')
   last_name.click()
    
   adress = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='Adress']")))
   adress.send_keys('Ленина, 55-3')
   adress_name.click()

   mail = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='e-mail']")))
   mail.send_keys('test@skypro.com')
   mail.click()

   phone = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='phone']")))
   phone.send_keys('+7985899998787')
   phone.click()

   city = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='city']")))
   city.send_keys('Москва')
   city.click()

   country = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='country']")))
   country.send_keys('Россия')
   country.click()

   job = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='job position']")))
   job.send_keys('QA')
   job.click()

   company = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='company']")))
   company.send_keys('SkyPro')
   company.click()

   driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
   zip_code wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='zip_code']")))
   background_color = zip_code.volue_of_css_property('background_color')
   assert background_color == "rgba(248, 215, 218, 1)"

   fields = ["first_name", "last_name", "adress", "e-mail", "phone", 
             "city", "country", "job position", "company"]
   for field in fields:
       element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='company']")))
       color = element.value_of_css_property("background-color")
   assert color == "rgba(209, 231, 221, 1)"
   print("\n Все проверки пройдены успешно!")
   driver.quit()
