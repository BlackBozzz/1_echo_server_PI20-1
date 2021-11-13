import socket
import time

with open("users.txt", "r") as file:
    users = [line.split() for line in file.readlines()]


#Сокет по умолчанию
sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen(1)
client_socket, addr = sock.accept()
Ident = False

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

#Пароль
for user in users:
    if user[0] == str(addr[0]):
        while True:
            try:
                if user[2] != "":
                    client_socket.send(("Введите пароль для входа: ").encode())
                    msg = client_socket.recv(1024).decode()
                    if msg == user[2]:
                        client_socket.send(("Вход выполнен\n Введите новое сообщение: ").encode())
                        break
                    else:
                        client_socket.send(("Неверный пароль\n").encode())
            except:
                client_socket.send(("Похоже, что у Вас еще нет пароля. Давайте установим его.\n Введите пароль: ").encode())
                msg = client_socket.recv(1024).decode()
                while True:
                    if msg != "":
                        user.append(msg)
                        with open("users.txt", "w") as file:
                            for line in users:
                                file.write(" ".join(line))
                        break
                    else:
                        client_socket.send(("Введите пароль: ").encode())






while True:
    msg = client_socket.recv(1024).decode()
    print(msg)
    client_socket.send(msg.encode())
    client_socket.send(("\nВведите новое сообщение: ").encode())
    if msg == "exit" or msg == "":
        break