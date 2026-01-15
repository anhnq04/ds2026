import socket
import os

HOST = '127.0.0.1'
PORT = 5000
BUFFER = 4096

filename = input("Enter filename to send: ")

if not os.path.exists(filename):
    print(f"File {filename} not found!")
    exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Gửi tên file
s.send(filename.encode())

# Gửi nội dung file
with open(filename, 'rb') as f:
    while True:
        data = f.read(BUFFER)
        if not data:
            break
        s.send(data)

s.send(b'EOF')
print(f"File {filename} sent successfully!")
s.close()
