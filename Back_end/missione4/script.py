from Back_end import queryLib
import json #simulo il db

#la parte post e coneessione al DB la tengo buona ma non so se conviene farla qui o su modulo
def aggiungi_utente(user, pw, em):
    queryLib.connetti()
    a= queryLib.execute(f'''INSERT INTO "utenti" (username, hash, email) VALUES ('{user}','{pw}','{em}')''')
    b=a
    queryLib.disconnetti()

def utente_registrato(user, pw):
    flag = 0
    queryLib.connetti()
    flag = queryLib.execute(f'''SELECT username, hash FROM "utenti" WHERE username='{user}';''')
    queryLib.disconnetti()
    return len(flag)==1 and flag[0][1]==pw




def check_get(path):
    #apre pagina principale
    if path == "/missione4":  
        f = open("Missioni/Missione4/primapagina.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #apre il css
    elif path.endswith("stile"):
        f = open("Missioni/Missione4/stile.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #apre la pagina per indovinare
    elif path.endswith("indovina"):
        f = open("Missioni/Missione4/indovina_soluzione.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #apre la pagina per giocare
    elif path.endswith("gioca"):
        f = open("Missioni/Missione4/wordle.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #torna alla home
    elif path.endswith("sm_home"):
        f = open("SceltaMissione/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #pagina vittoria
    elif path.endswith("vittoria"):
        f = open("Missioni/Missione4/vittoria.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #pagina sconfitta
    elif path.endswith("sconfitta"):
        f = open("Missioni/Missione4/sconfitta.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    #getDetteagliGenerali
    elif path.endswith("dettagliGenerali"):
        return getDettagliGenerali()
    
    #getDettagliIndovina
    elif path.endswith("dettagliIndovina"):
        return getDettagliIndovina()
    
    #getDettagliGioco
    elif path.endswith("dettagliGioco"):
    #elif path.contains("dettagliGioco/"):
        return getDettagliGioco()
    
    #reset dati gioco
    elif path.endswith("resetGame"):
        return resetGame()
    
    #reset dati missione
    elif path.endswith("resetMissione"):
        try:
            print("resetMissione")
            return resetMissione()
        except Exception as errore:
            return json.dumps({"errore": str(errore)}).encode("utf-8")
    
    #get tentativo
    elif path.endswith("tentativo"):
        return getTentativo()
    
    #tentativi superati
    elif path.endswith("tentativiSuperati"):
        dbDict["indiziOttenuti"].append("")
        return 0
    
    '''
    elif path.endswith("trycookie"):
        f = open(sys.path[0] +"/SceltaPersonaggio/scelta.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")'''
    #se non trova il path
    return '"Path not found"'.encode("utf-8")




def check_post(path, client_choice):
    if path.endswith("registrazione"):
        try:
            username = client_choice["user"]
            password = client_choice["pw"]
            email = client_choice["mail"]
            aggiungi_utente(username, password, email)
            return "Registrazione effettuata con successo!".encode("utf-8")
        except Exception as errore:
            return '"errore"'.encode("utf-8")

    elif path.endswith("accesso"):
        try:
            username = client_choice["user"]
            password = client_choice["pw"]
            if(utente_registrato(username, password)):
                return '"Successo"'.encode("utf-8")
            else:
                return '"errore"'.encode("utf-8")
        except Exception as errore:
            return '"errore"'.encode("utf-8")
        
    elif path.endswith("controllaRisposta"):
        try:
            tentativo = client_choice["tentativo"]
            soluzione = client_choice["soluzione"]
            return controllaRisposta(tentativo, soluzione)
        except Exception as errore:
                return f'errore: {str(errore)}'.encode("utf-8")
    
    elif "controlla/" in path:
        try:
            num = path.rsplit('/', 1)[-1]
            tentativo = client_choice["tentativo"]
            risposta = client_choice["risposta"]
            return controlla(num, tentativo, risposta)
        except Exception as errore:
                return f'errore: {str(errore)}'.encode("utf-8")
    
    
    
    return '"Path not found"'.encode("utf-8")

    





#PARTE PER SIMULARE DB
#json per simulare il db
DB = '''{
    "obiettivo": "scopri chi ha rapito Aldo Moro risolvendo i wordle!",
    "ricompensa": "titolo di Kung Fury",
    "tentativiIndovina": 3,
    "tentativiIndovinaFatti": 0,
    "tentativiGioco": 5,
    "tentativiGiocoFatti": 0,
    "soluzione": "gabibbo",
    "maxIndizi": 3,
    "indiziOttenuti": [],
    "prove": [
        {"soluz": "nonna", "ind": "usa spesso il termine BELANDI"},
        {"soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia"},
        {"soluz": "trave", "ind": "è rosso"}
    ]
}'''

dbDict = json.loads(DB)


def getDettagliGenerali():
    dati = {
        "obiettivo": dbDict["obiettivo"],
        "ricompensa": dbDict["ricompensa"],
        "tentativiIndovina": dbDict["tentativiIndovina"],
        "tentativiIndovinaFatti": dbDict["tentativiIndovinaFatti"],
        "indiziOttenuti": dbDict["indiziOttenuti"],
        "maxIndizi": dbDict["maxIndizi"]
    }
    return json.dumps(dati).encode("utf-8")

def getDettagliIndovina():
    dati = {
        "tentativiIndovina": dbDict["tentativiIndovina"],
        "tentativiIndovinaFatti": dbDict["tentativiIndovinaFatti"],
        "indiziOttenuti": dbDict["indiziOttenuti"],
        "maxIndizi": dbDict["maxIndizi"]
    }
    return json.dumps(dati).encode("utf-8")

def getDettagliGioco():
    dati = {
        "tentativiGioco": dbDict["tentativiGioco"],
        "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"]
    }
    return json.dumps(dati).encode("utf-8")

def getSoluzione(num):
    tentDict = dbDict["prove"][num - 1]
    dbDict["indiziOttenuti"].append(tentDict["ind"])
    dati = {
        "risultato": "hai vinto!",
        "tentativiGioco": dbDict["tentativiGioco"],
        "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"],
        "indizio": tentDict["ind"]
    }
    return json.dumps(dati).encode("utf-8")

def controlla(num, tentativo, risposta):
    tentativo = int(tentativo)
    num = int(num)
    print(tentativo,num, dbDict["tentativiGioco"])
    if tentativo <= int(dbDict["tentativiGioco"]) and tentativo > 0:
        dbDict["tentativiGiocoFatti"] = int(dbDict["tentativiGiocoFatti"]) + 1
        
        dbProva = dbDict["prove"][num-1]
        if risposta.lower() == dbProva["soluz"].lower():
            return getSoluzione(num)
        else:
            dati = {
                "risultato": "f",
                "tentativiGioco": dbDict["tentativiGioco"],
                "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"]
            }
            return json.dumps(dati).encode("utf-8")
    else:
        dbDict["indiziOttenuti"].append("")
        resetGame()
        dati = {
            "risultato": "tentativi esauriti",
            "tentativiGioco": dbDict["tentativiGioco"],
            "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"]
        }
        return json.dumps(dati).encode("utf-8")

def controllaRisposta(tentativo, soluzione):
    tentativo = int(tentativo) 
    if tentativo <= int(dbDict["tentativiIndovina"]) and tentativo > 0:
        dbDict["tentativiIndovinaFatti"] = int(dbDict["tentativiIndovinaFatti"]) + 1
        
        if soluzione.lower() == dbDict["soluzione"].lower():
            dati = {
                "risultato": "corretto",
                "tentativiIndovina": dbDict["tentativiIndovina"],
                "tentativiIndovinaFatti": dbDict["tentativiIndovinaFatti"]
            }
        else:
            dati = {
                "risultato": "sbagliato",
                "tentativiIndovina": dbDict["tentativiIndovina"],
                "tentativiIndovinaFatti": dbDict["tentativiIndovinaFatti"]
            }
        return json.dumps(dati).encode("utf-8")
    else:
        dati = {
            "risultato": "tentativi esauriti"
        }
        return json.dumps(dati).encode("utf-8")
    
def resetGame():
    dbDict["tentativiGioco"] = "5"
    dbDict["tentativiGiocoFatti"] = "0"

def resetMissione():
    global dbDict
    dbDict = json.loads(DB)
    return json.dumps({"risultato": "Missione resettata con successo"}).encode("utf-8")

def getTentativo():
    temp = int(dbDict["tentativiIndovina"]) - len(dbDict["indiziOttenuti"])
    dati = {
        "tentativo": temp
    }
    return json.dumps(dati).encode("utf-8")

