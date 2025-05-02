from Back_end import queryLib
import json

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
    
    # getDettagliGenerali
    elif path.endswith("dettagliGenerali"):
        return json.dumps(getDettagliGenerali()).encode("utf-8")
    
    # getDettagliGioco
    elif "dettagliGioco" in path:
        num = path.rsplit('/', 1)[-1] if '/' in path else 1
        return json.dumps(getDettagliGioco(int(num))).encode("utf-8")
    
    # Se non trova il path
    return '"Path not found"'.encode("utf-8")

def check_post(path, client_choice):
    if path.endswith("indovina"):
        try:
            tentativo = client_choice["tentativo"]
            risposta = client_choice["risposta"]
            return indovina(tentativo, risposta).encode("utf-8")
        except Exception as errore:
            return f'"errore: {str(errore)}"'.encode("utf-8")
    
    elif "controlla" in path:
        try:
            num = int(path.rsplit('/', 1)[-1])
            tentativo = client_choice["tentativo"]
            return controlla_wordle(num, tentativo).encode("utf-8")
        except Exception as errore:
            return f'"errore: {str(errore)}"'.encode("utf-8")
    
    return '"Path not found"'.encode("utf-8")

# PARTE PER SIMULARE DB
# JSON per simulare il db
DB = '{ "obiettivo": "scopri chi ha rapito Aldo Moro risolvendo i wordle!", ' \
     ' "ricompensa": "titolo di Kung Fury", ' \
     ' "tentativiIndovina": 3, ' \
     ' "tentativiIndovinaFatti": 0, ' \
     ' "tentativiGioco": 5, ' \
     ' "tentativiGiocoFatti": 0, ' \
     ' "soluzione": "gabibbo",' \
     ' "maxIndizi": 3,' \
     ' "indiziOttenuti":' \
     ' [' \
     ' ],' \
     ' "prove":' \
     ' [' \
     ' { "num": 1, "soluz": "trave", "ind": "usa spesso il termine BELANDI" },' \
     ' { "num": 2, "soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia" },' \
     ' { "num": 3, "soluz": "nonna", "ind": "è rosso" }' \
     ' ] }'

dbDict = json.loads(DB)

# Funzioni per simulare db
def getDettagliGenerali():
    return {
        "obiettivo": dbDict["obiettivo"],
        "ricompensa": dbDict["ricompensa"],
        "tentativiIndovina": dbDict["tentativiIndovina"],
        "tentativiIndovinaFatti": dbDict["tentativiIndovinaFatti"],
        "indiziOttenuti": dbDict["indiziOttenuti"],
        "maxIndizi": dbDict["maxIndizi"]
    }

def getDettagliGioco(num=1):
    prova = next((p for p in dbDict["prove"] if p["num"] == num), None)
    if prova:
        return {
            "tentativiGioco": dbDict["tentativiGioco"],
            "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"],
            "soluzione": prova["soluz"]
        }
    return {
        "tentativiGioco": dbDict["tentativiGioco"],
        "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"]
    }

def getVincita(num):
    prova = next((p for p in dbDict["prove"] if p["num"] == num), None)
    if prova:
        indizio = prova["ind"]
        if indizio not in dbDict["indiziOttenuti"]:
            dbDict["indiziOttenuti"].append(indizio)
        return indizio
    return "Indizio non trovato"

def getSoluzione(num):
    prova = next((p for p in dbDict["prove"] if p["num"] == num), None)
    return prova["soluz"] if prova else ""

def controlla_wordle(num, tentativo):
    soluzione = getSoluzione(num)
    if not soluzione:
        return json.dumps({"stato": "errore", "messaggio": "Prova non trovata"})
    
    if tentativo.lower() == soluzione.lower():
        indizio = getVincita(num)
        return json.dumps({"stato": "vittoria", "indizio": indizio})
    else:
        # Logica per verificare lettere corrette/posizione sbagliata
        risultato = []
        for i, lettera in enumerate(tentativo):
            if i < len(soluzione) and lettera.lower() == soluzione[i].lower():
                risultato.append({"lettera": lettera, "stato": "corretto"})
            elif lettera.lower() in soluzione.lower():
                risultato.append({"lettera": lettera, "stato": "presente"})
            else:
                risultato.append({"lettera": lettera, "stato": "assente"})
        
        dbDict["tentativiGiocoFatti"] += 1
        return json.dumps({
            "stato": "tentativo", 
            "risultato": risultato,
            "tentativiRimasti": dbDict["tentativiGioco"] - dbDict["tentativiGiocoFatti"]
        })

def indovina(tentativo, risposta):
    if dbDict["tentativiIndovinaFatti"] < dbDict["tentativiIndovina"]:
        dbDict["tentativiIndovinaFatti"] += 1
        if risposta.lower() == dbDict["soluzione"].lower():
            return json.dumps({"stato": "vittoria", "messaggio": "Complimenti! Hai indovinato la soluzione finale!"})
        else:
            return json.dumps({
                "stato": "errore", 
                "messaggio": "Risposta errata. Tentativi rimasti: " + 
                str(dbDict["tentativiIndovina"] - dbDict["tentativiIndovinaFatti"])
            })
    else:
        return json.dumps({"stato": "errore", "messaggio": "Tentativi esauriti"})
