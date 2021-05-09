import requests
from bs4 import BeautifulSoup as BS
import csv
import re

urlbase ='http://books.toscrape.com'
urlcatalogue ='http://books.toscrape.com/catalogue'
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
#url ='http://books.toscrape.com/catalogue/category/books/poetry_23/index.html'
urlcategory = url[:len(url)-11]
category ='poetry'
response = requests.get(url)
fichcsv = 'poetry.csv'

def livre(url,category,fichiercsv):
    urlbase = 'http://books.toscrape.com'
    response = requests.get(url)
    if response.ok:
        soup = BS(response.content, features="html.parser")
        title = soup.find('title').text
        UPC = soup.find('th', string='UPC').next_sibling.text
        PriceWithTax = soup.find('th', string='Price (incl. tax)').next_sibling.text
        PriceExcludingTax = soup.find('th', string='Price (excl. tax)').next_sibling.text
        numberAvailable = soup.find('th', string='Availability').next_sibling.next_sibling.text
        numberAvailable = re.findall("\d+", numberAvailable)
        numberAvailable = numberAvailable[0]
        productDescription = soup.find('div', id="product_description").next_sibling.next_sibling.text
        nbReview = soup.find('th', string='Number of reviews').next_sibling.next_sibling.text
        imageUrl = soup.find('div', id="product_gallery").find('img')['src']
        imageUrl = imageUrl[6:]
        imageUrl = (urlbase, imageUrl)
        imageUrl = '/'.join(imageUrl)
        with open(fichiercsv, 'a', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow([url, UPC, title, PriceExcludingTax, PriceWithTax, numberAvailable, nbReview, imageUrl,
                             productDescription, category])

def categoryPage(soup):
    divlink = soup.find_all('div', {"class": "image_container"})
    for div in divlink:
        a = div.find('a')
        link = a['href']
        link = link[8:]
        links.append(urlcatalogue + link)

    for i in links:
        livre(i, category, fichcsv)

if response.ok:
    soup = BS(response.content, features="html.parser")
    links=[]
    #next = soup.find('ul',{"class": "pager"}).
    next = soup.find('a',text='next')
    categoryPage(soup)
    while next :
        urltemp = [urlcategory,next['href']]
        url = '/'.join(urltemp)
        response = requests.get(url)
        if response.ok:
            soup = BS(response.content, features="html.parser")
            next = soup.find('a',text='next')
            categoryPage(soup)
