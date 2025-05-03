from http.server import BaseHTTPRequestHandler, HTTPServer
from Back_end import jslib
import json
from urllib.parse import urlparse
import Back_end.modulo_missione5 as m5
from Back_end import login, jslib, personaggio
from Back_end import complete_mission as cm
dict = { # dizionario per prendere i suffissi dei moduli da aggiungere
    "/cm" : cm,
    "/jslib": jslib,
    "/m5": m5,
    "/login": login,
    "/jslib": jslib,
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
    if path=="/favicon.ico":
        f = open("Config/logo magi.ico","rb")
        r = f.read()
        f.close()
        return r
    elif path=="/":
        return "<script>window.location='http://localhost:8080/login'</script>".encode("utf-8")
    return "Modulo non trovato".encode("utf-8")


def check_post(path, client_choice):
    for suffisso, modulo in dict.items():
        if path.startswith(suffisso):
            return modulo.check_post(path, client_choice)
    return "Modulo non trovato"


if __name__ == "__main__":
    run_server()