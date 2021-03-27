# -*- coding: utf-8 -*-
import socket


def handlerRequest(client):
    buf = client.recv(2048)
    print(buf)
    msg = "HTTP/1.1 200 OK\r\n\r\n"
    msg1 = "Hello World!"
    client.send(('%s' % msg).encode())
    client.send(('%s' % msg1).encode())


if __name__ == '__main__':
    ip_port = ("0.0.0.0", 8000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(ip_port)
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        handlerRequest(conn)
        conn.close()

"""
========== Chrome Browser

b'GET / HTTP/1.1\r\n
Host: localhost:8000\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7\r\n
Cookie: Pycharm-50af3b7d=e5744f8c-6802-40fb-9588-ce6209f1fac0; Idea-6c92d892=04cb8871-dcbe-420d-a8b3-bda8527045f9; Webstorm-8b18d2e8=7891e525-8364-49e2-a845-05e0cd68e6aa\r\n\r\n'

b'GET /favicon.ico HTTP/1.1\r\n
Host: localhost:8000\r\n
Connection: keep-alive\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36\r\n
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\n
Sec-Fetch-Site: same-origin\r\n
Sec-Fetch-Mode: no-cors\r\n
Sec-Fetch-Dest: image\r\n
Referer: http://localhost:8000/\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7\r\n
Cookie: Pycharm-50af3b7d=e5744f8c-6802-40fb-9588-ce6209f1fac0; Idea-6c92d892=04cb8871-dcbe-420d-a8b3-bda8527045f9; Webstorm-8b18d2e8=7891e525-8364-49e2-a845-05e0cd68e6aa\r\n\r\n'
"""

"""
========== Firefox Browser

b'GET / HTTP/1.1\r\n
Host: localhost:8000\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n
Accept-Encoding: gzip, deflate\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
Cache-Control: max-age=0\r\n\r\n'

"""

"""
========== Microsoft Edge Browser

b'GET / HTTP/1.1\r\n
Host: localhost:8000\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6\r\n\r\n'

b'GET /favicon.ico HTTP/1.1\r\n
Host: localhost:8000\r\n
Connection: keep-alive\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57\r\n
Accept: image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\n
Sec-Fetch-Site: same-origin\r\n
Sec-Fetch-Mode: no-cors\r\n
Sec-Fetch-Dest: image\r\n
Referer: http://localhost:8000/\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6\r\n\r\n'
"""