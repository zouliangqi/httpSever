import requests
postdata={'type':'1256','rusume':'123'}
headers = {'Content-Type':'text/html'
# 'Host': '127.0.0.1:9999',
# 'Connection': 'keep-alive',
# 'Content-Length': '21',
# 'Cache-Control': 'max-age=0',
# 'Origin': 'http://127.0.0.1:9999',
# 'Upgrade-Insecure-Requests': '1',
#  'Content-Type': 'application/x-www-form-urlencoded',
#  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-User': '?1',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 'Sec-Fetch-Site': 'same-origin',
# 'Referer': 'http://127.0.0.1:9999',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cookie': '1571212640111'
}
r=requests.post('http://127.0.0.1:9999/main.py',data=postdata, headers=headers)
print(r.text)


# import urllib2
# import urllib
# data = {'name': '123', 'password': '123'}
# f = urllib2.urlopen(
#         url='http://127.0.0.1:9999/login.html',
#         data=urllib.urlencode(data)
#   )


# print(f.read())
# import requests
# data = '{"name":"jack","password":"123"}'
# headers = {'Content-Type':'application/json'}
# rep = requests.post(url=config['request']['DeleteGraph'], data=data, headers=headers)
# print(rep.text)


# import http.client

# url = "http://127.0.0.1:9999/login.html?name=123&password=123"

# conn = http.client.HTTPConnection("127.0.0.1:9999")
# conn.request(method="GET",url=url) 

# response = conn.getresponse()
# res= response.read()
# print(res)

