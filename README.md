# Webscraper

This program is a web scraper designed to extract cocktail recipes from a specified website and store the data in a MongoDB database. The scraper then exports the collected data to a CSV file for further analysis or use. The data extracted includes the cocktail name, ingredients, preparation method, garnish, image URL, and importance. This program can be used for scraping anywebsite and doesn't need to be just for cocktails.

## How it is Made

**Tech used:** Python3, Selenium, pymongo, pandas, csv, dotenv

## Optimizations

To improve this web scraper, adding error handling to manage exceptions would be beneficial. Implementing logging to track the scraper's progress, errors, and other events would help with debugging and monitoring. With different websites, rate limits might be necessary to avoid overloading the target website.
