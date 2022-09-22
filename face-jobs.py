from selenium import webdriver
import time
import pymongo
import pandas as pd
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

client = pymongo.MongoClient("mongodb+srv://adamspersonaldeveloping:bczjdTYNN38wg4qr@cluster0.qbjnhw6.mongodb.net/?retryWrites=true&w=majority")
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
print(urlList[0])
for val in urlList[0]:

     driver.get(val)
     cocktailName = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[1]/div/div/h1').get_attribute('textContent')
     ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').get_attribute('textContent')
     #//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[1]/text()[1]
     ingredients2 = {
        for index, val in enumerate(ingredients): #ingredients in the html is a <p> with each ingredient seperated by <br>. I want to create an object that will have 'ingredient{i}': text in first element,  'ingredient{i +1}': text in second element // the problem is each cocktail has a different number of ingredients and I want the ingredients2 to be an object with each key matching the number of ingredients.
            f"ingredient{index + 1}":  driver.find_element("xpath", f'//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[1]/text()[{index}]').get_attribute('textContent'),
     }
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

     cocktailList.append(cocktail)

print(cocktailList)
#data = get_cocktail_info('https://iba-world.com/alexander/')#every time this changes the csv file is rewritten. how can I build off the csv values

x = col.insert_many(cocktailList)


df = pd.DataFrame(cocktailList)
df.to_csv('cocktailsFromIBA.csv')
print(df.head())

# driver.quit()
