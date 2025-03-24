#gita a monaco: 7/10
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from Back_end import select_mis as sm

mods = {
    "/sm_" : sm
}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        path = self.path
        path = urlparse(path).path

        resp = check_get(path)

        self.wfile.write(json.dumps(resp).encode("utf-8"))
        return

    def do_POST(self):
        self.send_response(200)
        # self.send_header("Content-type", "application/json")
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
    for k in mods.keys():
        if path.startswith(k):
            return mods[k].check_get(path)


def check_post(path, client_choice):
    for k in mods.keys():
        if path.startswith(k):
            return mods[k].check_post(path,client_choice)


if __name__ == "__main__":
    run_server()
