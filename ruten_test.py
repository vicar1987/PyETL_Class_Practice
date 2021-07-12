import requests

url = 'https://www.ruten.com.tw/category/00110002/list'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
headers = {
    'User-Agent': 'GoogleBot'
}

res = requests.get(url, headers=headers)
print(res.text)