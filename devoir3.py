# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

#Après avoir importé request, csv et BeautifulSoup, j'insère mon URL, soit le site internet de Ricardo.
# Important de le mettre entre guillemets, sinon ça ne fonctionne pas. 

url = "https://www.ricardocuisine.com/recettes/"

# J'insère ensuite mon entête pour me présenter. 

entetes = {
    "User-Agent": "Alexandra Lauzon, étudiante journalisme UQAM"
}

# site = requests.get(url, headers=entetes)

# print(site.status_code) #Je vérifie ainsi si tout fonctionne bien. J'ai mon 200, je continue.

# page = BeautifulSoup(site.text, "html.parser")

# print(page) #On voit bien ici l'accueil du site de Ricardo. Tout fonctionne. 

sections = ["plats-principaux","entrees","desserts"]

n=0

for recettes in sections:
    # print(recettes)
    urlsection1 = url + recettes #Il s'agit de mes urls de bases pour mes trois grandes sections.

    site = requests.get(urlsection1, headers=entetes)

    # print(site.status_code) #Je vérifie ainsi si tout fonctionne bien. J'ai mon 200, je continue.

    page = BeautifulSoup(site.text, "html.parser")

    # print(page)

    section2 = page.find_all("div", class_="desc") 

    numero = list(range(2,20))
    
for nombre in numero:
        # print(nombre)

#Ma section2 constitue les trois grandes classes ""
    for section3 in section2:
        n += 1
        # print(section3)
        urlRecettes = "https://www.ricardocuisine.com" + section3.find("a")["href"] #Il s'agit de mes urls pour chaque sous-sections de mes grandes sections (ex: Plats principaux>Canard)
        urlRecettes2 = "https://www.ricardocuisine.com" + section3.find("a")["href"] + "/page/" + str(nombre) #Url pour les recettes des autres pages
        # print(n, urlRecettes)
        # print("."*10)

        siteA = requests.get(urlRecettes, headers=entetes)
        pageA = BeautifulSoup(siteA.text, "html.parser")

        siteB = requests.get(urlRecettes2, headers=entetes)
        pageB = BeautifulSoup(siteB.text, "html.parser")

        section4 = pageA.find_all("h2", class_="title")
        section4 = pageB.find_all("h2", class_="title")

        for section5 in section4:
            n += 1
            # print(section5)
            urlRecettes2 = "https://www.ricardocuisine.com" + section5.find("a")["href"] #Je me suis rendue compte que les liens qui menaient directement aux recettes ne contenaient pas "plats-principaux" (par exemple). Ça me menait directement à la page "Canard" (par exemple). Donc je n'ai pas besoin de le rajouter à l'url. 
            print(n,urlRecettes2) 
            print("."*10)


#Pour une raison qui m'échappe, je n'ai que les résultats pour les desserts. Je croyais que c'était à cause de l'ajout des numéros de pages, mais même lorsque je le sépare en deux "recettes", ça ne fonctionne pas. 
