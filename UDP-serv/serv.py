# Модуль socket для сетевого программирования
from socket import *

# данные сервера
addr = ('localhost', 9090)

# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# bind - связывает адрес и порт с сокетом
udp_socket.bind(addr)


while True:
    # recvfrom - получает UDP сообщения
    text, addr = udp_socket.recvfrom(1024)
    print('client ' + str(addr[1]) + ': ', text.decode())

    # sendto - передача сообщения UDP
    udp_socket.sendto(b'Message send', addr)

udp_socket.close()