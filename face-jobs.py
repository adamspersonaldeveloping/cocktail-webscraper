from selenium import webdriver
import time

import pandas as pd

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
urlList = ['https://iba-world.com/americano/', 'https://iba-world.com/alexander/', 'https://iba-world.com/trinidad-sour/']
cocktailList = []

for val in urlList:
    def get_cocktail_info(val):

        driver.get(val)




        cocktailName = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[1]/div/div/h1').get_attribute('textContent')

        ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').get_attribute('textContent')

        method = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[2]').get_attribute('textContent')
    
        garnish = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[3]').get_attribute('textContent')

        importance = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/p/a[2]').get_attribute('textContent')

        cocktail = {
            'cocktailName': cocktailName,
            'ingredients': ingredients,
            'method': method,
            'garnish': garnish,
            'importance': importance,
            'ibaCocktail': 'true',

        }

        return cocktailList.append(cocktail)

print(cocktailList)
data = get_cocktail_info('https://iba-world.com/alexander/')#every time this changes the csv file is rewritten. how can I build off the csv values

df = pd.DataFrame([data])
df.to_csv('cocktailsFromIBA.csv')
print(df.head())

# driver.quit()
