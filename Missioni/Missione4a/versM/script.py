from Back_end import queryLib
import json

# --- Funzioni database utenti ---

def aggiungi_utente(user, pw, em):
    queryLib.connetti()
    # Da mettere in sicurezza con parametri, qui lasciato come in origine
    a = queryLib.execute(f'''INSERT INTO "utenti" (username, hash, email) VALUES ('{user}','{pw}','{em}')''')
    queryLib.disconnetti()

def utente_registrato(user, pw):
    flag = 0
    queryLib.connetti()
    flag = queryLib.execute(f'''SELECT username, hash FROM "utenti" WHERE username='{user}';''')
    queryLib.disconnetti()
    return len(flag) == 1 and flag[0][1] == pw

# --- Simulazione DB missione ---

DB = """
{
  "obiettivo": "scopri chi ha rapito Aldo Moro risolvendo i wordle!",
  "ricompensa": "titolo di Kung Fury",
  "tentativiIndovina": 3,
  "tentativiIndovinaFatti": 0,
  "tentativiGioco": 5,
  "tentativiGiocoFatti": 0,
  "soluzione": "gabibbo",
  "maxIndizi": 3,
  "indiziOttenuti": [
    "prova1",
    "prova1"
  ],
  "prove": [
    {"soluz": "nonna", "ind": "usa spesso il termine BELANDI"},
    {"soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia"},
    {"soluz": "trave", "ind": "è rosso"}
  ]
}
"""

dbDict = json.loads(DB)

# --- Funzioni per simulare il DB missione ---

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

def getDettagliGioco():
    dati = {
        "tentativiGioco": dbDict["tentativiGioco"],
        "tentativiGiocoFatti": dbDict["tentativiGiocoFatti"]
    }
    return json.dumps(dati).encode("utf-8")

def getVincita(num):
    tentDict = dbDict["prove"][num - 1]
    return tentDict["ind"]

def getSoluzione(num):
    tentDict = dbDict["prove"][num - 1]
    dbDict["indiziOttenuti"].append(tentDict["ind"])
    return "hai vinto!".encode("utf-8")

def indovina(num, tentativo, risposta):
    num = int(num)
    tentativo = int(tentativo)
    if tentitivo <= dbDict["tentativiGioco"]:
        dbProva = dbDict["prove"][num-1]
        dbDict["tentativiGiocoFatti"] = int(dbDict["tentativiGiocoFatti"]) + 1
        if risposta == dbProva["soluz"]:
            return getSoluzione(num)
        else:
            return "".encode("utf-8")
    else:
        return "tentativi esauriti".encode("utf-8")

def resetGame():
    dbDict["tentativiGioco"] = 5
    dbDict["tentativiGiocoFatti"] = 0
    return "Game resettato".encode("utf-8")

# --- Funzioni di routing HTTP ---

def check_get(path):
    if path == "/missione4":
        with open("Missioni/Missione4/primapagina.html", "r") as f:
            return f.read().encode("utf-8")
    elif path.endswith("stile"):
        with open("Missioni/Missione4/stile.css", "r") as f:
            return f.read().encode("utf-8")
    elif path.endswith("indovina"):
        with open("Missioni/Missione4/indovina_soluzione.html", "r") as f:
            return f.read().encode("utf-8")
    elif path.endswith("gioca"):
        with open("Missioni/Missione4/wordle.html", "r") as f:
            return f.read().encode("utf-8")
    elif path.endswith("sm_home"):
        with open("SceltaMissione/index.html", "r") as f:
            return f.read().encode("utf-8")
    elif path.endswith("dettagliGenerali"):
        return getDettagliGenerali()
    elif path.endswith("dettagliGioco"):
        return getDettagliGioco()
    elif path.endswith("resetGame"):
        return resetGame()
    else:
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
            if utente_registrato(username, password):
                return '"Successo"'.encode("utf-8")
            else:
                return '"errore"'.encode("utf-8")
        except Exception as errore:
            return '"errore"'.encode("utf-8")
    elif path.endswith("indovina"):
        try:
            tentativo = client_choice["tentativo"]
            risposta = client_choice["risposta"]
            # Qui manca il parametro num, va gestito in base alla logica della tua app
            return indovina(1, tentativo, risposta)
        except Exception as errore:
            return '"errore"'.encode("utf-8")
    elif "controlla/" in path:
        try:
            num = int(path.rsplit('/', 1)[-1])
            tentativo = client_choice["tentativo"]
            risposta = client_choice["risposta"]
            return indovina(num, tentativo, risposta)
        except Exception as errore:
            return '"errore"'.encode("utf-8")
    return '"Path not found"'.encode("utf-8")
