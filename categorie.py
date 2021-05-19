import requests
from bs4 import BeautifulSoup as BS
import csv
import re
import urllib.request
import os


def supterm(text):
    text = re.sub('[/:?*"<>|]', ' ', text)
    return text


def livre(url,category,fichiercsv):
    urlbase = 'http://books.toscrape.com'
    response = requests.get(url)
    if response.ok:
        soup = BS(response.content, features="html.parser")
        imageUrl = soup.find('div', id="product_gallery").find('img')['src']
        imageUrl = imageUrl[6:]
        imageUrl = (urlbase, imageUrl)
        imageUrl = '/'.join(imageUrl)
        nomImage = soup.find('div', id="product_gallery").find('img')['alt']
        nomImage = supterm(nomImage)
        nomImage = (nomImage, 'jpg')
        nomImage = '.'.join(nomImage)
        nomImage = (category,nomImage)
        nomImage = '/'.join(nomImage)
        urllib.request.urlretrieve(imageUrl, nomImage)
        title = soup.find('li',{'class':'active'}).text
        tableau = soup.select('article td')
        UPC = tableau[0].text
        PriceWithTax = tableau[3].text
        PriceExcludingTax = tableau[2].text
        numberAvailable = tableau[5].text
        numberAvailable = re.findall("\d+", numberAvailable)
        numberAvailable = numberAvailable[0]
        if soup.find('div', id="product_description"):
            productDescription = soup.select_one('article > p').text
            productDescription = re.sub('\W+', '', productDescription)
        else:
            productDescription =''
        nbReview = tableau[6].text
        with open(fichiercsv, 'a', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow([url, UPC, title, PriceExcludingTax, PriceWithTax, numberAvailable, nbReview, imageUrl,productDescription, category])


def categoryPage(soup,links):
    urlcatalogue = 'http://books.toscrape.com/catalogue'
    divlink = soup.find_all('div', {"class": "image_container"})
    for div in divlink:
        a = div.find('a')
        link = a['href']
        link = link[8:]
        links.append(urlcatalogue + link)
    return links

def category(url):
    urlcategory = url[:len(url) - 11]
    response = requests.get(url)
    if response.ok:
        soup = BS(response.content, features="html.parser")
        cat = soup.find('li',{"class":'active'}).text
        fichcsv = [cat,'csv']
        fichcsv = '.'.join(fichcsv)
        links = []
        next = soup.find('a',text='next')
        links = categoryPage(soup,links)
        while next :
            urltemp = [urlcategory,next['href']]
            url = '/'.join(urltemp)
            response = requests.get(url)
            if response.ok:
                soup = BS(response.content, features="html.parser")
                next = soup.find('a',text='next')
                links = categoryPage(soup,links)
        with open(fichcsv, 'a', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow(['url', 'UPC', 'titre', 'Prix sans taxe','Prix avec Taxe','Nombre disponibles', 'Note','Url de l image','Description du livre','Catégorie'])
        if not os.path.exists(cat):
            os.makedirs(cat)
        for i in links:
            livre(i, cat, fichcsv)
        return cat


def impsite()  :
    urlbase = 'http://books.toscrape.com'

    response = requests.get(urlbase)

    if response.ok:
        soup = BS(response.content, features="html.parser")
    urlbase = 'http://books.toscrape.com'
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
            categorie = category(urlcategorie)
            print(categorie)