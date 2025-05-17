import jason
import sys
from http.server import BaseHTTPRequestHandler
from Back_end import queryLib

def check_get():
    if path == "/classi":
        f=open(sys.path[0]+"/Missioni/Proserpio/classi.html","r")
        stringa=f.read()
        f.close()
        return stringa.encode("utf-8")
    if path=="/classi":
        try:
            elenchi=PrendiDati()
            return elenchi.encode("utf-8")
         except Exception :
            val=0
            return val.encode("utf-8")

def PrendiDati():
    queryLib.connetti()
    risposta=queryLib.execute(f'''SELECT classi.id,classi.vigore, classi.forza FROM classi''')
    queryLib.disconnetti()
    return risposta
