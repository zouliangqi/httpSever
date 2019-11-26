import requests
import json
import pymysql

url='https://kaifa.fii-fmc.com/api/upload_img'
payload={'file':1}
re = requests.post(url,)

print(re.text)

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
cursor = conn.cursor()
cursor.execute('xxxxxxxxxxx')
sql1 = "kkk"
cursor.execute(sql1)
conn.commit()






"""url2='https://kaifa.fii-fmc.com/api/contact'
re=requests.post(url)
tokenObj=json.loads(re.text)
if  tokenObj["result"] == "success":
    print(tokenObj["toke"])
else:
    print("failed")"""