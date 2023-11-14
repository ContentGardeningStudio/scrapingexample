import requests
from bs4 import BeautifulSoup
import csv

# URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31'

# Search of films released since 01/01/2023
URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,'

res = requests.get(URL)

if res.status_code == 200:
    # initialisation de la liste résultat
    movies = []

    soup = BeautifulSoup(res.text, 'html.parser')
    # Affiche le 1er film
    # print(soup.find('h3').findChild('a').text)

    movie_containers = soup.find_all("div", attrs={"class": "lister-item mode-advanced"})
    # print(movie_containers)

    for mc in movie_containers:
        # get all links and see if we can extract the title and other details from those links
        links = mc.find_all("a")
        # print(links)
        title = ""
        url = ""
        participants = []

        # Init du dict de chaque movie
        movie = {}

        for link in links[1:]:
            href = link.attrs["href"]
            text = link.text
            if text != "":
                if href.startswith("/title/") and not href.endswith("/vote"):
                    # print("Title ?", text, href)
                    title = text
                elif href.startswith("/name/"):
                    # print("Name ?", text, href)
                    participants.append({"name": text, "href": href})

        # print(title, url, participants)
        movie['title'] = title
        movie['participants'] = participants
        years = soup.find_all('span',attrs={"class": "lister-item-year text-muted unbold"})
        for year in years:
            movie['year'] = year.text
            break
        print(movie)

        # Une fois le dict movie prêt, on l'ajoute à la liste des movies
        movies.append(movie)

    # Maintenant on a movies, on peut faire l'enregistrement en CSV
    # On s'assure quand même que la liste n'est pas vide...
    if len(movies) != 0:
        headers = ['title','participants','url','year']
        with open('movies.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(movies)
