import sys
from http.server import BaseHTTPRequestHandler
from Back_end import queryLib
import json
def check_post(path,cc):
    return b""
def check_get(path):
    if path == "/missione6":  # per aprire la prima missione 
        f = open("Missioni/Missione6/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/stile":
        f = open("Missioni/Missione6/styles.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path == "/missione6/backend":
        f = open("Missioni/Missione6/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/image":
        f = open("Missioni/Missione6/cielo.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/quiz2":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione6/parte grafica.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/stile_quiz2":
        f = open("Missioni/Missione6/style.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path == "/missione6/backend_quiz2":
        f = open("Missioni/Missione6/javascript.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/image_quiz2":
        f = open("Missioni/Missione6/cielo.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/memory":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione6/Missione2/memory/index.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/stile_memory":
        f = open("Missioni/Missione6/Missione2/memory/stili.css", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    
    elif path == "/missione6/backend_memory":
        f = open("Missioni/Missione6/Missione2/memory/script.js", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == ("/missione6/drago1"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago1.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago2"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago2.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago3"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago3.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago4"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago4.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago5"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago5.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago6"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago6.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago7"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago7.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == ("/missione6/drago8"):
        f = open("Missioni/Missione6/Missione2/memory/img/drago8.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/pagina_sconfitta":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione6/Missione_Finale/pagina_boss_finale/sconfitta.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/casa":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/casa.png", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/reload":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/reload.png", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/sconfitta":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/sconfitta.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/favicon.ico":
        try:
            with open(sys.path[0] + "/Missioni/Missione6/favicon.ico", "rb") as f:
                return f.read()
        except FileNotFoundError:
            return b''  # ritorna una risposta vuota se il file non c'è
    elif path == "/missione6/pagina_boss_finale":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione6/Missione_Finale/pagina_boss_finale/prog.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/drago":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/drago.gif", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/inferno":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/inferno.jpg", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/sfera":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/sfera.png", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/vittoria":  # per aprire la prima missione 
        f = open(sys.path[0]+"/Missioni/Missione6/Missione_Finale/pagina_boss_finale/vittoria.html", "r")
        stringa = f.read()
        f.close()
        return stringa.encode("utf-8")  # Assicurati di restituire bytes
    elif path == "/missione6/vit":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/vit.gif", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    elif path == "/missione6/vittoria_gif":
        f = open("Missioni/Missione6/Missione_Finale/pagina_boss_finale/vittoria.gif", "rb")  # 'rb' per leggere in binario
        image_data = f.read()
        f.close()
        return image_data  # Restituisci direttamente i dati binari
    return '"Path not found"'.encode("utf-8")


