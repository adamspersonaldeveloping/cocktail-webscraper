from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/Users/stein/Desktop/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://iba-world.com/trinidad-sour/')

#sleep5 = driver.time.sleep(5)
submit = driver.find_element("xpath", "/html/body/div[8]/p[2]/button[1]").click()
#sleep5
ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]')

# h1 = driver.find_element(By.XPATH, '/html/body/h1')
# ingredients = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]')
print(driver.page_source)
driver.quit()