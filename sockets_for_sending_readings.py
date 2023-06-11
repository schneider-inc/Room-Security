import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def send_message(msg, conn):
    print('beginning send')
    message = msg.encode(FORMAT)
    msg_length = len(message)
    print(msg_length)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    print('sent length')
    conn.send(message)
    print('sent message')

def decode_message(conn):
    client_msg_length = conn.recv(HEADER).decode(FORMAT)
    if client_msg_length:
        client_msg_length = int(client_msg_length)
        msg = conn.recv(client_msg_length).decode(FORMAT)
        return msg

def send_readings(conn, addr):
    connected = True
    while connected:
        readings = input("Sample readings: ")

        send_message(readings, conn)

        msg = decode_message(conn)
        if msg == DISCONNECT_MESSAGE:
            connected = False    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=send_readings, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING] Server is starting...")
start()