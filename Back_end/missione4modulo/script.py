import json #simulo il db

#json per simulare il db
DB = '{ "obiettivo": "scopri chi ha rapito Aldo Moro", ' \
'       "ricompensa": "titolo di Kung Fury", ' \
'       "tentativiIndovina": 3, ' \
'       "tentativiGioco": 5, ' \
'       "soluzione": "gabibbo",' \
'       "maxIndizi": 2,' \
'       "prove":' \
'       [' \
'           { "num": 1, "soluz": "nonna" "ind": "è rosso" },' \
'           { "num": 2, "soluz": "porto" "ind": "partecipa al programma televisivo Striscia la Notizia" },' \
'           { "num": 3, "soluz": "trave" "ind": "usa spesso il termine BELANDI" },' \
'       ] }'

dbDict = json.loads(DB)


#gestione get e post
def check_get(path):
    if path.endswith("dettagli"):
        return getDettagli()

def check_post(path, tentativo, risposta=''):
    if path.endswith("indovina"):
        return indovina(tentativo, risposta)
    elif path.endswith("prove"):
        return getProve(tentativo)



#funzioni
def getDettagli():
    return dbDict["obiettivo"],dbDict["ricompensa"],dbDict["tentativi"]

def getProve(tentativo):
    tentDict = dbDict["prove"][tentativo]
    return tentDict["soluz"], tentDict["ind"]


def indovina(tentativo, risposta):
    if tentativo <= dbDict["tentativi"]:
        if risposta == dbDict["soluzione"]:
            print("complimenti! hai indovinato")
        else:
            print("mi dispiace ma non è la risposta corretta")
    else:
        print("tentativi esauriti")