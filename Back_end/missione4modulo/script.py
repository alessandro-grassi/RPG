#TODO: INTEGRARE QUESTO IN UN SOLO MODULO IN MISSIONE4 (LA COPIA DEL LOGIN)

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
'           { "num": 0, "ind": "è una prova" },' \
'       ] }' \

'       "prove":' \
'       [' \
'           { "num": 1, "soluz": "nonna", "ind": "è rosso" },' \
'           { "num": 2, "soluz": "porto", "ind": "partecipa al programma televisivo Striscia la Notizia" },' \
'           { "num": 3, "soluz": "trave", "ind": "usa spesso il termine BELANDI" },' \
'       ] }'

dbDict = json.loads(DB)


#gestione get e post
def check_get(path):
    if path.endswith("dettagliGenerali"):
        return getDettagliGenerali()

def check_post(path, tentativo, risposta=''):
    if path.endswith("indovina"):
        return indovina(tentativo, risposta)
    #elif path.endswith("dettagliGioco"):
    elif path.contains("dettagliGioco/"):
        num = path.rsplit('/', 1)[-1]
        return getDettagliGioco(num)



#funzioni
def getDettagliGenerali():
    return dbDict["obiettivo"],dbDict["ricompensa"],dbDict["tentativiIndovina"],dbDict["tentativiIndovinaFatti"],dbDict["indiziOttenuti"],dbDict["maxIndizi"]

def getDettagliGioco(num):
    tentDict = dbDict["prove"][num - 1]
    return tentDict["num"], tentDict["ind"]


def indovina(tentativo, risposta):
    if tentativo <= dbDict["tentativi"]:
        if risposta == dbDict["soluzione"]:
            print("complimenti! hai indovinato")
        else:
            print("mi dispiace ma non è la risposta corretta")
    else:
        print("tentativi esauriti")


