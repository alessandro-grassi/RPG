from Back_end import queryLib
import os

#queryLib.connetti()

def check_get(path):
    if path == "/m5/styletest": # stest get fogli stile
        with open("Missioni/Missione5/missione.css", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") # per tutti i file html css e javascript si deve aggiungere .encode("utf-8")
        
    elif path == "/m5/mission-start": # get pagina di start missione
        with open("Missioni/Missione5/missione.html", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == "/m5/mission-start":
        with open("Missioni/Missione5/assets/font.css", "r") as f: # usare r per richieste sui file
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == "/m5/script":
        with open("Missioni/Missione5/missione.js") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == "/m5/castle-front":
        with open("Missioni/Missione5/assets/castle-front.jpg", "rb") as f: # utilizzare rb(read byte) per richieste sulle immagini
            r = f.read()
            f.close()
            return r
        
    elif path == "/m5/get-dialogue":
        with open("Missioni/Missione5/assets/dialogs.json", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") # encode per restituire i contenuti del file json come stringa da convertire in json dopo
            
    elif path == "/m5/dialog-index":
        with open("Missioni/Missione5/assets/progress.json") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
            
def check_post(path,clientchoice):
    pass

if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()