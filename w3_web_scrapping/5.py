import requests
from bs4 import BeautifulSoup


data = requests.get('https://catalog.data.gov/dataset?q=&sort=metadata_modified+desc')
data_parsed = BeautifulSoup(data.text)

print(data_parsed.select_one('.dataset-content').select_one('a').text)