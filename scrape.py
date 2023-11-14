import requests
from bs4 import BeautifulSoup
import csv

# URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31'

# Search of films released since 01/01/2023
URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,'

res = requests.get(URL)

if res.status_code == 200:
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
        movies = {}

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
        movies['title'] = title
        movies['participants'] = participants
        years = soup.find_all('span',attrs={"class": "lister-item-year text-muted unbold"})
        for year in years:
            movies['year'] = year.text
            break
        print(movies)

        headers = ['title','casting','url','year']
        with open('movies.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(movies)


    # movies = soup.find_all('h3', 'lister-item-header')
    # for indice, movie in enumerate(movies, 1):
    #     movie_title = movie.find('a')
    #     print(str(indice) + '.' + movie_title.text)
