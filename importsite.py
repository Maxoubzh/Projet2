import requests
from bs4 import BeautifulSoup as BS
import categorie

def choix() :
    choix ='0'
    while choix != '1' and choix !='2' and choix !='3' and choix != '4':
        print("Pour télécharger un livre, taper 1")
        print("Pour télécharger une section, taper 2")
        print("Pour télécharger le site entier, taper 3")
        print("Pour quitter le programme, taper 4")
        choix = input("Quel est votre choix? : ")

        if choix == '1' :
            print('')
            print("Vous souhaitez récupérer les informations d'un livre")
            url =input("Pour ceci, veuillez rentrer l'url du livre : ")
            response = requests.get(url)
            if response.ok :
                soup = BS(response.content, features="html.parser")
                name = soup.find('li', {"class":"active"}).text
                csv = [name,'csv']
                csv = '.'.join(csv)
                category = soup.select('ul li a')[2].text
                categorie.livre(url,category,csv)
                print("Vous allez maintenant retrouver les informations dans un fichier au nom du livre")
                print("Merci d'avoir utiliser notre logiciel, au revoir")
        elif choix == '2' :
            print('')
            print("Vous souhaitez récupérer les informations d'une catégorie")
            url = input("Pour ceci, veuillez rentrer l'url de la catégorie : ")
            categorie.category(url)
            print ("Vous allez maintenant retrouver les informations dans un fichier au nom de la catégorie")
            print("Merci d'avoir utiliser notre logiciel, au revoir")
        elif choix == '3' :
            print("Traitrment en cours, attention le traitement peux être long")
            print("Le nombre de catégories traitées va s'afficher durant le traitement")
            categorie.impsite()
            print("Vous allez maintenant retrouver les informations dans différents fichiers aux noms des catégories")
            print("Merci d'avoir utiliser notre logiciel, au revoir")
        elif choix == '4' :
            print("Merci d'avoir utiliser notre logiciel, au revoir")
        else :
            print('')
            print("Vous avez du faire une erreur en tapant")
            print('')

if __name__ == '__main__':
    print("Bonjour, à l'aide de ce programme, vous pouvez télécharger les informations d'un livre en particulier, de toute une section ou bien le site en entier")
    choix()
