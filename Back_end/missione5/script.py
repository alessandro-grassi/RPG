import sys
from http.server import BaseHTTPRequestHandler
from Back_end import queryLib

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
    elif path == "/missione2":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/parte grafica.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/stile_missione2"):
        f = open(sys.path[0] +"/Missioni/Missione5/style.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path.endswith("/backend_missione2"):
        f = open(sys.path[0] +"/Missioni/Missione5/javascript.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/image_missione2"):
        f = open(sys.path[0] +"/Missioni/Missione5/cielo.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione_memory":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/Missione2/memory/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/stile_memory"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/stili.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path.endswith("/backend_memory"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/drago1"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago1.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("/drago2"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago2.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("drago3"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago3.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("drago4"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago4.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("drago5"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago5.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("drago6"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago6.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("drago7"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago7.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("drago8"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione2/memory/img/drago8.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/pagina_sconfitta":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/sconfitta.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/casa"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/casa.png", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("/reload"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/reload.png", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("/sconfitta"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/sconfitta.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/favicon.ico":
        try:
            with open(sys.path[0] + "/Missioni/Missione5/favicon.ico", "rb") as f:
                return f.read()
        except FileNotFoundError:
            return b''  # ritorna una risposta vuota se il file non c'è
    elif path == "/pagina_boss_finale":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/prog.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/drago"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/drago.gif", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("/inferno"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/inferno.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("/sfera"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/sfera.png", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/vittoria":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/vittoria.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path.endswith("/vit"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/vit.gif", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path.endswith("/vittoria_gif"):
        f = open(sys.path[0] +"/Missioni/Missione5/Missione_Finale/pagina_boss_finale/vittoria.gif", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    return '"Path not found"'.encode("utf-8")

def check_post(path, data):
    if path == "/missione6/inviaData":
        try:
            variabile = data
            aggiungiValore(variabile)
            val = 1
            return val.encode("utf-8")
        except Exception:
            val = 0
            return val.encode("utf-8")
        
def aggiungiValore(valore):
    queryLib.connetti()
    a = queryLib.execute(f'''INSERT INTO "utenti"() VALUES ('{valore}')''')
    queryLib.disconnetti()


