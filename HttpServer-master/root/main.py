# !E:\python\venv\Scripts\
# -*- coding:utf-8 -*-

# 全局变量
SESSION = None
POST = None
GET = None
import pymysql



def app():
    if POST is not None:
        print('POST ', POST)
        if (('type' in POST.keys()) and ('resume' in POST.keys())):
            SESSION.setCookie('type', '123')
            SESSION.write2XML()
            s=str(POST.values())
            s=s[14:]
            s=s[:-3]
            c=s.split("', '")
            conn = pymysql.connect(user='root', password='123456', database='test', charset='utf8')
            cursor = conn.cursor()
            query = ("insert into cantactsalesman(type, resume, contact, mobile, companyName, email) values(%s,%s,%s,%s,%s,%s)")
            cursor.execute(query, (c[0],c[1],c[2],c[3],c[4],c[5]))
            conn.commit()
            cursor.close()
            conn.close()
            return "success"
        else:
            with open('root/index.html', 'r') as f:
                data = f.read()
            return data
    else:
        if SESSION.getCookie('name') is not None:
            return 'hello, '+SESSION.getCookie('name')
        with open('root/index.html', 'r') as f:
            data = f.read()
        return data

# and (POST['name'] == '123') and (POST['password']=='123')