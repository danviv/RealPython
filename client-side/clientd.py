import requests
url='http://httpbin.org/post'
data={'fname':'Dan','lname':'V'}
r=requests.post(url,data=data)
print r.content