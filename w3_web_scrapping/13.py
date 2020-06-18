import requests


data = requests.get('https://analytics.usa.gov/data/live/realtime.json')
print(data.json()['data'][0]['active_visitors'])