import sys
from Back_end import queryLib

def check_get(path):
    if path == "/":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    elif path.endswith("stile"):
        f = open(sys.path[0] +"/Missioni/Missione5/styles.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    
    elif path.endswith("backend"):
        f = open(sys.path[0] +"/Missioni/Missione5/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")
    return '"Path not found"'.encode("utf-8")
