import json

from Back_end import queryLib as ql

def check_get(path):
    if path.endswith("index.html"): # Invio di file al client
        f = open("./Missioni/mariuzzo/index.html")
        contenuto = f.read()
        return contenuto.encode("utf-8")
    if path.endswith("script.js"): # Invio di file al client
        f = open("./Missioni/mariuzzo/script.js")
        contenuto = f.read()
        return contenuto.encode("utf-8")
    elif path.endswith("classi"):
        ql.connetti()
        # Lista che poi verrà convertita in json
        classi = []
        # Effettuo una query al database
        classiDB = ql.execute("SELECT * FROM classi")
        print(classiDB)
        # Inserisco nella lista solo il nome della classe
        for classe in classiDB:
            classeObj = {
                "nome": classe[0],
                "vigore": classe[1],
                "forza": classe[2]
            }
            classi.append(classeObj)
        ql.disconnetti()
        # Invio al client una stringa json contenente un attributo classi con l'array dei nomi delle classi
        return json.dumps({"classi": classi}).encode("utf-8")

def check_post(path, client_choice):
    if path.endswith("post"):
        print("post generica")
        return "ciao post"