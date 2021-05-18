import categorie

def impsite(soup)  :
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
            print(urlcategorie)
            categorie.category(urlcategorie)
