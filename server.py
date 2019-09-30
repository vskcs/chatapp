import socket

host= '10.5.1.16' //my system ipconfig
port= 5000

server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen()
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:
    data = conn.recv(1024).decode()
    print("from connected user: " + str(data))
    data = input('->')
    conn.send(data.encode())

conn.close()
