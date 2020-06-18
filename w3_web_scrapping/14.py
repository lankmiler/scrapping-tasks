import requests
import datetime
from bs4 import BeautifulSoup


data = requests.get('https://www.us-cert.gov/ncas/alerts/%s' % datetime.datetime.now().strftime('%Y'))
print(len(BeautifulSoup(data.text).find_all('div', {'class', 'views-field'})))