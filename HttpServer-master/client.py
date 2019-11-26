#!E:\python\venv\Scripts

# -*- coding:utf-8 -*-

import socket


def post_request():
    req = 'POST /?ni=00 HTTP/1.1\r\n'
    req = req + 'Host: 10.139.199.133:9999\r\n\r\n'
    req = req + 'name=linyi&data=163'
    return req


def get_request():
    req = 'GET / HTTP/1.1\r\n'
    req = req + 'Host: 10.139.199.133:9999\r\n\r\n'
    return req


def start_request():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.139.199.133', 9999))
    req = get_request()
    s.send(bytes(req).encode('utf-8'))
    buff = []
    while True:
        d = s.recv(1024)
        if d:
            buff.append(d)
        else:
            break
    data = ''.join(buff)
    s.close()
    header, html = data.split('\r\n\r\n', 1)
    f = open('res.html', 'w')
    f.write(html)
    f.close()


if __name__ == '__main__':
    start_request()
    input("press any key to exit;")

