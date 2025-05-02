import json
from .script import verifica_parola, verifica_soluzione_finale, leggi_file, db

# Funzioni per l'interfaccia con server.py
def check_get(path):
    if path == "/missione4/":
        return leggi_file("prima_pagina.html").encode()
    elif path == "/missione4/wordle.html":
        return leggi_file("wordle.html").encode()
    elif path == "/missione4/prima_pagina.html":
        return leggi_file("prima_pagina.html").encode()
    elif path == "/missione4/indovina_soluzione.html":
        return leggi_file("indovina_soluzione.html").encode()
    elif path == "/missione4/stile.css":
        return leggi_file("stile.css").encode()
    elif path == "/missione4/api/indizi":
        return json.dumps({"indizi": db["stato_gioco"]["indizi_sbloccati"]}).encode()
    elif path == "/missione4/api/tentativi-rimasti":
        return json.dumps({"tentativiRimasti": db["stato_gioco"]["tentativi_rimasti"]}).encode()
    else:
        return "Pagina non trovata".encode()

def check_post(path, client_choice):
    if path == "/missione4/api/verifica-parola":
        parola = client_choice.get("parola", "")
        risultato = verifica_parola(parola)
        return json.dumps(risultato).encode()
    elif path == "/missione4/api/verifica-soluzione":
        soluzione = client_choice.get("soluzione", "")
        risultato = verifica_soluzione_finale(soluzione)
        return json.dumps(risultato).encode()
    else:
        return "API non trovata".encode()
