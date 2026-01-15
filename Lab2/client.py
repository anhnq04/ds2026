import xmlrpc.client
import base64
import os

HOST = '127.0.0.1'
PORT = 5000

filename = input("Enter filename to send: ")

if not os.path.exists(filename):
    print(f"File {filename} not found!")
    exit()

with open(filename, 'rb') as f:
    file_data = base64.b64encode(f.read()).decode()

proxy = xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}/")
result = proxy.upload_file(filename, file_data)
print(result)
