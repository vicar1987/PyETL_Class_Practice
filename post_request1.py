import requests

url = 'http://2280decc246b.ngrok.io/hello_post'
url = 'http://httpbin.org/post'
data = {
    'username': 'Vic'
}
# 此處的Value值隨意帶入

res = requests.post(url, data=data)

print(res.text)