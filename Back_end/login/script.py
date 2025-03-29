import sys
from Back_end import queryLib

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
    if path == "/login":  # per aprire la pagina di login principale
        f = open(sys.path[0]+"/Autenticazione/Login/login.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
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