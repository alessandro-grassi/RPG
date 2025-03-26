import sys
def check_get(path):
    #if path == "/login":  # per aprire la pagina di login principale
    #    f = open("/Autenticazione/Login/login.html", "r")
    #    stringa = f.read()
    #    f.close()
    #    return stringa.encode("utf-8")
    if path.endswith("stile"):
        f = open(sys.path[0] +"/Autenticazione/Login/login.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("backend"):
        f = open(sys.path[0] +"/Autenticazione/Login/login.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")

def check_post(path):
    if path.endswith("registrazione"):
        parole = "registrazione effettuata"
        return parole.encode("utf-8")
    elif path.endswith("accesso"):
        parole = "accesso effettuata"
        return parole.encode("utf-8")