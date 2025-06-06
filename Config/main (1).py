from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
import mis1
import mis2


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        path = self.path
        path = urlparse(path).path

        resp = check_get(path)

        self.wfile.write(json.dumps(resp).encode("utf-8"))
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        path = self.path
        path = urlparse(path).path

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b""
        client_choice = json.loads(post_data)

        resp = check_post(path, client_choice)

        self.wfile.write(json.dumps(resp).encode("utf-8"))
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def run_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server in esecuzione su http://localhost:8080...")
    httpd.serve_forever()


def check_get(path):
    if path.startswith("/m1_"):
        mis1.check_get(path)
        return 0
    if path.startswith("/m2_"):
        mis2.check_get(path)
        return 1


def check_post(path, client_choice):
    if path.startswith("/m1_"):
        mis1.check_post(path, client_choice)
        return 0
    if path.startswith("/m2_"):
        mis2.check_post(path, client_choice)
        return 1


if __name__ == "__main__":
    run_server()
