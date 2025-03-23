from Back_end import queryLib
import os
import json

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
    if path == "update-index":
        

if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()
    

def update_index(index):
    json_file = open("Missioni/Missione%/assets/progress.json", "r")  # legge il file json
    parsed_data = json.loads(json_file.read()) # fa il parse in formato json della stringa
    json_file.close()
    parsed_data["current_index"] = index # imposta il nuovo index
    converted_data = json.dumps(parsed_data, indent=4) # converte i dati in formato json
    json_file = open("Missioni/Missione%/assets/progress.json", "w") # apre il file in lettura
    json_file.write(converted_data) # scrive sul file json i dati
    