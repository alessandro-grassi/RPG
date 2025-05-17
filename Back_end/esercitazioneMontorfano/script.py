from Back_end import queryLib

def check_get(path):
    if path == "/eserzitazione-montorfano": 
        f = open("./Missioni/montorfano/monto.html", "rb")
        stringa = f.read()
        f.close()
        return stringa
    elif path.endswith("montoJS"):
        f = open("./Missioni/montorfano/monto.js", "rb")
        stringa = f.read()
        f.close()
        return stringa
    
    #per ottenere dati
    elif path.endswith("getDati"):
        return getDati()
    return '"Path not found"'.encode("utf-8")

def getDati():
    queryLib.connetti()
    datiOttenuti = queryLib.execute('SELECT ID, VIGORE, FORZA FROM classi')
    queryLib.disconnetti()
    return datiOttenuti