import requests
import json
import os #輸入套件可以建立資料夾
from urllib import request

# mac電腦要多輸入下面套件才不會出現錯誤
# import ssl
# ssl._create_default_https_context = ssl.create_unverified_context

if not os.path.exists('./dcardPhoto'):
    os.mkdir('./dcardPhoto')

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=235983370'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

res = requests.get(url, headers=headers)
# print(res.text)
jsonData = json.loads(res.text) #這是一個list

for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p/' + str(articleObj['id'])
    print(title)
    print(articleUrl)
    for img in articleObj['mediaMeta']:
        imgUrl = img['url']
        # 儲存圖片
        # request.urlretrieve(imgUrl, './dcardPhoto/{}.{}'.format(title, imgUrl.split('.')[-1]))
        # request.urlretrieve(imgUrl, './dcardPhoto/{}_{}'.format(title, imgUrl.split('/')[-1]))
        imgRes = requests.get(imgUrl, headers=headers)
        imgContent = imgRes.content
        with open('./dcardPhoto/{}_{}'.format(title, imgUrl.split('/')[-1], 'wb') as f:
            f.write(imgContent)
        print('\t', imgUrl)
    print('==========')


