import sys
from Back_end import queryLib
import json

def aggiungi_personaggio(nome, classe, abilita):
    queryLib.connetti()
    a = queryLib.execute(f'''INSERT INTO "personaggi" (Nome, id_classe) VALUES ('{nome}','{classe}')''')
    b = queryLib.execute(f'''SELECT personaggi.id FROM "personaggi" WHERE personaggi.Nome ='{nome}' ''')
    c = queryLib.execute(f'''INSERT INTO "relazione_abilita" (personaggio, ab1, ab2, ab3) VALUES ('{b}','{abilita[0]}','{abilita[1]}','{abilita[2]}')''')
    e = queryLib.execute(f'''INSERT INTO "abilita" () ''')
    b = a
    queryLib.disconnetti()

def ottieni_classi():
    queryLib.connetti()
    listaClassi = queryLib.execute(f'''SELECT classi.id FROM "classi" ''')
    queryLib.disconnetti()
    stringa = json.dumps(listaClassi)
    return stringa.encode("utf-8")

def ottieni_abilita(classe):
    #confrontare le stats della classe scelta dall'utente con le sigole stats delle abilita. Se minori della soglia richiesta dalle abilità non mostrare l'abilità in lista
    queryLib.connetti()
    statsClasse = queryLib.execute(f''' SELECT classe.Forza, classe.Destrezza, classe.Intelligenza, classe.Fede FROM "classi" WHERE classe.id ='{classe}' ''')
    listaAbilita = queryLib.execute(f''' SELECT abilita.id, abilita.Forza, abilita.Destrezza, abilita.Intelligenza, abilita.Fede FROM "abilita" ''')
    queryLib.disconnetti()
    return 



def check_get(path):
    if path == "/personaggio":  # per aprire la pagina di login principale
        f = open("Autenticazione/Creazione-personaggio/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    if path.endswith("stile"):
        f = open("Autenticazione/Creazione-personaggio/style.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("backend"):
        f = open("Autenticazione/Creazione-personaggio/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("listaClassi"):
        f = ottieni_classi()
        return f

    elif path.endswith("listaPersonaggi"):
        print()
       
    elif path.endswith("magoblu"):                  
        f = open("Autenticazione/Creazione-personaggio/magoblu.jpg", "rb")
        stringa = f.read()
        f.close()
        return stringa

    elif path.endswith("magorosso"):    
        f = open("Autenticazione/Creazione-personaggio/magorosso.jpg", "rb")
        stringa = f.read()
        f.close()
        return stringa
    


def check_post(path, client_choice):

    if path.endswith("listaAbilita"):
        #chris da qui per inviarti le cose. Ricordati di sistemare il json
        f = ottieni_abilita(client_choice)