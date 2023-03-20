import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_message(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # start a new thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_message, args=(s,))
    receive_thread.start()
    
    # continually send messages to the server
    while True:
        message = input("write to the server:")
        s.sendall(message.encode())
