import requests
import argparse

API_KEY = 'f4f2361f8a484a8ea71c1aa0cdb30ca2'

parser = argparse.ArgumentParser()
parser.add_argument('address', metavar='page', type=str,
                    help='Page link')
args = parser.parse_args()

API_URL = 'https://api.opencagedata.com/geocode/v1/json?q=%s&key=' + API_KEY

try:
    r = requests.get(API_URL % args.address)
    if r.status_code == 200:
        result = r.json()['results'][0]
        print('latitude %s and longitude %s' % (result['annotations']['DMS']['lat'], result['annotations']['DMS']['lng']))
    else:
        print('Wrong address given.')
except requests.exceptions.MissingSchema:
    print('page not exist')



