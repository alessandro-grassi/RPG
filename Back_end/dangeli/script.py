import json
from Back_end import queryLib

def ottieni_abilita():
    #confrontare le stats della classe scelta dall'utente con le sigole stats delle abilita. Se minori della soglia richiesta dalle abilità non mostrare l'abilità in lista
    queryLib.connetti()
    listaAbilita = queryLib.execute(f''' SELECT abilita.id, abilita."Forza", abilita."Destrezza", abilita."Intelligenza", abilita."Fede" FROM "abilita" ''')
    queryLib.disconnetti()
    array=[]
    for ab in listaAbilita:
        array.append(ab[0])
    return json.dumps(array).encode("utf-8")


def check_get(path):
    if path == "/dangeli":  # per aprire la pagina 
        f = open("Missioni/dangeli/mostraAbilita.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("backend"):
        f = open("Missioni/dangeli/dangeli.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("listaAbilita"):
        f = ottieni_abilita()
        return f
    
def check_post(path, client_choice):
    return
