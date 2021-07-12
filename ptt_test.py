from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'

uesrAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
headers = {
    'User-Agent': uesrAgent
}

req = request.Request(url=url, headers=headers)

res = request.urlopen(req)

html = res.read().decode('utf8')

print(html)