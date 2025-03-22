from moduli import queryLib
import os
#non funziona
import moduli.modulo_missione5.combactSystem as combactSystem


#queryLib.connetti()

PREFIX = "/m5/" 
PREFIX_API = PREFIX+"api/"

def check_get(path:str):
    if path == PREFIX+"styletest": # stest get fogli stile
        with open("Missioni/Missione5/missione.css", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") # per tutti i file html css e javascript si deve aggiungere .encode("utf-8")
        
    elif path == PREFIX+"mission-start": # get pagina di start missione
        with open("Missioni/Missione5/missione.html", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == PREFIX+"mission-start":
        with open("Missioni/Missione5/assets/font.css", "r") as f: # usare r per richieste sui file
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == PREFIX+"castle-front":
        with open("Missioni/Missione5/assets/castle-front.jpg", "rb") as f: # utilizzare rb(read byte) per richieste sulle immagini
            r = f.read()
            f.close()
            return r
    elif path.startswith( PREFIX_API+"get_life/"):
        name = path.split("/")[4]
        life = str (combactSystem.get_life(name))
        return life.encode("utf-8")
    
            
            
def check_post(path,clientchoice):
    pass

if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()