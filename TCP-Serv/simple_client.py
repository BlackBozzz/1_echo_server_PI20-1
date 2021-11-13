import socket


#Сокет по умолчанию
sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))
msg = ""

while True:
    serv_msg = sock.recv(1024).decode()
    print(serv_msg)
    if serv_msg[-2] == ":" or serv_msg[-2] == "?":
        msg = input()
        sock.send(msg.encode())

    if msg == "exit":
        break


sock.close()


