import requests
from bs4 import BeautifulSoup


data = requests.get('https://en.wikipedia.org/wiki/Main_Page')
data_parsed = BeautifulSoup(data.text)

print(data_parsed.select('h1'))