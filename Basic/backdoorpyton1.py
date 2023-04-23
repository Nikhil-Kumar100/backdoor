import socket

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("10.2.62.206",4444)) 
