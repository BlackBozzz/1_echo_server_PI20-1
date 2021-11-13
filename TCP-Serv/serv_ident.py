import socket

with open("users.txt", "r") as file:
    users = [line[:-1].split() for line in file.readlines()]


#Сокет по умолчанию
sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen(1)
client_socket, addr = sock.accept()

#Идентификация
try:
    for user in users:
        if user[0] == str(addr[0]):
            client_socket.send((f"Здравствуйте, {user[1]}\n").encode())
            Ident = True
            break
except:
    pass

if not(Ident):
    client_socket.send(("Здравствуйте!\n").encode())
    while True:
        client_socket.send(("Как я могу к Вам обращаться?)\n").encode())
        msg = client_socket.recv(1024).decode()
        if msg != "":
            users.append([addr[0], msg])
            with open("users.txt", "w") as file:
                for line in users:
                    file.write(" ".join(line))
            client_socket.send((f"Отлично!) Очень приятно, {msg}\n").encode())
            break
        else:
            client_socket.send(("Что-то пошло не так(\n").encode())

while True:
    msg = client_socket.recv(1024).decode()
    print(msg)
    client_socket.send(msg.encode())
    if msg == "exit":
        break