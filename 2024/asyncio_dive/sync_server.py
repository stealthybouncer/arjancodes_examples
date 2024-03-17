import socket
import time

class Server:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"Server started at http://{self.host}:{self.port}")
            self.accept_connections()
        finally:
            self.server_socket.close()

    def accept_connections(self):
        while True:
            conn, addr = self.server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                request_handler = RequestHandler(conn)
                request_handler.process_request()

class RequestHandler:
    def __init__(self, conn):
        self.conn = conn

    def process_request(self):
        request = self.conn.recv(1024).decode('utf-8')
        print(f"Request: {request}")
        self.handle_request(request)

    def handle_request(self, request):
        path = self.get_path(request)
        response = self.generate_response(path)
        self.conn.sendall(response.encode())

    def get_path(self, request):
        try:
            path = request.split(' ')[1]
            if path == '/':
                return 'index.html'
            return path
        except IndexError:
            return 'index.html'

    def generate_response(self, path):
        time.sleep(2)
        try:
            with open(path, 'r') as file:
                response_body = file.read()
            response_header = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        except FileNotFoundError:
            response_body = "<html><body><h1>404 Not Found</h1></body></html>"
            response_header = "HTTP/1.1 404 Not Found\n\n"
        return response_header + response_body

if __name__ == "__main__":
    def main():
        server = Server()
        server.start()
    
    main()