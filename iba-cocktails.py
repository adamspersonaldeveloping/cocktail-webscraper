import os
import csv
import pymongo
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

#Load env variables
def load_env():
    load_dotenv()
    return os.getenv("DB_STRING")

#Connect to MongoDb using pymongo
def connect_database(db_string):
    client = pymongo.MongoClient(db_string)
    db = client["cocktails-apd"]
    return db["cocktails-iba"]

#Set up Selenium and driver
def setup_selenium(driver_path):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(options=options, service=service)
    return driver

#Get URLs from CSV and return a list of them
def handle_url_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        url_list = list(reader)[0]
        return url_list

#Get cocktail data from IBA website
def get_cocktail_data(driver, url):
    driver.get(url)

    cocktailName = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[1]/div/div/h1').get_attribute('textContent')
    ingredients = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]').get_attribute('textContent').split('\n')
    method = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[2]').get_attribute('textContent')
    garnish = driver.find_element("xpath", '//*[@id="main-content"]/div/div/div/div/div[2]/div[1]/p[3]').get_attribute('textContent')
    importance = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/p/a[2]').get_attribute('textContent')

    def convert_to_dictionary(ingredients):
        ingredient_dictionary = {f'ingredient{i}': ingredients[i] for i in range(0, len(ingredients))}
        return ingredient_dictionary

    cocktail = {
         'cocktailName': cocktailName,
         'ingredients': convert_to_dictionary(ingredients),
         'method': method,
         'garnish': garnish,
         'importance': importance,
         'ibaCocktail': 'true',
         'public': 'true',
         'user': 'IBA',
    }

    return cocktail

def main():
    db_string = load_env()
    col = connect_database(db_string)
    path = "/Users/stein/Desktop/chromedriver"
    driver = setup_selenium(path)
    url_list = handle_url_csv("cocktailURLs.csv")
    cocktail_list = []

    #Create a list of cocktails by going over each url and scraping the data for the cocktails
    for url in url_list:
        cocktail = get_cocktail_data(driver, url)
        cocktail_list.push(cocktail)

    #Put the new list into the database
    col.insert_many(cocktail_list)

    #Put the cocktails into a csv file for later
    df = pd.DataFrame(cocktail_list)
    df.to_csv("cocktailsFromIBA.csv", index=False)

    driver.quit()

if __name__ == "__main__":
    main()
