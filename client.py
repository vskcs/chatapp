import socket

host= '10.5.1.16'
port= 5000

client_socket = socket.socket()
client_socket.connect((host, port))

message = input(" -> ")

while message.lower().strip() != 'Bye' :
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    print('Received from Server: ' + data)

    message = input(" -> ")

client_socket.close()
