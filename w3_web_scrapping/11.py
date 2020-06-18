import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('page', metavar='page', type=str,
                    help='Page link')
args = parser.parse_args()


try:
    r = requests.get(args.page)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text)
        if soup.find('title'):
            print('Has title')
        else:
            print("Hasn't title")
    else:
        print('Wrong page given.')
except requests.exceptions.MissingSchema:
    print('page not exist')



