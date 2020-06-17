import requests

robots_page = 'https://en.wikipedia.org/robots.txt'
r = requests.get(robots_page)
print(r.text)



