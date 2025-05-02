import json
import os
import random
from pathlib import Path
from urllib.parse import urlparse

# directories -------------------------------
BASE_DIR = Path(__file__).parent.parent.parent  # directory base, RPG
HTML_DIR = BASE_DIR / "Missioni" / "Missione4"  # directory missione4
DB_PATH = Path(__file__).parent / "database.json" # directory database.json
# -------------------------------------------

# GET e POST --------------------------------
# gestore GET
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

# gestore POST
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
# --------------------------------------------------------

# gestione DATABASE (json) -------------------------------
def carica_database():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File database non trovato in: {DB_PATH}")
    
    # Inizializza le parole random
    db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
    db["stato_gioco"]["parola_finale"] = random.choice(db["parole_finali"])
    salva_database(db)
    return db

def salva_database(db):
    # Assicurati che la directory esista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2)

# Carica il database all'avvio
db = carica_database()
print(f"Database caricato. Parola corrente: {db['stato_gioco']['parola_corrente']}, Parola finale: {db['stato_gioco']['parola_finale']}")
# --------------------------------------------------------

# gestione GIOCO -----------------------------------------
# verificare una parola nel Wordle -----------------------
def verifica_parola(parola_tentativo):
    global db
    parola_corretta = db["stato_gioco"]["parola_corrente"]
    parola_tentativo = parola_tentativo.lower()
    
    print(f"Verifica parola: tentativo '{parola_tentativo}', corretta '{parola_corretta}'")
    
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
            nuovo_indizio = indizi_disponibili[indizio_index]
            db["stato_gioco"]["indizi_sbloccati"].append(nuovo_indizio)
            print(f"Indizio sbloccato: {nuovo_indizio}")
        
        # Cambia la parola corrente per il prossimo round
        vecchia_parola = db["stato_gioco"]["parola_corrente"]
        while db["stato_gioco"]["parola_corrente"] == vecchia_parola:
            db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
        
        print(f"Nuova parola corrente: {db['stato_gioco']['parola_corrente']}")
        salva_database(db)
        
        return {
            "esito": "successo",
            "messaggio": "Complimenti! Hai indovinato la parola!",
            "risultato": risultato
        }
    else:
        db["stato_gioco"]["tentativi_rimasti"] -= 1
        tentativi_rimasti = db["stato_gioco"]["tentativi_rimasti"]
        print(f"Tentativo errato. Tentativi rimasti: {tentativi_rimasti}")
        salva_database(db)
        
        if tentativi_rimasti <= 0:
            # Reimposta i tentativi e cambia la parola
            db["stato_gioco"]["tentativi_rimasti"] = 5
            vecchia_parola = db["stato_gioco"]["parola_corrente"]
            while db["stato_gioco"]["parola_corrente"] == vecchia_parola:
                db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
            
            print(f"Tentativi esauriti. Nuova parola corrente: {db['stato_gioco']['parola_corrente']}")
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

# verificare la soluzione finale ------------------------
def verifica_soluzione_finale(soluzione_tentativo):
    soluzione_corretta = db["stato_gioco"]["parola_finale"]
    
    print(f"Verifica soluzione finale: tentativo '{soluzione_tentativo}', corretta '{soluzione_corretta}'")
    
    if soluzione_tentativo.lower() == soluzione_corretta.lower():
        # L'utente ha vinto il gioco!
        print("Soluzione corretta! Vittoria!")
        return {
            "esito": "successo",
            "messaggio": f"Congratulazioni! Hai risolto l'enigma finale: {soluzione_corretta}!"
        }
    else:
        print("Soluzione errata")
        return {
            "esito": "errore",
            "messaggio": "Soluzione errata, raccogli più indizi!"
        }
# --------------------------------------------------------