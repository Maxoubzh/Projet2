import requests
from bs4 import BeautifulSoup as BS

url ='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

if response.ok:
    soup = BS(response.content, features="html.parser")
    title = soup.find('title')
    UPC = soup.find('th', string='UPC').next_sibling.text
    PriceWithTax= soup.find('th', string='Price (incl. tax)').next_sibling.text
    PriceExcludingTax = soup.find('th', string='Price (excl. tax)').next_sibling.text
    numberAvailable = soup.find('th', string='Availability').next_sibling.next_sibling.text
    productDescription = soup.find('div', id="product_description").next_sibling.next_sibling.text
    nbReview = soup.find('th', string='Number of reviews').next_sibling.next_sibling
    if nbReview.text=='0' :
        reviewRating = "None"
    else :
        reviewRating = soup.find('th', string='UPC').next_sibling.text
    imageUrl = soup.find('div' , id="product_gallery").find('img')['src']
    print('UPC :',UPC)
    print('Prix avec Taxe :', PriceWithTax)
    print('Prix sans taxe :', PriceExcludingTax)
    print("Nombre d'ouvrage disponible :", numberAvailable)
    print("Note utilisateur s'il y en a :",reviewRating)
    print("Url de l'image :",imageUrl)
    print(productDescription)
