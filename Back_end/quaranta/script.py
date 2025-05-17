import sys
import json
from Back_end import queryLib

def check_get(path):
    if path == "/quaranta":
        try:
            with open(sys.path[0] + "/Missioni/quaranta/index.html", "r", encoding="utf-8") as f:
                html = f.read()
            return html.encode("utf-8")
        except FileNotFoundError:
            return json.dumps({"errore": "File index.html non trovato in /Missioni/quaranta"}).encode("utf-8")
    
    elif path == "/quaranta/getData_quaranta": 
        try:
            queryLib.connetti()
            data = queryLib.execute('SELECT id, "Forza", "Destrezza" FROM abilita')
            print("Dati:", data)
            queryLib.disconnetti()
            return json.dumps(data).encode("utf-8")
        except Exception as e:
            print("Errore:", e)
            return json.dumps({"errore": str(e)}).encode("utf-8")
