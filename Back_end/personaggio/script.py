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
    if classe["class"]=="default":return json.dumps([]).encode("utf-8")
    #confrontare le stats della classe scelta dall'utente con le sigole stats delle abilita. Se minori della soglia richiesta dalle abilità non mostrare l'abilità in lista
    queryLib.connetti()
    statsClasse = queryLib.execute(f''' SELECT classi."Forza", classi."Destrezza", classi."Intelligenza", classi."Fede" FROM "classi" WHERE classi.id ='{classe["class"]}' ''')[0]
    listaAbilita = queryLib.execute(f''' SELECT abilita.id, abilita."Forza", abilita."Destrezza", abilita."Intelligenza", abilita."Fede" FROM "abilita" ''')
    queryLib.disconnetti()
    array=[]
    for ab in listaAbilita:
        if statsClasse[0]>=ab[1] and statsClasse[1]>=ab[2] and statsClasse[2]>=ab[3] and statsClasse[3]>=ab[4]:
            array.append(ab[0])
    return json.dumps(array).encode("utf-8")

def aggiungi_personaggio(nome, classe, ab1, ab2, ab3, username):
    queryLib.connetti()
    statsClasse = queryLib.execute(f''' SELECT classi."Vigore", classi."Forza", classi."Destrezza", classi."Intelligenza", classi."Fede" FROM "classi" WHERE classi.id ='{classe}' ''')[0]
    nuovo_personaggio = queryLib.execute(f''' INSERT INTO "personaggi" ("Nome", "Livello", "Vigore", "Forza", "Destrezza", "Intelligenza", "Fede", "id_classe", "creatore") VALUES ('{nome}', 0, '{statsClasse[0]}', '{statsClasse[1]}', '{statsClasse[2]}', '{statsClasse[3]}', '{statsClasse[4]}', '{classe}', '{username}')''')
    id_personaggio = queryLib.execute(f'''SELECT personaggi.id FROM "personaggi" WHERE personaggi."Nome"= '{nome}' ORDER BY personaggi."Created_at" DESC ''')[0][0]
    nuovo_personaggio_abilita = queryLib.execute(f''' INSERT INTO "relazione_abilità" (personaggio, ab1, ab2, ab3) VALUES ({id_personaggio},'{ab1}','{ab2}','{ab3}')''')
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
    
def personaggiUtente(utente):
    queryLib.connetti()
    listone = queryLib.execute(f'''SELECT personaggi.id, personaggi."Nome" FROM "personaggi" WHERE personaggi.creatore='{utente}' ''')
    queryLib.disconnetti()
    return json.dumps(listone).encode("utf-8");
    pass

def check_post(path, client_choice):

    if path.endswith("listaAbilita"):
        #chris da qui per inviarti le cose. Ricordati di sistemare il json
        f = ottieni_abilita(client_choice)
        return f

    elif path.endswith("crea_personaggio"):
        try:
            username = client_choice["username"]
            nome = client_choice["name"]
            classe = client_choice["class"]
            ab1 = client_choice["ability1"]
            ab2 = client_choice["ability2"]
            ab3 = client_choice["ability3"]
            aggiungi_personaggio(nome, classe, ab1, ab2, ab3, username)
            return '"Registrazione personaggio effettuata con successo!"'.encode("utf-8")
        except KeyError as errore:
            return '"errore"'.encode("utf-8")
    elif  path.endswith("listaPersonaggi"):
        return personaggiUtente(client_choice)

    else: return '"errore"'.encode("utf-8")
