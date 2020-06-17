import requests
from bs4 import BeautifulSoup


robots_page = 'https://www.data.gov/'
r = requests.get(robots_page)

soup = BeautifulSoup(r.text)

tag = soup.select_one('a[href="/metrics"]')
print('Number of datasets is %s' % (tag.text.rstrip('datasets')))
