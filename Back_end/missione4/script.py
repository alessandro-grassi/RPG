from Back_end import queryLib
import json
import random

# Liste delle parole per il Wordle e delle soluzioni finali
parole_wordle = ["pesca", "monte", "luogo", "tempo", "libro", "fiume", "canto", "passo", "vista", "fiore"]
parole_finali = ["enigma", "tesoro", "vittoria", "mistero", "successo"]

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

# Inizializzazione del database
parola_corrente = random.choice(parole_wordle)
parola_finale = random.choice(parole_finali)

# Simulazione database con JSON
DB = json.dumps({
    "obiettivo": "Risolvi i Wordle per ottenere indizi e scoprire la parola finale!",
    "ricompensa": "Una sorpresa speciale!",
    "tentativiGioco": 5,
    "tentativiGiocoFatti": 0,
    "tentativiIndovina": 3,
    "tentativiIndovinaFatti": 0,
    "parolaCorrente": parola_corrente,
    "parolaFinale": parola_finale,
    "indiziOttenuti": []
})

dbDict = json.loads(DB)

def check_get(path):
    # Apre pagina principale
    if path == "/missione4":
        f = open("Missioni/Missione4/primapagina.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    # Apre il css
    elif path.endswith("stile"):
        f = open("Missioni/Missione4/stile.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    # Apre la pagina per indovinare
    elif path.endswith("indovina"):
        f = open("Missioni/Missione4/indovina_soluzione.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    # Apre la pagina per giocare
    elif path.endswith("gioca"):
        f = open("Missioni/Missione4/wordle.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    # Torna alla home
    elif path.endswith("sm_home"):
        f = open("SceltaMissione/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    # API: Dettagli generali
    elif path.endswith("dettagliGenerali"):
        return json.dumps(getDettagliGenerali()).encode("utf-8")
    
    # API: Dettagli gioco
    elif "dettagliGioco" in path:
        return json.dumps(getDettagliGioco()).encode("utf-8")
    
    # API: Indizi
    elif path.endswith("indizi"):
        return json.dumps({"indizi": dbDict["indiziOttenuti"]}).encode("utf-8")
    
    # API: Tentativi rimasti
    elif path.endswith("tentativi-rimasti"):
        return json.dumps({"tentativiRimasti": dbDict["tentativiGioco"] - dbDict["tentativiGiocoFatti"]}).encode("utf-8")
    
    # Se non trova il path
    return '"Path not found"'.encode("utf-8")

def check_post(path, client_choice):
    if path.endswith("verifica-parola"):
        try:
            parola = client_choice.get("parola", "")
            risultato = verifica_parola(parola)
            return json.dumps(risultato).encode("utf-8")
        except Exception as errore:
            return json.dumps({"esito": "errore", "messaggio": str(errore)}).encode("utf-8")
    
    elif path.endswith("verifica-soluzione"):
        try:
            soluzione = client_choice.get("soluzione", "")
            risultato = verifica_soluzione_finale(soluzione)
            return json.dumps(risultato).encode("utf-8")
        except Exception as errore:
            return json.dumps({"esito": "errore", "messaggio": str(errore)}).encode("utf-8")
    
    return '"Path not found"'.encode("utf-8")

# Funzioni per simulare db
def getDettagliGenerali():
    return {
        "obiettivo": dbDict["obiettivo"],
        "ricompensa": dbDict["ricompensa"],
        "tentativiIndovina": dbDict["tentativiIndovina"],
        "tentativiIndovinaFatti": dbDict["tentativiIndovinaFatti"],
        "indiziOttenuti": dbDict["indiziOttenuti"],
        "maxIndizi": len(tutti_indizi[dbDict["parolaFinale"]])
    }

def getDettagliGioco():
    return {
        "tentativiGioco": dbDict["tentativiGioco"],
        "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"]
    }

# Funzione per verificare una parola nel Wordle
def verifica_parola(parola_tentativo):
    parola_corretta = dbDict["parolaCorrente"]
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
        if len(dbDict["indiziOttenuti"]) < len(tutti_indizi[dbDict["parolaFinale"]]):
            indizio_index = len(dbDict["indiziOttenuti"])
            dbDict["indiziOttenuti"].append(tutti_indizi[dbDict["parolaFinale"]][indizio_index])
        
        # Cambia la parola corrente per il prossimo round
        vecchia_parola = dbDict["parolaCorrente"]
        while dbDict["parolaCorrente"] == vecchia_parola:
            dbDict["parolaCorrente"] = random.choice(parole_wordle)
        
        return {
            "esito": "successo",
            "messaggio": "Complimenti! Hai indovinato la parola!",
            "risultato": risultato
        }
    else:
        dbDict["tentativiGiocoFatti"] += 1
        
        if dbDict["tentativiGiocoFatti"] >= dbDict["tentativiGioco"]:
            # Reimposta i tentativi e cambia la parola
            dbDict["tentativiGiocoFatti"] = 0
            vecchia_parola = dbDict["parolaCorrente"]
            while dbDict["parolaCorrente"] == vecchia_parola:
                dbDict["parolaCorrente"] = random.choice(parole_wordle)
            
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
    soluzione_corretta = dbDict["parolaFinale"]
    
    dbDict["tentativiIndovinaFatti"] += 1
    
    if soluzione_tentativo.lower() == soluzione_corretta.lower():
        # L'utente ha vinto il gioco!
        return {
            "esito": "successo",
            "messaggio": f"Congratulazioni! Hai risolto l'enigma finale: {soluzione_corretta}!"
        }
    elif dbDict["tentativiIndovinaFatti"] >= dbDict["tentativiIndovina"]:
        return {
            "esito": "fallimento",
            "messaggio": "Hai esaurito i tentativi! Missione fallita."
        }
    else:
        return {
            "esito": "errore",
            "messaggio": f"Soluzione errata, raccogli più indizi! Tentativi rimasti: {dbDict['tentativiIndovina'] - dbDict['tentativiIndovinaFatti']}"
        }
