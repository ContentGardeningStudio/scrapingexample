import requests
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31'
res = requests.get(URL)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    # Affiche le 1er film
    # print(soup.find('h3').findChild('a').text)

    movies = soup.find_all('h3', 'lister-item-header')
    for indice, movie in enumerate(movies, 1):
        movie_title = movie.find('a')
        print(str(indice) + '.' + movie_title.text)

    # lis = soup.find_all('li')
    # for li in lis:
    #     for d in dir('li'):
    #         print(d)
    #         if li.attrs['class'] == ['ipc-inline-list__item']:
    #             print(li.attrs)
    #             label = li.attrs['class']
    #             print(label)