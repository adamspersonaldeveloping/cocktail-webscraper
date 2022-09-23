from selenium import webdriver
import pymongo
import pandas as pd
import csv
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
db = os.getenv("DB_STRING")
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

client = pymongo.MongoClient(db)
db = client["cocktails-apd"]
col = db["cocktails-iba"]

DRIVER_PATH = '/Users/stein/Desktop/chromedriver'
service = Service(
                executable_path=DRIVER_PATH, 
            )
driver = webdriver.Chrome(options=options, service=service)

with open("cocktailURLs.csv") as f:
    reader = csv.reader(f)
    urlList = list(reader)
cocktailList = []

for val in urlList[0]:

     driver.get(val)
     
     cocktailName = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[1]/div/div/h1').get_attribute('textContent')
     
     ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').get_attribute('textContent').split('\n')
     
     def Convert(ingredients):
        ingredientDick= {f'ingredient{i}': ingredients[i] for i in range(0, len(ingredients))}
        return ingredientDick

     method = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[2]').get_attribute('textContent')

     garnish = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[3]').get_attribute('textContent')
     
     importance = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/p/a[2]').get_attribute('textContent')
     
     cocktail = {
         'cocktailName': cocktailName,
         'ingredients': Convert(ingredients),
         'method': method,
         'garnish': garnish,
         'styleType': importance,
         'ibaCocktail': 'true',
         'public': 'true',
         'user': 'IBA',
     }

     cocktailList.append(cocktail)

print(cocktailList)


x = col.insert_many(cocktailList)


df = pd.DataFrame(cocktailList)
df.to_csv('cocktailsFromIBA.csv')
print(df.head())


