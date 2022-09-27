from selenium import webdriver
import os
import pymongo
import pandas as pd
import csv
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
db = client["test"]
col = db["posts"]

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

     method = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[2]').get_attribute('textContent')

     garnish = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[3]').get_attribute('textContent')

     importance = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/p/a[2]').get_attribute('textContent')
     
     #note = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/div/div/p[1]/text()[1]').get_attribute('textContent')

     image = driver.find_element("xpath", '/html/head/meta[12]').get_attribute("content")

    

     cocktail = {
         'cocktailName': cocktailName,
         'ingredients': ingredients,
         'method': method,
         'garnish': garnish,
         #'note': note,
         'image': image,
         'importance': importance,
         'ibaCocktail': 'true',
         'public': 'true',
         'user': 'International Bartenders Association',
         'createdAt': 1,
     }

     cocktailList.append(cocktail)
     print(cocktail)

print(cocktailList)


x = col.insert_many(cocktailList)


df = pd.DataFrame(cocktailList)
df.to_csv('cocktailsFromIBA.csv')
print(df.head())


