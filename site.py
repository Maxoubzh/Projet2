import requests
from bs4 import BeautifulSoup as BS
import csv
import re
import urllib.request
import categorie

urlbase ='http://books.toscrape.com'
urlcatalogue ='http://books.toscrape.com/catalogue'

response = requests.get(urlbase)

if response.ok:
    soup = BS(response.content, features="html.parser")
    linksCat = []
    divCat = soup.find('div', {"class": "side_categories"}).find_all('li')
    for i in divCat:
        a = i.find('a')
        linkCat = a['href']
        linksCat.append(urlbase + '/' + linkCat)

    i=1
    while i < len(linkCat):
            urlcategorie = linksCat[i]
            i += 1
            print(urlcategorie)
            categorie.category(urlcategorie)
