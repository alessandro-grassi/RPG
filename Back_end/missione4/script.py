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
    '''
    #apre il backend
    elif path.endswith("backend"):
        f = open(sys.path[0] +"/Back_end/Missione4/backend.py", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
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
    return '"Path not found"'.encode("utf-8")