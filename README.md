# Projet Book to Scrape

Afin de mettre en oeuvre le projet, vous aurez besoin d'utiliser un terminal et python
Si vous n'avez pas de terminal, vous pouvez installer cygwin, vous le trouverez site: 

Il faut aussi que votre version de python soit à jour, vous aurez besoin de l'environnement virtuel. 
Vous pouvez tapez. python --version
Si votre version est supérieur à la version 3.3, cela devrait correctement fonctionner.

Nous allons créer un dossier pour y déposer nos fichiers
mkdir projetBookToScrap
et nous y déplacer
cd projetBookToScrap

Vous allez pouvoir maintenant placer le contenu de github dans le repertoire projetBookToScrap

Nous allons maintenant creer l'environnement virtuel pour ceci taper la commande suivante :
python -m venv env
Puis nous allons l'activer :
env/Scripts/activate.bat

Nous allons maintenant importer les modules nécessaires à l'aide de la commande 

pip install -r requirements.txt

Vous pouvez vérifier que la commande à bien installer les modules avec la commande:
pip freeze


Nous allons maintenant pouvoir lancer le programme à l'aide de la commande :
python importsite.py

Un menu s'affiche alors à vous, vous pouvez ainsi soit:
  télécharger le contenu d'un livre
  télécharger toute une section
  télécharger le site entier
  ou quitter l'application
  
Lorsque vous allez télécharger un livre ou une section, il faudra fournir le lien hypertexte du livre ou de la section choisie.

Attention l'importation du site entier peut être long.

