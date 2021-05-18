import requests
from bs4 import BeautifulSoup as BS
import csv
import re
import urllib.request


def supterm(text):
    text = re.sub('[/:?*]', ' ', text)
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
        if len(nomImage)>20:
            nomImage = nomImage[:19]
        nomImage = supterm(nomImage)
        nomImage = (nomImage, 'jpg')
        nomImage = '.'.join(nomImage)
        urllib.request.urlretrieve(imageUrl, nomImage)
        title = soup.find('li',{'class':'active'}).text
        UPC = soup.find('th', string='UPC').next_sibling.text
        PriceWithTax = soup.find('th', string='Price (incl. tax)').next_sibling.text
        PriceExcludingTax = soup.find('th', string='Price (excl. tax)').next_sibling.text
        numberAvailable = soup.find('th', string='Availability').next_sibling.next_sibling.text
        numberAvailable = re.findall("\d+", numberAvailable)
        numberAvailable = numberAvailable[0]
        if soup.find('div', id="product_description"):
            productDescription = soup.find('div', id="product_description").next_sibling.next_sibling.text
        else:
            productDescription =''
        nbReview = soup.find('th', string='Number of reviews').next_sibling.next_sibling.text
        with open(fichiercsv, 'a', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow([url, UPC, title, PriceExcludingTax, PriceWithTax, numberAvailable, nbReview, imageUrl,productDescription.encode('utf8'), category])


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
        for i in links:
            livre(i, cat, fichcsv)
