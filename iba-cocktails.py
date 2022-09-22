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
driver.get('https://iba-world.com/trinidad-sour/')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('xpath', "/html/body/div[8]/p[2]/button[1]")).click()
    )
    
finally:
    #cocktailName = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[1]/div/div/h1').get_attribute('textContent')
    
    ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').get_attribute('textContent')
    ingredientsArray = ingredients.split('\n')
    ingredients2 = {}
    for index, val in ingredientsArray:
        ingredients2.append(f'ingredient{index}: {val}') #for index, val in enumerate(ingredients):
    print(ingredients2)
   # method = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[2]').get_attribute('textContent')
   
    #garnish = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[3]').get_attribute('textContent')

    #cocktail = {
    #     'cocktailName': cocktailName,
    #     'ingredients': ingredients,
    #     'method': method,
    #     'garnish': garnish,
    #     'ibaCocktail': 'true',

    # }
    # print(cocktail)
    #df = pd.DataFrame(cocktail)
    #print(df.head())
    
    



driver.quit()