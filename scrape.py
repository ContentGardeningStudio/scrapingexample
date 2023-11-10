import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/search/title/?release_date=2023-01-01,2023-12-31')

if res.ok:
    i = 1
    soup = BeautifulSoup(res.text, 'html.parser')
    movies = soup.find_all('li', ['ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent'])
    print(dir(movies))
    for movie in movies:
        movie_title = movie.findChildren('h3', 'ipc-title__text')
        print(dir(movie))
        i += 1
        if i == 1:
            break

    # my_lis = soup.find_all('li')
    # for li in my_lis:
    #      doc = dir(li)
    #      for d in doc:
    #          print(d)
    #         if li.attrs["class"] == ['ipc-inline-list__item']:
    #             print(li.attrs)
    #             label = li.attrs["class"]
    #             print(label)

    divs = soup.find_all('div')
    for div in divs:
        doc = dir(div)
        for d in doc:
            print(d)
