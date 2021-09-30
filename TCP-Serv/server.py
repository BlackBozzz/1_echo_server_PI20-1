import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen(1)
client_socket, addr = sock.accept()

while True:
	msg = client_socket.recv(1024).decode()
	print(msg)
	client_socket.send(msg.encode())
	if msg == "exit":
		sock.close()
		break



