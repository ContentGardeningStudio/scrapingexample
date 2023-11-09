import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.scrapethissite.com/pages/')

if res.ok:
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find('h1')
    print(title.text)