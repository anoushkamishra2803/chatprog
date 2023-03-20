import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_message(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
        # start a new thread to receive messages from the client
        receive_thread = threading.Thread(target=receive_message, args=(conn,))
        receive_thread.start()
        
        # continually send messages to the client
        while True:
            message = input("write to the client:")
            conn.sendall(message.encode())
