from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
dict = { # dizionario per prendere i suffissi dei moduli da aggiungere
    
}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        path = self.path
        path = urlparse(path).path

        resp = check_get(path)

        self.wfile.write(resp)
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

        self.wfile.write(resp)
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
    for suffisso, modulo in dict.items():
        if path.startswith(suffisso):
            return modulo.check_get(path)
    return "Modulo non trovato".encode("utf-8")


def check_post(path, client_choice):
    for suffisso, modulo in dict.items():
        if path.startswith(suffisso):
            return modulo.check_post(path, client_choice)
    return "Modulo non trovato".encode("utf-8")


if __name__ == "__main__":
    run_server()
