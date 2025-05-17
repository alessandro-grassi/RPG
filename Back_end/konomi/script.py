import json
from urllib.parse import urlparse
from Back_end import queryLib

def check_get(path):
    path = urlparse(path).path
    
    if path == "/konomi/api/js":
        queryLib.connetti()

        tupla = queryLib.execute("SELECT * FROM abilita")

        queryLib.disconnetti()
        
        return json.dumps({
            "tuplarisultato": tupla
        }).encode("utf-8")
    
    else:
        file_path = None

        if path == "/konomi/js":    #apre il file js
            file_path = "Missioni/Konomi/script.js"
        elif path == "/konomi":
            file_path = "Missioni/Konomi/pagina.html"

        if file_path and file_path.exists():
            with open(file_path, 'rb') as file:
                content = file.read()
            return content
        
        return f"File non trovato: {path}".encode("utf-8")