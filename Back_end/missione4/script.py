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
    
    #getDettagliGioco
    elif path.endswith("dettagliGioco"):
    #elif path.contains("dettagliGioco/"):
        return getDettagliGioco()
    
    #reset dati gioco
    elif path.endswith("resetGame"):
    #elif path.contains("dettagliGioco/"):
        return resetGame()
    
    '''
    elif path.endswith("trycookie"):
        f = open(sys.path[0] +"/SceltaPersonaggio/scelta.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")'''
    #se non trova il path
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
            tentativo = client_choice["tentativo"]
            risposta = client_choice["risposta"]
            return indovina(tentativo, risposta)
        except Exception as errore:
                return '"errore"'.encode("utf-8")
    
    elif path.contains("controlla/"):
        try:
            num = path.rsplit('/', 1)[-1]
            tentativo = client_choice["tentativo"]
            risposta = client_choice["risposta"]
            return indovina(num, tentativo, risposta)
        except Exception as errore:
            return json.dumps({"esito": "errore", "messaggio": str(errore)}).encode("utf-8")
    
    return '"Path not found"'.encode("utf-8")

    





#PARTE PER SIMULARE DB
import json #simulo il db

#json per simulare il db
DB = '{ "obiettivo": "scopri chi ha rapito Aldo Moro risolvendo i wordle!", ' \
'       "ricompensa": "titolo di Kung Fury", ' \

'       "tentativiIndovina": 3, ' \
'       "tentativiIndovinaFatti": 0, ' \
'       "tentativiGioco": 5, ' \
'       "tentativiGiocoFatti": 0, ' \

'       "soluzione": "gabibbo",' \

'       "maxIndizi": 3,' \
'       "indiziOttenuti":' \
'       [' \
'           "prova1",' \
'           "prova1"' \
'       ],' \

'       "prove":' \
'       [' \
'           {"soluz": "nonna", "ind": "usa spesso il termine BELANDI" },' \
'           {"soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia" },' \
'           {"soluz": "trave", "ind": "è rosso" }' \
'       ] }'

dbDict = json.loads(DB)

#funzioni per simulare db
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
    return dbDict["tentativiGioco"],dbDict["tentativiGiocoFatti"]

def getVincita(num):
    tentDict = dbDict["prove"][num - 1]
    return tentDict["ind"]

def getSoluzione(num):
    tentDict = dbDict["prove"][num - 1]
    dbDict["indiziOttenuti"] += ", " + tentDict["ind"]
    return "hai vinto!"


def indovina(num, tentativo, risposta):
    if tentativo <= dbDict["tentativiGioco"]:

        #aggiungo tentativo
        dbProva["tentativiGiocoFatti"] = str(int(dbProva["tentativiGiocoFatti"]) + 1)

        dbProva = dbDict["prove"][num-1]
        if risposta == dbProva["soluz"]:
            return getSoluzione(num)
        else:
            return ""
    else:
        return "tentativi esauriti"
    
def resetGame():
    dbDict["tentativiGioco"] = "5"
    dbDict["tentativiGiocoFatti"] = "0"

