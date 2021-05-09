import requests
from bs4 import BeautifulSoup as BS
import csv
import re
import nltk

urlbase ='http://books.toscrape.com'
urlcatalogue ='http://books.toscrape.com/catalogue'

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


def category(urlcat) :
    urlcategory = urlcat[:len(urlcat) - 11]
    response = requests.get(urlcat)
    links = []


    if response.ok:
        soup = BS(response.content, features="html.parser")
        nameCat = soup.find('div', {'class': 'page-header action'}).find({'h1'}).text
        print(nameCat)
        csvjoin = (nameCat, 'csv')
        fichcsv = ".".join(csvjoin)
        next = soup.find('a', text='next')
        divlink = soup.find_all('div', {"class": "image_container"})
        for div in divlink:
            a = div.find('a')
            link = a['href']
            link = link[8:]
            links.append(urlcatalogue + link)
        while next:
            urltemp = [urlcategory, next['href']]
            url = '/'.join(urltemp)
            response = requests.get(url)
            if response.ok:
                soup = BS(response.content, features="html.parser")
                next = soup.find('a', text='next')
                divlink = soup.find_all('div', {"class": "image_container"})
                for div in divlink:
                    a = div.find('a')
                    link = a['href']
                    link = link[8:]
                    links.append(urlcatalogue + link)
        for i in links:
            livre(i, category, fichcsv)




response = requests.get(urlbase)

if response.ok:
    soup = BS(response.content, features="html.parser")
    linksCat = []
    nameCat = []
    divCat = soup.find('div', {"class": "side_categories"}).find_all('li')
    for i in divCat:
        a = i.find('a')
        linkCat = a['href']
        Cat = a.text
        linksCat.append(urlbase + '/' + linkCat)
        nameCat.append(Cat)

    i=1
    while i < len(nameCat):
            urlcategorie = linksCat[i]
            Categorie= nameCat[i]
            i += 1
            category(urlcategorie)






