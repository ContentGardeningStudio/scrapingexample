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

# Simplified case for testing (participants / casting for a given movie)
casting_names = []
casting_urls = []
participants = [{'name': 'Aria Mia Loberti', 'href': '/name/nm13200978/'}, {'name': 'Louis Hofmann', 'href': '/name/nm3836977/'}, {'name': 'Lars Eidinger', 'href': '/name/nm1955257/'}, {'name': 'Hugh Laurie', 'href': '/name/nm0491402/'}]
for p in participants:
    vals = list(p.values())
    # list() est nécessaire, ici dans notre cas, pour convertir l'object dict_values
    print(vals)   # example output: ['Aria Mia Loberti', '/name/nm13200978/']

    # deal with the name value... and collect the data in casting_names
    name = vals[0]
    # print(name)
    casting_names.append(name)

    # deal with the url/href value... and collect the data in casting_urls
    url = vals[1]
    # print(url)
    casting_urls.append(url)

print("COLLECTED DATA FOR THIS MOVIE:")
print("=>", casting_names)
print("=>", casting_urls)