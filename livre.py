import requests
from bs4 import BeautifulSoup as BS
import csv
import re

urlbase ='http://books.toscrape.com'
url ='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
category ='poetry'
response = requests.get(url)
print(url)
if response.ok:
    soup = BS(response.content, features="html.parser")
    title = soup.find('title').text
    print(title)
    UPC = soup.find('th', string='UPC').next_sibling.text
    PriceWithTax= soup.find('th', string='Price (incl. tax)').next_sibling.text
    PriceExcludingTax = soup.find('th', string='Price (excl. tax)').next_sibling.text
    numberAvailable = soup.find('th', string='Availability').next_sibling.next_sibling.text
    numberAvailable = re.findall("\d+", numberAvailable)
    numberAvailable = numberAvailable[0]
    productDescription = soup.find('div', id="product_description").next_sibling.next_sibling.text
    nbReview = soup.find('th', string='Number of reviews').next_sibling.next_sibling.text
    imageUrl = soup.find('div' , id="product_gallery").find('img')['src']
    imageUrl = imageUrl[6:]
    imageUrl = (urlbase,imageUrl)
    imageUrl = '/'.join(imageUrl)
    print(url)
    with open('livre.csv', 'a', newline='') as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow([url,UPC,title, PriceExcludingTax,PriceWithTax, numberAvailable, nbReview, imageUrl, productDescription,category])
