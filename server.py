import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 7777

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SOL_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}
'''
server_socket.listen(13)

while True:
    clientSocket, address = serverSocket.accept()
    print(f"Connection from {address} has bin established")

    clientSocket.send(bytes("Connection established", "utf-8"))
'''