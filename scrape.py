import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31')

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    # Affiche le 1er film
    # print(soup.find('h3').findChild('a').text)
    i = 1
    movies = soup.find_all('h3', 'lister-item-header')
    for movie in movies:
        movie_title = movie.find('a')
        print(str(i) + '.' + movie_title.text)
        i += 1

    # lis = soup.find_all('li')
    # for li in lis:
    #     for d in dir('li'):
    #         print(d)
    #         if li.attrs['class'] == ['ipc-inline-list__item']:
    #             print(li.attrs)
    #             label = li.attrs['class']
    #             print(label)