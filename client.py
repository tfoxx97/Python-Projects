import socket
#import pickle # if you want to send non-byte data (objects, etc.)
import time

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "127.0.0.1" # control processor where we RX data from
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) # encode in bytes format
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # padding if header != 64
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

for i in range(5):
    send('!memory')
    time.sleep(1)
    if i == 4:
        send(DISCONNECT_MESSAGE)
