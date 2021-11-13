import socket

#Сокет по умолчанию
sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9091))

#Сокет по запросу
sock_zapr = socket.socket()
sock_zapr.setblocking(1)


while True:
    try:
        #Получение данных
        host = input("Введите номер хоста: ")
        port = input("Введите номер порта: ")

        #Проверка на пустоту
        if not (host) or not (port):
            raise ValueError

        #Отправка желаемых параметров
        msg = host+"/"+port
        sock.send(msg.encode())

        # Получение сообщения о готовности подключения
        msg = sock.recv(1024).decode()

        if msg == "ERROR":
            raise ValueError
        elif msg == "PROTECTED_SERV":
            sock_zapr.connect((host, int(port)))
            sock.close()
            break
        elif msg == "PROTECTED_SERV_CHOICE":
            while True:
                msg = sock.recv(1024).decode()
                try:
                    sock_zapr.connect((host, int(msg)))
                    sock.close()
                    print("Порт был занят, подключен порт: ", msg)
                    break
                except:
                    pass
            break


    except ValueError:
        if not (host) or not (port):
            sock.send(("STANDART").encode())
            sock_zapr.close()
            sock_zapr = sock
            print("Похоже, Вы ничего не ввели в одном из параметров. Сокет подключен по умолчанию")
            break
        else:
            print("Неверные значения. Попробуйте еще раз ")






while True:
    msg = input()
    sock_zapr.send(msg.encode())
    print(sock_zapr.recv(1024).decode())

    if msg == "exit":
        break

sock_zapr.close()


