import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = {
    'User-Anget': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

ss = requests.session()     # 類似開啟新的無痕視窗

ss.cookies['over18'] = '1'  # 類似在剛開的新無痕視窗內貼上網址
                            # 身分紀錄會被沿用

res = ss.get(url, headers=headers)

print(res.text)
