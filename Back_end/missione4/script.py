from Back_end import queryLib

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
    
    #getDetteagliGenerali
    elif path.endswith("dettagliGenerali"):
        return getDettagliGenerali()
    
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
        
    elif path.endswith("indovina"):
        tentativo = client_choice["tentativo"]
        risposta = client_choice["risposta"]
        return indovina(tentativo, risposta)
    
    #elif path.endswith("dettagliGioco"):
    elif path.contains("dettagliGioco/"):
        num = path.rsplit('/', 1)[-1]
        return getDettagliGioco(num)
    
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

'       "maxIndizi": 2,' \
'       "indiziOttenuti":' \
'       [' \
'           "prova1",' \
'           "prova1"' \
'       ]' \

'       "prove":' \
'       [' \
'           { "num": 1, "soluz": "nonna", "ind": "è rosso" },' \
'           { "num": 2, "soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia" },' \
'           { "num": 3, "soluz": "trave", "ind": "usa spesso il termine BELANDI" },' \
'       ] }'

dbDict = json.loads(DB)

#funzioni per simulare db
def getDettagliGenerali():
    return dbDict["obiettivo"],dbDict["ricompensa"],dbDict["tentativiIndovina"],dbDict["tentativiIndovinaFatti"],dbDict["indiziOttenuti"],dbDict["maxIndizi"]

def getDettagliGioco(num):
    tentDict = dbDict["prove"][num - 1]
    return tentDict["ind"]


def indovina(tentativo, risposta):
    if tentativo <= dbDict["tentativi"]:
        if risposta == dbDict["soluzione"]:
            print("complimenti! hai indovinato")
        else:
            print("mi dispiace ma non è la risposta corretta")
    else:
        print("tentativi esauriti")

