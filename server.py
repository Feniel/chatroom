import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.connect((socket.gethostname(), 7777))
serverSocket.listen(13)

while True:
    clientSocket, address = serverSocket.accept()
    print(f"Connection from {address} has bin established")

    clientSocket.send(bytes("Connection established", "utf-8"))
