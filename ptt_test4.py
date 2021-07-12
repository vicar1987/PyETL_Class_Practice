import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {
    'User-Anget': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    titleList = soup.select('div.title') # return list
    # print(titleList)

    for titleSoup in titleList:
        try:
            title = titleSoup.select('a')[0].text
            urlArticle = 'https://www.ptt.cc/bbs' + titleSoup('a')[0]['href']
            print(title)
            print(urlArticle)
        except:
            pass
        print('==========')


    urlNew = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    print(urlNew)
    url = urlNew