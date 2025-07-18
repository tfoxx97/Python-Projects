import socket
import threading
import random

rando_list = [1, 2, 3, 4, 5, 6, 7, 8, 3.14, 69, 420]
memory = "!memory"

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "127.0.0.1" # control processor where we RX data from
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    ''' handling individual client connections in a single thread.'''
    print("New connection {} connected".format(addr))
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            if msg == memory:
                conn.send("{}\n".format(random.choice(rando_list)).encode(FORMAT))

            print("{} {}".format(addr, msg))
            conn.send("Message received: {}".format(msg).encode(FORMAT))

    conn.close()

def start():
    ''' begin listening on ip and port for any client communication'''
    server.listen()
    print("Listening on {}".format(SERVER))
    while True:
        # wait for new connection to server, store connect info, send 2 server
        conn, addr = server.accept() 
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print("Active clients: {}".format(threading.activeCount() - 1))

print("Server is listening ... ")
start()
