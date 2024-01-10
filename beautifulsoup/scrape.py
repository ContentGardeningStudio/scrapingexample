import requests
from bs4 import BeautifulSoup
import csv

# URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31'

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# Search of films released since 01/01/2023
def save_data(headers, tab):
    if tab:
        with open('movies.csv', 'w', encoding='utf8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(tab)

def scrape_url(website_url):
    res = requests.get(website_url, headers=HEADERS)

    # initialize movies list
    movies = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup.prettify())
        # movie_containers = soup.find_all("div", attrs={"class": "lister-item mode-advanced"})
        movie_containers = soup.find_all("li", attrs={"class": "ipc-metadata-list-summary-item"})

        # print(movie_containers)

        for mc in movie_containers:
            BASE_URL = "https://imdb.com"
            # get all links and see if we can extract the title and other details from those links
            links = mc.find_all("a")
            # print(links)
            title = mc.find("h3")
            metascore = mc.find("span", "sc-b0901df4-0 bcQdDJ metacritic-score-box")
            url = ""

            # Init du dict de chaque movie
            movie = {}

            # print("title : " + title.text)
            # print(links)
            for link in links:
                # print(link.get('href'))
                if "sr_t" in link.get('href'):
                    url += BASE_URL + link.get('href')
            # print(url)
            # print('----------------------------------')
            movie['title'] = title.text
            movie['href'] = url
            try:
                # print("metascore : " + metascore.text)
                movie['metascore'] = metascore.text
            except:
                pass

            # Une fois le dict movie prêt, on l'ajoute à la liste des movies
            movies.append(movie)

    # the return needs to happen here
    return movies


URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,'
scrape_url(URL)
list_movies = scrape_url(URL)
headers = ['title', 'href', 'metascore']
save_data(headers, list_movies)