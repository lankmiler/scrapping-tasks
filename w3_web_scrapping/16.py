import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('twitter_link', metavar='twitter_link', type=str,
                    help='Twitter link')
args = parser.parse_args()

try:
    r = requests.get(args.twitter_link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text)
        print(soup.find('span', {'class': [ 'css-901oao' , 'css-16my406', 'r-1qd0xha', 'r-ad9z0x', 'r-bcqeeo', 'r-qvutc0']}).text)
    else:
        print('Wrong address given.')
except requests.exceptions.MissingSchema:
    print('page not exist')



