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
        classi = []
        classiDB = ql.execute("SELECT * FROM classi")
        for classe in classiDB:
            classi.append(classe[0])
        ql.disconnetti()
        return json.dumps({"classi": classi}).encode("utf-8")

def check_post(path, client_choice):
    if path.endswith("post"):
        print("post generica")
        return "ciao post"