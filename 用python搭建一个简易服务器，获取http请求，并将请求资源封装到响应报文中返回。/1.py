
import socket  #用套接字编程
 
serverPort = 6699
bind_ip = "127.0.0.1"  #设置端口号和本地ip
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, serverPort))
server.listen(1000)
print('the server is ready to receive')
 
 
def get_headers(line_list):
    headers = {}
    for line in line_list:
        new_line = line.decode('utf8')
        index = new_line.find(':')
        key = new_line[:index]
        value = new_line[index+1:].strip()
        headers[key] = value
    return headers
#动态获取请求报文需要的资源
while True:
    client, addr = server.accept()
    print("Accepted connection from: %s:%d" % (addr[0], addr[1]))
    try:
        sentence = client.recv(1024)
        filename = sentence.split()[1]
        f = open('D:/'+filename.decode('utf-8'), 'rb')#   r"index.html", "r" 读取本地文件
        line_list = sentence.split(b'\r\n')
        headers = get_headers(line_list)
        for i in line_list:
            print(i)
        accept = str(headers.get('Accept').split(',')[0].strip())
 
        outputdata = f.read()
        header = ' HTTP/1.1 200 OK\r\n' \
                 'Connection: close\r\n' \
                 'Content-Type: ' + accept + '\r\n' \
                                             'Content-Length: %d\r\n\r\n' % (len(outputdata))  #长度设置 important
 
        client.send(header.encode()+outputdata)
        client.close()
    except IOError:
        header = ' HTTP/1.1 404 Not Found'
        client.send(header.encode())
