import requests
from bs4 import BeautifulSoup

data = requests.get('https://en.wikipedia.org/wiki/Python')
data_parsed = BeautifulSoup(data.text)

for item in data_parsed.findAll('a'):
    print(item.get('href'))