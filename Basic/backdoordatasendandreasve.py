import socket

#connect to the servear
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("10.2.62.206",4444)) #server ip addresh and port number

# clint send massage to server

message = "Seccessfully Connected."

connection.sendto(message.encode(),("10.2.62.206",4444))

#server send message to client and client receive message

receive_data = connection.recv(1024)
print(receive_data)

connection.close()
