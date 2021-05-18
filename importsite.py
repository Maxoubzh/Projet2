import requests
from bs4 import BeautifulSoup as BS
import impsite

if __name__ == '__main__':
    urlbase = 'http://books.toscrape.com'
    urlcatalogue = 'http://books.toscrape.com/catalogue'

    response = requests.get(urlbase)

    if response.ok:
        soup = BS(response.content, features="html.parser")
        impsite.impsite(soup)