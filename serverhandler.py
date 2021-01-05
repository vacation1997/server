from socket import AF_INET, SOCK_STREAM
import socket
from handle_msg import HandleMsg
import threading


def threading_run_this(dataline_1, addr_1):
    print('get connection by', addr_1)
    handlemsg = HandleMsg()
    data = dataline_1.recv(4096)
    send_data = handlemsg.handle(str(data)[2:-1])
    if isinstance(send_data, bytes):
        dataline_1.sendall(send_data)
    else:
        dataline_1.sendall(bytes(send_data, encoding='utf-8'))


def sever_handler():
    # 服务器必须按序执行 socket(), bind(), listen(), accept() （可能需要重复执行 accept() 以服务多个客户端）
    server = socket.socket(AF_INET, SOCK_STREAM)
    server.bind(('192.168.110.45', 40001))
    server.listen(10)
    print('host address is ', socket.gethostbyname(socket.gethostname()))
    while True:
        dataline, addr = server.accept()
        t = threading.Thread(target=threading_run_this, args=(dataline, addr))
        t.start()


if __name__ == '__main__':
    sever_handler()