from socket import AF_INET, SOCK_STREAM
import socket
import threading
import time


# 客户端仅需要按序执行 socket(), connect()
def test():
    s = socket.socket(AF_INET, SOCK_STREAM)
    s.connect(('192.168.110.45', 40001))
    s.send(b'GET / HTTP/1.1\r\nHost: 192.168.110.45:37192\r\nConnection: keep-alive\r\n\r\n')
    print(s.recv(4096), end='')
    # print(i)


print(time.strftime('%x'))
for i in range(100):
    test()
print(time.strftime('%x'))

# s = socket.socket(AF_INET, SOCK_STREAM)
# s.connect(('127.0.1.1', 40001))
# s.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nConnection: keep-alive\r\n\r\nhgdfsdsfsfdsfdsff')
# print(s.recv(4096))
