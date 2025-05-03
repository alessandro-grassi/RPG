import sys
from http.server import BaseHTTPRequestHandler

def check_get(path):
    if path == "/":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("stile"):
        f = open(sys.path[0] +"/Missioni/Missione5/styles.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path.endswith("backend"):
        f = open(sys.path[0] +"/Missioni/Missione5/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("image"):
        f = open(sys.path[0] +"/Missioni/Missione5/cielo.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    if path == "/missione2":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/parte grafica.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("stile"):
        f = open(sys.path[0] +"/Missioni/Missione5/styles.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path.endswith("backend"):
        f = open(sys.path[0] +"/Missioni/Missione5/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    return '"Path not found"'.encode("utf-8")

