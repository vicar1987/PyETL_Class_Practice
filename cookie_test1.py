import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = {
    'User-Anget': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

cookies = {
    'over18': '1'
}

res = requests.get(url, headers=headers, cookies=cookies)

print(res.text)