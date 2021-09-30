from socket import *

addr = ('localhost', 9090)
udp_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('write to server: ')
    if not data:
        udp_socket.close()
        break

    #encode - перекодирует введенные данные в байты, decode - обратно
    udp_socket.sendto(data.encode(), addr)
    data = udp_socket.recvfrom(1024)
    print((data[0]).decode(), '\n')


udp_socket.close()
