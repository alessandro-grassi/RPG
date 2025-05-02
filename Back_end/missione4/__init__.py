from .script import *
import json
import os
from urllib.parse import urlparse, parse_qs
from pathlib import Path

# Otteniamo il percorso assoluto alla directory dei file HTML
BASE_DIR = Path(__file__).parent.parent.parent
HTML_DIR = BASE_DIR / "Missioni" / "Missione4"

# Funzione per controllare e gestire le richieste GET
def check_get(path):
    path = urlparse(path).path
    
    # API per ottenere i tentativi rimasti
    if path == "/missione4/api/tentativi-rimasti":
        db = carica_database()
        tentativi_rimasti = db["stato_gioco"]["tentativi_rimasti"]
        return json.dumps({"tentativiRimasti": tentativi_rimasti}).encode("utf-8")
    
    # API per ottenere gli indizi sbloccati
    elif path == "/missione4/api/indizi":
        db = carica_database()
        indizi = db["stato_gioco"]["indizi_sbloccati"]
        return json.dumps({"indizi": indizi}).encode("utf-8")
    
    # Servi i file HTML, CSS e JS
    else:
        file_path = None
        
        # Mappatura tra URL e file
        if path == "/missione4" or path == "/missione4/":
            file_path = HTML_DIR / "Prima_pagina.html"
        elif path == "/missione4/wordle.html":
            file_path = HTML_DIR / "Wordle.html"
        elif path == "/missione4/prima_pagina.html":
            file_path = HTML_DIR / "Prima_pagina.html"
        elif path == "/missione4/indovina_soluzione.html":
            file_path = HTML_DIR / "Indovina_soluzione.html"
        elif path == "/missione4/stile.css":
            file_path = HTML_DIR / "Stile.css"
        
        if file_path and file_path.exists():
            with open(file_path, 'rb') as file:
                content = file.read()
                return content
        
        return f"File non trovato: {path}".encode("utf-8")

# Funzione per controllare e gestire le richieste POST
def check_post(path, client_choice):
    path = urlparse(path).path
    
    # API per verificare una parola del Wordle
    if path == "/missione4/api/verifica-parola":
        if "parola" in client_choice:
            result = verifica_parola(client_choice["parola"])
            return json.dumps(result).encode("utf-8")
    
    # API per verificare la soluzione finale
    elif path == "/missione4/api/verifica-soluzione":
        if "soluzione" in client_choice:
            result = verifica_soluzione_finale(client_choice["soluzione"])
            return json.dumps(result).encode("utf-8")
    
    return json.dumps({"esito": "errore", "messaggio": "Richiesta non valida"}).encode("utf-8")