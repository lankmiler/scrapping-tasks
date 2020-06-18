import requests
from bs4 import BeautifulSoup

data = requests.get('http://example.com')
data_parsed = BeautifulSoup(data.text)
print(data_parsed.select_one('h1'))