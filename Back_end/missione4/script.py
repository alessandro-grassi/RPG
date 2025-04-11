import json
import sys
import random

# Liste delle parole per il Wordle e delle soluzioni finali
parole_wordle = ["pesca", "monte", "luogo", "tempo", "libro", "fiume", "canto", "passo", "vista", "fiore"]
parole_finali = ["enigma", "tesoro", "vittoria", "mistero", "successo"]

# Variabili di stato del gioco
stato_gioco = {
    "tentativi_rimasti": 5,
    "indizi_sbloccati": [],
    "parola_corrente": random.choice(parole_wordle),
    "parola_finale": random.choice(parole_finali)
}

# Indizi per le parole finali
tutti_indizi = {
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

# Funzione per verificare una parola nel Wordle
def verifica_parola(parola_tentativo):
    parola_corretta = stato_gioco["parola_corrente"]
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
        if len(stato_gioco["indizi_sbloccati"]) < len(tutti_indizi[stato_gioco["parola_finale"]]):
            indizio_index = len(stato_gioco["indizi_sbloccati"])
            stato_gioco["indizi_sbloccati"].append(tutti_indizi[stato_gioco["parola_finale"]][indizio_index])
            # Cambia la parola corrente per il prossimo round
            vecchia_parola = stato_gioco["parola_corrente"]
            while stato_gioco["parola_corrente"] == vecchia_parola:
                stato_gioco["parola_corrente"] = random.choice(parole_wordle)
        
        return {
            "esito": "successo",
            "messaggio": "Complimenti! Hai indovinato la parola!",
            "risultato": risultato
        }
    else:
        stato_gioco["tentativi_rimasti"] -= 1
        if stato_gioco["tentativi_rimasti"] <= 0:
            # Reimposta i tentativi e cambia la parola
            stato_gioco["tentativi_rimasti"] = 5
            vecchia_parola = stato_gioco["parola_corrente"]
            while stato_gioco["parola_corrente"] == vecchia_parola:
                stato_gioco["parola_corrente"] = random.choice(parole_wordle)
            
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
    soluzione_corretta = stato_gioco["parola_finale"]
    
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

def check_get(path):
    if path == "/missione4" or path == "/missione4/":  # pagina principale
        f = open(sys.path[0] + "/Missioni/Missione4/vers2/prima_pagina.html", "r", encoding="utf-8")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    elif path == "/missione4/wordle.html":
        f = open(sys.path[0] + "/Missioni/Missione4/vers2/wordle.html", "r", encoding="utf-8")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    elif path == "/missione4/prima_pagina.html":
        f = open(sys.path[0] + "/Missioni/Missione4/vers2/prima_pagina.html", "r", encoding="utf-8")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    elif path == "/missione4/indovina_soluzione.html":
        f = open(sys.path[0] + "/Missioni/Missione4/vers2/indovina_soluzione.html", "r", encoding="utf-8")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    elif path == "/missione4/stile.css":
        f = open(sys.path[0] + "/Missioni/Missione4/vers2/stile.css", "r", encoding="utf-8")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    elif path == "/missione4/api/indizi":
        risposta = json.dumps({"indizi": stato_gioco["indizi_sbloccati"]})
        return risposta.encode("utf-8")
    elif path == "/missione4/api/tentativi-rimasti":
        risposta = json.dumps({"tentativiRimasti": stato_gioco["tentativi_rimasti"]})
        return risposta.encode("utf-8")
    return '"Path not found"'.encode("utf-8")

def check_post(path, client_choice):
    if path == "/missione4/api/verifica-parola":
        try:
            parola = client_choice["parola"]
            risultato = verifica_parola(parola)
            return json.dumps(risultato).encode("utf-8")
        except Exception as errore:
            return '"errore"'.encode("utf-8")
    elif path == "/missione4/api/verifica-soluzione":
        try:
            soluzione = client_choice["soluzione"]
            risultato = verifica_soluzione_finale(soluzione)
            return json.dumps(risultato).encode("utf-8")
        except Exception as errore:
            return '"errore"'.encode("utf-8")
    return '"Path not found"'.encode("utf-8")