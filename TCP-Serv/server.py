import socket
from socket import SHUT_RDWR
import logging
import time

#Файл служебных записей
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename="log.txt", level=logging.DEBUG)

def DoItAgain():
	#Сокет по умолчанию
	sock = socket.socket()
	#Настройка позволяющая использовать сокет заново
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('127.0.0.1', 9090))
	sock.listen(1)
	client_socket, addr = sock.accept()

	#Сокет по запросу
	sock_client = socket.socket()

	while True:
		#Получение запроса от клиента
		msg = client_socket.recv(1024).decode()

		#Подключение по умолчанию
		if msg == "STANDART":
			logging.info("Клиент подключен по умолчанию")
			client_socket_zapr, addr_zapr = client_socket, addr
			sock.close()
			break


		#Сокет по запросу
		try:
			client_socket_zapr, addr_zapr = msg.split("/")
			sock_client.bind((str(client_socket_zapr), int(addr_zapr)))
			sock_client.listen(1)
			client_socket.send("PROTECTED_SERV".encode())
			client_socket_zapr, addr_zapr = sock_client.accept()
			logging.info(f"Клиент подключен к порту {addr_zapr}")
			sock.close()
			break

		except OSError:
			addr_zapr = int(addr_zapr)
			while True:
				if addr_zapr < 64000:
					addr_zapr += 1
				else:
					addr_zapr = 2000
				try:
					sock_client.bind((str(client_socket_zapr), addr_zapr))
					sock_client.listen(1)
					client_socket.send("PROTECTED_SERV_CHOICE".encode())
					time.sleep(1)
					client_socket.send(str(addr_zapr).encode())
					client_socket_zapr, addr_zapr = sock_client.accept()
					sock.close()
					break
				except ValueError:
					pass
			break

		except ValueError:
			logging.error("Ошибка подключения клиента")
			client_socket.send("ERROR".encode())


	logging.info("Сервер начал прослушивание")
	while True:
		msg = client_socket_zapr.recv(1024).decode()
		logging.info("Прием данных от клиента")
		print(msg)
		client_socket_zapr.send(msg.encode())
		logging.info("Отправка данных клиенту")
		if msg == "exit":
			logging.info("Клиент отключен")
			break
		elif msg == "":
			logging.info("Разрыв соединения")
			sock_client.close()
			time.sleep(1)
			DoItAgain()

	sock_client.close()
	logging.info("Сервер закрыт")


DoItAgain()