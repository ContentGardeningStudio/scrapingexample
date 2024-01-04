import requests
from bs4 import BeautifulSoup
import csv

# URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31'

# Search of films released since 01/01/2023
def save_data(headers, tab):
    if tab:
        with open('movies.csv', 'w', encoding='utf8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(tab)

def scrape_url(website_url):
    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(website_url, headers=HEADERS)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
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
            years = soup.find_all('span', attrs={"class": "lister-item-year text-muted unbold"})
            for year in years:
                movie['year'] = year.text
                break
            # print(movie)

            # Une fois le dict movie prêt, on l'ajoute à la liste des movies
            movies.append(movie)
            return movies


URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,'
movies = scrape_url(URL)
print(type(movies))
# headers = ['title', 'url', 'participants', 'year']
# save_data(headers, movies)