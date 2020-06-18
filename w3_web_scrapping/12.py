import requests
from bs4 import BeautifulSoup

data = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(data.text)

for item in range(3, 0, -1):
    languages_soup = soup.find('li', {'id': 'lang-{}'.format(item)})
    print(languages_soup.text)

