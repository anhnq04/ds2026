import socket
import os

HOST = '0.0.0.0'
PORT = 5000
BUFFER = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = s.accept()
print(f"Connected by {addr}")

filename = conn.recv(1024).decode()
print(f"Receiving: {filename}")

with open(filename, 'wb') as f:
    while True:
        data = conn.recv(BUFFER)
        if not data or data == b'EOF':
            break
        f.write(data)

print(f"File {filename} received successfully!")
conn.close()
s.close()
