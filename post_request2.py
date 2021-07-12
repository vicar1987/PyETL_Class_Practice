import requests
from bs4 import BeautifulSoup


dataStr = """method: search
searchMethod: true
searchTarget: ATM
orgName: 12312314
orgId: 123123
hid_1: 1
tenderName: 123123123123
tenderId: 12313123
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/05/15
awardAnnounceEndDate: 110/05/15
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: adasdasdad
hid_2: 1
gottenVendorName: asdasdasd
gottenVendorId: asdasdad
hid_3: 1
submitVendorName: asdasdasd
submitVendorId: asdasdads
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""
# data = dict()
# for row in dataStr.split('\n'):
#     data[row.split(': ')[0]] = row.split(': ')[1]
# 將上述資料轉成dictionary

data = {row.split(': ')[0]: row.split(': ')[1] for row in dataStr.split('\n')}
# 一行的迴圈處理

print(data)