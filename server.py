import http.server
import socketserver
import socket

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
ip = socket.gethostbyname(socket.gethostname())

with socketserver.TCPServer((ip, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()