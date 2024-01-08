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

    # initiualize movies list
    movies = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup.prettify())
        #class lien : ipc-lockup-overlay ipc-focusable
        #class lien : ipc-title-link-wrapper
        # metascore : sc-b0901df4-0 bcQdDJ metacritic-score-box
        # movie_containers = soup.find_all("div", attrs={"class": "lister-item mode-advanced"})
        movie_containers = soup.find_all("li", attrs={"class": "ipc-metadata-list-summary-item"})

        # print(movie_containers)

        for mc in movie_containers:
            # get all links and see if we can extract the title and other details from those links
            links = mc.find_all("a")
            # print(links)
            title = mc.find("h3")
            metascore = mc.find("span", "sc-b0901df4-0 bcQdDJ metacritic-score-box")
            url = ""
            list_url = []

            # Init du dict de chaque movie
            movie = {}

            # for link in links[1:]:
            #     href = link.attrs["href"]
            #     text = link.text
            #     if text != "":
            #         if href.startswith("/title/") and not href.endswith("/vote"):
            #             # print("Title ?", text, href)
            #             title = text
            #         elif href.startswith("/name/"):
            #             # print("Name ?", text, href)
            #             participants.append({"name": text, "href": href})

            print("title : " + title.text)
            print(links)
            for link in links:
                print(link.get('href'))
                list_url.append(link.get('href'))
            try:
                print("metascore : " + metascore.text)
            except:
                pass
            print('----------------------------------')
            movie['title'] = title.text
            # movie['participants'] = participants
            # years = soup.find_all('span', attrs={"class": "lister-item-year text-muted unbold"})
            # for year in years:
            #     movie['year'] = year.text
            #     break
            # print(movie)

            # Une fois le dict movie prêt, on l'ajoute à la liste des movies
            movies.append(movie)

    # the return needs to happen here
    return movies

def print_html(web_url):
    print("print html")
    response = requests.get(web_url)
    bs = BeautifulSoup(response.text, "html.parser")
    print(response.status_code)
    if response.status_code == 200:
        print("ok")
        print(bs.prettify())


URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,'
scrape_url(URL)
# movies = scrape_url(URL)
# print(movies)
# headers = ['title', 'url', 'participants', 'year']
# save_data(headers, movies)