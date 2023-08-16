#import scrapy
from bs4 import BeautifulSoup
import requests


#page_to_scrape = requests.get("https://quotes.toscrape.com")
#soup= BeautifulSoup(page_to_scrape.text, "html.parser")
#quotes = soup.findAll("span", attrs={"class": "text"})
#authors = soup.findAll("small", attrs= {"class": "author"})

#for quote, author in zip(quotes, authors):
#    print(quote.text + " - " + author.text)


page_to_scrape = requests.get("https://inside.wooster.edu/registrar/exams/")
soup= BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("figure", attrs={"class": "wp-block-table is-style-stripes"})



for quote in quotes:
    print(quote.text)


#soup= BeautifulSoup(page_to_scrape.text, "html.parser")
#quotes = soup.findAll("figure", attrs={"class": "wp-block-table is-style-stripes"}["thread"])