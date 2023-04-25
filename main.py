from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

host_name = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('Hello, World wide web', "utf-8"))


if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port), MyServer)
    print('Всё хокей')

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
