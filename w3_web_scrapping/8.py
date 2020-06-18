import requests
from bs4 import BeautifulSoup

data = requests.get('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
data_parsed = BeautifulSoup(data.text)

for item in data_parsed.findAll('img'):
    print(item.get('src'))