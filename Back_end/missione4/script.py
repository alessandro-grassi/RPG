import json
import os
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

# Percorsi dei file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML_DIR = os.path.join(BASE_DIR, "Missioni", "Missione4")
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")

# Funzioni per gestire il database JSON
def carica_database():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # Se il file non esiste, lo creiamo con valori predefiniti
        db = {
            "parole_wordle": ["pesca", "monte", "luogo", "tempo", "libro", "fiume", "canto", "passo", "vista", "fiore"],
            "parole_finali": ["enigma", "tesoro", "vittoria", "mistero", "successo"],
            "stato_gioco": {
                "tentativi_rimasti": 5,
                "indizi_sbloccati": [],
                "parola_corrente": "",
                "parola_finale": ""
            },
            "tutti_indizi": {
                "enigma": [
                    "Un rompicapo che sfida la mente",
                    "Deriva dal greco 'ainigma', che significa 'parlare in modo oscuro'",
                    "Spesso richiede un salto logico per essere risolto"
                ],
                "tesoro": [
                    "Oggetto di grande valore",
                    "Spesso nascosto e protetto",
                    "Cercato dai cacciatori di fortuna"
                ],
                "vittoria": [
                    "Rappresenta il trionfo dopo la lotta",
                    "È simboleggiata da una corona d'alloro",
                    "Deriva dal latino 'victoria'"
                ],
                "mistero": [
                    "Ciò che rimane incomprensibile",
                    "Deriva dal greco 'mysterion'",
                    "Richiede indagine e scoperta"
                ],
                "successo": [
                    "Raggiungimento di un obiettivo",
                    "Deriva dal latino 'successus', che significa 'avanzare'",
                    "Ricompensa per l'impegno e la perseveranza"
                ]
            }
        }
        # Inizializza le parole random
        db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
        db["stato_gioco"]["parola_finale"] = random.choice(db["parole_finali"])
        salva_database(db)
        return db

def salva_database(db):
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2)

# Carica il database all'avvio
db = carica_database()

# Funzione per leggere i file HTML
def leggi_file(nome_file):
    try:
        with open(os.path.join(HTML_DIR, nome_file), "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"File {nome_file} non trovato"

# Funzione per verificare una parola nel Wordle
def verifica_parola(parola_tentativo):
    global db
    parola_corretta = db["stato_gioco"]["parola_corrente"]
    parola_tentativo = parola_tentativo.lower()
    
    if len(parola_tentativo) != 5:
        return {"esito": "errore", "messaggio": "La parola deve essere di 5 lettere"}
    
    risultato = []
    for i in range(5):
        if i < len(parola_tentativo):
            if parola_tentativo[i] == parola_corretta[i]:
                risultato.append({"lettera": parola_tentativo[i], "stato": "corretto"})
            elif parola_tentativo[i] in parola_corretta:
                risultato.append({"lettera": parola_tentativo[i], "stato": "posizione_errata"})
            else:
                risultato.append({"lettera": parola_tentativo[i], "stato": "non_presente"})
    
    if parola_tentativo == parola_corretta:
        # Sblocca un indizio
        indizi_disponibili = db["tutti_indizi"][db["stato_gioco"]["parola_finale"]]
        if len(db["stato_gioco"]["indizi_sbloccati"]) < len(indizi_disponibili):
            indizio_index = len(db["stato_gioco"]["indizi_sbloccati"])
            db["stato_gioco"]["indizi_sbloccati"].append(indizi_disponibili[indizio_index])
        
        # Cambia la parola corrente per il prossimo round
        vecchia_parola = db["stato_gioco"]["parola_corrente"]
        while db["stato_gioco"]["parola_corrente"] == vecchia_parola:
            db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
        salva_database(db)
        
        return {
            "esito": "successo",
            "messaggio": "Complimenti! Hai indovinato la parola!",
            "risultato": risultato
        }
    else:
        db["stato_gioco"]["tentativi_rimasti"] -= 1
        salva_database(db)
        
        if db["stato_gioco"]["tentativi_rimasti"] <= 0:
            # Reimposta i tentativi e cambia la parola
            db["stato_gioco"]["tentativi_rimasti"] = 5
            vecchia_parola = db["stato_gioco"]["parola_corrente"]
            while db["stato_gioco"]["parola_corrente"] == vecchia_parola:
                db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
            salva_database(db)
            
            return {
                "esito": "fallimento",
                "messaggio": f"Tentativi esauriti! La parola era: {parola_corretta}. Ne ho scelta una nuova.",
                "risultato": risultato
            }
        
        return {
            "esito": "errore",
            "messaggio": "Parola errata, riprova!",
            "risultato": risultato
        }

# Funzione per verificare la soluzione finale
def verifica_soluzione_finale(soluzione_tentativo):
    soluzione_corretta = db["stato_gioco"]["parola_finale"]
    
    if soluzione_tentativo.lower() == soluzione_corretta.lower():
        # L'utente ha vinto il gioco!
        return {
            "esito": "successo",
            "messaggio": f"Congratulazioni! Hai risolto l'enigma finale: {soluzione_corretta}!"
        }
    else:
        return {
            "esito": "errore",
            "messaggio": "Soluzione errata, raccogli più indizi!"
        }

# Classe per gestire le richieste HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type="text/html"):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_OPTIONS(self):
        self._set_headers()
    
    def do_GET(self):
        path = self.path
        
        if path == "/":
            self._set_headers()
            self.wfile.write(leggi_file("prima_pagina.html").encode())
        elif path == "/wordle.html":
            self._set_headers()
            self.wfile.write(leggi_file("wordle.html").encode())
        elif path == "/prima_pagina.html":
            self._set_headers()
            self.wfile.write(leggi_file("prima_pagina.html").encode())
        elif path == "/indovina_soluzione.html":
            self._set_headers()
            self.wfile.write(leggi_file("indovina_soluzione.html").encode())
        elif path == "/stile.css":
            self._set_headers("text/css")
            self.wfile.write(leggi_file("stile.css").encode())
        elif path == "/api/indizi":
            self._set_headers("application/json")
            response = json.dumps({"indizi": db["stato_gioco"]["indizi_sbloccati"]})
            self.wfile.write(response.encode())
        elif path == "/api/tentativi-rimasti":
            self._set_headers("application/json")
            response = json.dumps({"tentativiRimasti": db["stato_gioco"]["tentativi_rimasti"]})
            self.wfile.write(response.encode())
        else:
            self._set_headers()
            self.wfile.write("Pagina non trovata".encode())
    
    def do_POST(self):
        path = self.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        if path == "/api/verifica-parola":
            parola = data.get("parola", "")
            risultato = verifica_parola(parola)
            self._set_headers("application/json")
            self.wfile.write(json.dumps(risultato).encode())
        elif path == "/api/verifica-soluzione":
            soluzione = data.get("soluzione", "")
            risultato = verifica_soluzione_finale(soluzione)
            self._set_headers("application/json")
            self.wfile.write(json.dumps(risultato).encode())
        else:
            self._set_headers()
            self.wfile.write("API non trovata".encode())

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server in ascolto sulla porta {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
