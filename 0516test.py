import requests
from bs4 import BeautifulSoup

url = 'http://2280decc246b.ngrok.io/practice/cfb101-11'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

ss = requests.session()

res = ss.get(url, headers=headers)
print(res.text)