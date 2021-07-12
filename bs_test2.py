import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

uesrAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
headers = {
    'User-Agent': uesrAgent
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

# logo = soup.select('a#logo')
logo = soup.select('a[id="logo"]')
print(logo)
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc' + logo[0]['href'])
print(logo[0]['id'])

# logo = soup.findAll('a')
# for i in logo:
#     print(i)

bbsContent = soup.select('div.bbs-content')
print(bbsContent)