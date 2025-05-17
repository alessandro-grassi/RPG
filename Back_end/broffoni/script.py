import json
import Back_end.queryLib as ql

def check_post(path, cc):
    if path.endswith("sm_abilita"):
        return get_abilita()
    return "Non trovato :_-{".encode("utf-8")
    
def check_get(path):
    if path.endswith("broffoni/index.html"):
        with open("Missioni/broffoni/index.html", "rb") as f:
            return f.read()
    elif path.endswith("broffoni/script.js"):
        with open("Missioni/broffoni/script.js", "rb") as f:
            return f.read()
    elif path.endswith("sm_abilita"):
        return get_abilita()
    return "Non trovato :_-{".encode("utf-8")

def get_abilita():
    ql.connetti()
    dati = ql.execute("SELECT * FROM abilita")
    ql.disconnetti()


    lista = []
    for row in dati:
        abilita = {
            "id": row[0],
            "Forza": row[1],
            "Destrezza": row[2],
            "Intelligente": row[3]
        }
        lista.append(abilita)

    return json.dumps({"abilita": lista}).encode("utf-8")
