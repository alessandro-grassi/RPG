from Back_end import queryLib

#la parte post e coneessione al DB la tengo buona ma non so se conviene farla qui o su modulo
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
    
    #elif path.endswith("dettagliGioco"):
    elif path.contains("dettagliGioco/"):
        return getDettagliGioco()
    
    '''
    elif path.endswith("trycookie"):
        f = open(sys.path[0] +"/SceltaPersonaggio/scelta.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")'''
    #se non trova il path
    return '"Path not found"'.encode("utf-8")




def check_post(path, client_choice):
    if path.endswith("indovina"):
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
            return indovina(tentativo, risposta)
        except Exception as errore:
                return '"errore"'.encode("utf-8")
    
    
    
    return '"Path not found"'.encode("utf-8")

    

#PARTE PER SIMULARE DB
import json #simulo il db

#json per simulare il db
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
     ' "prova1",' \
     ' "prova1"' \
     ' ],' \
     ' "prove":' \
     ' [' \
     ' { "num": 3, "soluz": "nonna", "ind": "è rosso" },' \
     ' { "num": 2, "soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia" },' \
     ' { "num": 1, "soluz": "trave", "ind": "usa spesso il termine BELANDI" }' \
     ' ] }'


dbDict = json.loads(DB)

#funzioni per simulare db
def getDettagliGenerali():
    return dbDict["obiettivo"],dbDict["ricompensa"],dbDict["tentativiIndovina"],dbDict["tentativiIndovinaFatti"],dbDict["indiziOttenuti"],dbDict["maxIndizi"]

def getDettagliGioco():
    return dbDict["tentativiGioco"],dbDict["tentativiGiocoFatti"]

def getVincita(num):
    tentDict = dbDict["prove"][num - 1]
    return tentDict["ind"]

def getSoluzione(num):
    tentDict = dbDict["prove"][num - 1]
    return tentDict["soluz"]


def indovina(tentativo, risposta):
    if tentativo <= dbDict["tentativi"]:
        if risposta == dbDict["soluzione"]:
            print("complimenti! hai indovinato")
        else:
            print("mi dispiace ma non è la risposta corretta")
    else:
        print("tentativi esauriti")