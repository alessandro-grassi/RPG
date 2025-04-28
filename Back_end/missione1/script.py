import json

def check_get(path):
    if path.endswith("get_generica"):
        return 'ciao'.encode("utf-8")
    elif path.endswith("/index"):
        try:
            with open("./Missioni/Missione1/index.html", "r") as file:
                content = file.read()
            return content.encode("utf-8")
        except FileNotFoundError:
            return "File non trovato".encode("utf-8")
    elif path.endswith("/script.js"):
        try:
            with open("./Missioni/Missione1/script.js", "r") as file:
                content = file.read()
            return content.encode("utf-8")
        except FileNotFoundError:
            return "File non trovato".encode("utf-8")
    elif path.endswith("grass.png"):
        f= open("Missioni/Missione1/grass.png","rb")
        r= f.read()
        f.close()
        return r
    elif path.endswith("grassRed.png"):
        f= open("Missioni/Missione1/grassRed.png","rb")
        r= f.read()
        f.close()
        return r




def check_post(path, client_choice):
    if path.endswith("post_generica"):
        return process_mission(client_choice)
    else:
        return "Percorso non valido".encode("utf-8")





