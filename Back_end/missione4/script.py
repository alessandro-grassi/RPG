import json
import os
import random
from pathlib import Path

# Otteniamo il percorso assoluto della directory base RPG
BASE_DIR = Path(__file__).parent.parent.parent
# Percorso assoluto alla directory dei file HTML
HTML_DIR = BASE_DIR / "Missioni" / "Missione4"
# Percorso assoluto al file database nella stessa cartella dello script
DB_PATH = Path(__file__).parent / "database.json"

# Funzioni per gestire il database JSON
def carica_database():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File database non trovato in: {DB_PATH}")
        print("Creazione di un nuovo database...")
        
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
    # Assicurati che la directory esista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2)

# Carica il database all'avvio
db = carica_database()
print(f"Database caricato. Parola corrente: {db['stato_gioco']['parola_corrente']}, Parola finale: {db['stato_gioco']['parola_finale']}")

# Funzione per verificare una parola nel Wordle
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

# Funzione per verificare la soluzione finale
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