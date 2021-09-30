import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))

while True:
    msg = input()
    sock.send(msg.encode())
    print(sock.recv(1024).decode())

    if msg == "exit":
        break

sock.close()


