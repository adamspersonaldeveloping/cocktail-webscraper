from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/Users/stein/Desktop/chromedriver'
service = Service(
                executable_path=DRIVER_PATH, 
            )
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://iba-world.com/trinidad-sour/')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('xpath', "/html/body/div[8]/p[2]/button[1]")).click()
    )
    
finally:
    ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').get_attribute('textContent')
    print(ingredients)


# sleep5 = driver.time.sleep(5)
# submit = driver.find_element("xpath", "/html/body/div[8]/p[2]/button[1]").click()
# sleep1 = driver.time.sleep(1)
# ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').element.text

#print(ingredients)
driver.quit()