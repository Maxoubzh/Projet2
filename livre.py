import requests
from bs4 import BeautifulSoup as BS
import csv
import re


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
        nomImage = (nomImage, 'jpg')
        nomImage = '.'.join(nomImage)
        urllib.request.urlretrieve(imageUrl, nomImage)
        title = soup.find('title').text
        UPC = soup.find('th', string='UPC').next_sibling.text
        PriceWithTax = soup.find('th', string='Price (incl. tax)').next_sibling.text
        PriceExcludingTax = soup.find('th', string='Price (excl. tax)').next_sibling.text
        numberAvailable = soup.find('th', string='Availability').next_sibling.next_sibling.text
        numberAvailable = re.findall("\d+", numberAvailable)
        numberAvailable = numberAvailable[0]
        productDescription = soup.find('div', id="product_description").next_sibling.next_sibling.text
        nbReview = soup.find('th', string='Number of reviews').next_sibling.next_sibling.text
        with open(fichiercsv, 'a', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow([url, UPC, title, PriceExcludingTax, PriceWithTax, numberAvailable, nbReview, imageUrl,productDescription, category])
