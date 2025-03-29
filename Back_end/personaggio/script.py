import sys
from Back_end import queryLib

def aggiungi_personaggio(nome, classe, abilita):
    queryLib.connetti()
    a = queryLib.execute(f'''INSERT INTO "personaggi" (Nome, id_classe) VALUES ('{nome}','{classe}')''')
    b = queryLib.execute(f'''SELECT personaggi.id FROM "personaggi" WHERE personaggi.Nome ='{nome}' ''')
    c = queryLib.execute(f'''INSERT INTO "relazione_abilita" (personaggio, ab1, ab2) VALUES ('{b}','{abilita[0]}','{abilita[1]}')''')
    e = queryLib.execute(f'''INSERT INTO "abilita" () ''')
    b = a
    queryLib.disconnetti()



def check_get(path):
    if path == "/personaggio":  # per aprire la pagina di login principale
        f = open(sys.path[0]+"/Autenticazione/Creazione-personaggio/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    if path.endswith("stile"):
        f = open(sys.path[0] +"/AutenticazioneCreazione-personaggio/style.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("backend"):
        f = open(sys.path[0] +"/Autenticazione/Creazione-personaggio/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("magoblu"):                  
        f = open(sys.path[0] +"/Autenticazione/Creazione-personaggio/magoblu.jpg", "rb")
        stringa = f.read()
        f.close()
        return stringa

    elif path.endswith("magorosso"):    
        f = open(sys.path[0] +"/Autenticazione/Creazione-personaggio/magorosso.jpg", "rb")
        stringa = f.read()
        f.close()
        return stringa
    


def check_post(path, client_choice):
    ...