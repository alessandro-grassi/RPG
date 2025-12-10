import json
import os
import random
from pathlib import Path
from urllib.parse import urlparse

# directories ----------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent.parent.parent # directory base, RPG
HTML_DIR = BASE_DIR / "Missioni" / "Missione4a" # directory missione4a
DB_PATH = Path(__file__).parent / "database.json" # directory database.json
# ----------------------------------------------------------------------------------------

# GET e POST -----------------------------------------------------------------------------
# gestore GET ----------------------------------------------------------------------------
def check_get(path):
    path = urlparse(path).path
    
    # API per ottenere i tentativi rimasti
    if path == "/missione4a/api/tentativi-rimasti":
        db = carica_database()
        tentativi_rimasti = db["stato_gioco"]["tentativi_rimasti"]
        return json.dumps({"tentativiRimasti": tentativi_rimasti}).encode("utf-8")
    
    # API per ottenere informazioni sulla difficoltà
    elif path == "/missione4a/api/info-difficolta":
        db = carica_database()
        parola_finale = db["stato_gioco"]["parola_finale"]
        totale_indizi = len(db["tutti_indizi"][parola_finale])
        
        return json.dumps({
            "totaleIndizi": totale_indizi
        }).encode("utf-8")
    
    # API per ottenere gli indizi sbloccati
    elif path == "/missione4a/api/indizi":
        db = carica_database()
        indizi = db["stato_gioco"]["indizi_sbloccati"]
        
        # Controlla se tutti gli indizi sono stati sbloccati
        parola_finale = db["stato_gioco"]["parola_finale"]
        tutti_indizi_disponibili = db["tutti_indizi"][parola_finale]
        indizi_tutti_sbloccati = len(indizi) >= len(tutti_indizi_disponibili)
        
        return json.dumps({
            "indizi": indizi,
            "tuttiIndiziSbloccati": indizi_tutti_sbloccati
        }).encode("utf-8")
    
    # Servi i file HTML, CSS e JS
    else:
        file_path = None
        
        # Mappatura tra URL e file
        if path == "/missione4a" or path == "/missione4a/":
            file_path = HTML_DIR / "Prima_pagina.html"
        elif path == "/missione4a/wordle":
            # Prima di servire la pagina Wordle, controlla se tutti gli indizi sono già stati sbloccati
            db = carica_database()
            indizi = db["stato_gioco"]["indizi_sbloccati"]
            parola_finale = db["stato_gioco"]["parola_finale"]
            tutti_indizi_disponibili = db["tutti_indizi"][parola_finale]
            
            if len(indizi) >= len(tutti_indizi_disponibili):
                # Reindirizza alla pagina principale con un messaggio
                return """
                <script>
                alert('Hai già sbloccato tutti gli indizi! Vai alla pagina per indovinare la soluzione.');
                window.location.href = '/missione4a/';
                </script>
                """.encode("utf-8")
            
            file_path = HTML_DIR / "Wordle.html"
        elif path == "/missione4a/primapagina":
            file_path = HTML_DIR / "Prima_pagina.html"
        elif path == "/missione4a/indovinasoluzione":
            file_path = HTML_DIR / "Indovina_soluzione.html"
        elif path == "/missione4a/stile":
            file_path = HTML_DIR / "Stile.css"
        
        if file_path and file_path.exists():
            with open(file_path, 'rb') as file:
                content = file.read()
            return content
        
        return f"File non trovato: {path}".encode("utf-8")

# gestore POST ------------------------------------------------------------------------------
def check_post(path, client_choice):
    path = urlparse(path).path
    
    # API per verificare una parola del Wordle
    if path == "/missione4a/api/verifica-parola":
        if "parola" in client_choice:
            # Prima di verificare, controlla se tutti gli indizi sono già stati sbloccati
            db = carica_database()
            indizi = db["stato_gioco"]["indizi_sbloccati"]
            parola_finale = db["stato_gioco"]["parola_finale"]
            tutti_indizi_disponibili = db["tutti_indizi"][parola_finale]
            
            if len(indizi) >= len(tutti_indizi_disponibili):
                return json.dumps({
                    "esito": "errore", 
                    "messaggio": "Hai già sbloccato tutti gli indizi! Non puoi giocare ulteriormente."
                }).encode("utf-8")
                
            result = verifica_parola(client_choice["parola"])
            return json.dumps(result).encode("utf-8")
    
    # API per verificare la soluzione finale
    elif path == "/missione4a/api/verifica-soluzione":
        if "soluzione" in client_choice:
            result = verifica_soluzione_finale(client_choice["soluzione"])
            return json.dumps(result).encode("utf-8")
    
    return json.dumps({"esito": "errore", "messaggio": "Richiesta non valida"}).encode("utf-8")

# gestione DATABASE (json) --------------------------------------------------------------------
def carica_database():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File database non trovato in: {DB_PATH}")
    
    salva_database(db)
    return db

def salva_database(db):
    # Assicurati che la directory esista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2)

def carica_database_avvio():
    db = carica_database()

    #scelta parole
    db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
    db["stato_gioco"]["parola_finale"] = random.choice(db["parole_finali"])
    #reimposta gioco ogni avvio
    db["stato_gioco"]["tentativi_rimasti"] = 5
    db["stato_gioco"]["tentativi_nella_partita_corrente"] = 0
    db["stato_gioco"]["indizi_sbloccati"] = []

    salva_database(db)
    return db

