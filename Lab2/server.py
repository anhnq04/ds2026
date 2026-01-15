from xmlrpc.server import SimpleXMLRPCServer
import base64

HOST = '0.0.0.0'
PORT = 5000

def upload_file(filename, data):
    """Receive file from client via RPC"""
    try:
        file_data = base64.b64decode(data.encode())
        with open(filename, 'wb') as f:
            f.write(file_data)
        return f"File {filename} uploaded successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

server = SimpleXMLRPCServer((HOST, PORT))
server.register_function(upload_file, "upload_file")
print(f"RPC Server listening on {HOST}:{PORT}")
server.serve_forever()
