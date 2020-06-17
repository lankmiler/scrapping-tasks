import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('page', metavar='page', type=str,
                    help='Page link')
args = parser.parse_args()
try:
    r = requests.get(args.page)
    if r.status_code == 200:
        print('page exist')
    else:
        print('page not exist')
except requests.exceptions.MissingSchema:
    print('page not exist')