# Carica il database all'avvio
db = carica_database_avvio()
print(f"Database caricato. Parola corrente: {db['stato_gioco']['parola_corrente']}, Parola finale: {db['stato_gioco']['parola_finale']}")

# gestione GIOCO ------------------------------------------------------------------------
# verificare una parola nel Wordle ------------------------------------------------------
def verifica_parola(parola_tentativo):
    global db
    parola_corretta = db["stato_gioco"]["parola_corrente"]
    parola_tentativo = parola_tentativo.lower()
    
    print(f"Verifica parola: tentativo '{parola_tentativo}', corretta '{parola_corretta}'")
    
    # Controlla se tutti gli indizi sono già stati sbloccati
    parola_finale = db["stato_gioco"]["parola_finale"]
    indizi_disponibili = db["tutti_indizi"][parola_finale]
    
    if len(db["stato_gioco"]["indizi_sbloccati"]) >= len(indizi_disponibili):
        return {
            "esito": "errore", 
            "messaggio": "Hai già sbloccato tutti gli indizi! Non puoi giocare ulteriormente."
        }
    
    if len(parola_tentativo) != 5:  #se la lettera non è da 5 lettere
        return {"esito": "errore", "messaggio": "La parola deve essere di 5 lettere"}
    
    #inizializza il risultato con tutte le lettere segnate come non presenti
    risultato = [{"lettera": parola_tentativo[i], "stato": "non_presente"} for i in range(5)]
    
    
    lettere_disponibili = list(parola_corretta) #array con le lettere giuste
    
    #colora le lettere corrette in verde
    for i in range(5):
        if parola_tentativo[i] == lettere_disponibili[i]:
            risultato[i]["stato"] = "corretto"
            # Segna questa posizione come utilizzata
            lettere_disponibili[i] = None
    
    #colora le lettere semi-errate in giallo
    for i in range(5):
        if risultato[i]["stato"] == "non_presente":  # Salta posizioni già corrette
            for j in range(5):
                if lettere_disponibili[j] is not None and parola_tentativo[i] == lettere_disponibili[j]:
                    risultato[i]["stato"] = "posizione_errata"
                    lettere_disponibili[j] = None
                    break
    
    #se becca la parola
    if parola_tentativo == parola_corretta:
        #scrive l'indizio
        indizi_disponibili = db["tutti_indizi"][db["stato_gioco"]["parola_finale"]]
        if len(db["stato_gioco"]["indizi_sbloccati"]) < len(indizi_disponibili):
            indizio_index = len(db["stato_gioco"]["indizi_sbloccati"])
            nuovo_indizio = indizi_disponibili[indizio_index]
            db["stato_gioco"]["indizi_sbloccati"].append(nuovo_indizio)
            
        #-1 contatore delle partite rimaste
        db["stato_gioco"]["tentativi_rimasti"] -= 1
        
        #reset contatore dei tentativi
        db["stato_gioco"]["tentativi_nella_partita_corrente"] = 0
        
        #cambia la parola per il prossimo round
        vecchia_parola = db["stato_gioco"]["parola_corrente"]
        while db["stato_gioco"]["parola_corrente"] == vecchia_parola:
            db["stato_gioco"]["parola_corrente"] = random.choice(db["parole_wordle"])
        
        # Controlla se dopo aver aggiunto l'indizio abbiamo sbloccato tutti gli indizi
        tutti_indizi_sbloccati = len(db["stato_gioco"]["indizi_sbloccati"]) >= len(indizi_disponibili)
        messaggio_aggiuntivo = ""
        
        if tutti_indizi_sbloccati:
            messaggio_aggiuntivo = " Hai sbloccato tutti gli indizi disponibili! Ora puoi provare a indovinare la soluzione finale."
        
        salva_database(db)
        
        return {
            "esito": "successo",
            "messaggio": f"Complimenti! Hai indovinato la parola!{messaggio_aggiuntivo}",
            "risultato": risultato,
            "tuttiIndiziSbloccati": tutti_indizi_sbloccati
        }
    #se non becca la parola
    else:
        # Inizializza o incrementa i tentativi nella partita corrente
        if "tentativi_nella_partita_corrente" not in db["stato_gioco"]:
            db["stato_gioco"]["tentativi_nella_partita_corrente"] = 1
        else:
            db["stato_gioco"]["tentativi_nella_partita_corrente"] += 1
        
        tentativi_nella_partita = db["stato_gioco"]["tentativi_nella_partita_corrente"]
        print(f"Tentativo errato. Tentativi nella partita: {tentativi_nella_partita}")
        
        #al quinto tentativo, partita persa
        if tentativi_nella_partita >= 5:
            db["stato_gioco"]["tentativi_rimasti"] -= 1
            db["stato_gioco"]["tentativi_nella_partita_corrente"] = 0
            
            tentativi_rimasti = db["stato_gioco"]["tentativi_rimasti"]
            print(f"Partita persa. Partite rimaste: {tentativi_rimasti}")
            
            #reimposta la parola
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
        
        salva_database(db)
        return {
            "esito": "errore",
            "messaggio": "Parola errata, riprova!",
            "risultato": risultato
        }

# verificare la soluzione finale -----------------------------------------------------------
def verifica_soluzione_finale(soluzione_tentativo):
    soluzione_corretta = db["stato_gioco"]["parola_finale"]
    print(f"Verifica soluzione finale: tentativo '{soluzione_tentativo}', corretta '{soluzione_corretta}'")
    
    if soluzione_tentativo.lower() == soluzione_corretta.lower():
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