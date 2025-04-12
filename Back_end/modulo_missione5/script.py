from Back_end import queryLib
import os
import json
#non funziona
import Back_end.modulo_missione5.combactSystem as combactSystem

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
        
    elif path == PREFIX+"api-test":
        with open("Missioni/Missione5/api-test.html", "r") as f: # usare r per richieste sui file
            r = f.read()
            f.close()
            return r.encode("utf-8")
        
    elif path.startswith( PREFIX_API+"get-life/"):
        name = path.split("/")[4]
        life = str (combactSystem.get_life(name))
        return ('{"result":"'+life+'"}').encode("utf-8")
    
    elif path.startswith(PREFIX_API+"get-mana/"):
        name = path.split("/")[4]
        mana = str(combactSystem.get_mana(name))
        return ('{"result":"'+mana+'"}').encode("utf-8")
    
    # prende javascript missione
    elif path == PREFIX + "script":
        with open("Missioni/Missione5/missione.js") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    # prende le linee di testo da far scorrere per i dialoghi
    elif path == PREFIX + "get-dialog":
        with open("Missioni/Missione5/assets/dialogs.json", "rb") as f:
            r = f.read()
            f.close()
            return r # encode per restituire i contenuti del file json come stringa da convertire in json dopo
    
    # prende index dialoghi per dialogo corrente
    elif path == PREFIX + "dialog-index":
        with open("Missioni/Missione5/assets/progress.json") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
        
        
    # prende il mapping tra dialoghi e immagini per storyline
    elif path == PREFIX + "get-mapping":
        with open("Missioni/Missione5/assets/dialogs_images.json","r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
     
    #funzione usata per recuperare le immagini in base al nome richiesto
    elif path.startswith(PREFIX+"get-image/"):
        image_name = path.split("/")[3] # fa uno split e prende la 4a cella
        with open("Missioni/Missione5/assets/"+image_name, "rb") as f: # utilizzare rb(read byte) per richieste sulle immagini
            r = f.read()
            f.close()
            return r # restituisce immagine in formato binario
    
    
def check_post(path,clientchoice):
    try:
        if path == PREFIX_API+"set-life":
            name = clientchoice['name']
            value = clientchoice['value']
            combactSystem.set_life(name, int(value))
            return '{"result":"Life set successfully"}'.encode("utf-8")
        
        elif path == PREFIX_API+"set-mana":
            name = clientchoice['name']
            value = clientchoice['value']
            combactSystem.set_mana(name, int(value))
            return '{"result":"Mana set successfully"}'.encode("utf-8")
        
        elif path == PREFIX_API+"do-damage":
            name = clientchoice['name']
            value = clientchoice['value']
            combactSystem.do_damage(name, int(value))
            return '{"result":"Damage done successfully"}'.encode("utf-8")
        
        elif path == PREFIX_API+"use-mana":
            name = clientchoice['name']
            value = clientchoice['value']
            combactSystem.use_mana(name, int(value))
            return '{"result":"Mana used successfully"}'.encode("utf-8")
        
        elif path == PREFIX_API+"attack":
            attacker_name = clientchoice['attacker_name']
            attacked_name = clientchoice['attacked_name']
            attack_name = clientchoice['attack_name']
            combactSystem.attack(attacker_name, attacked_name, attack_name)
            return '{"result":"Attack executed successfully"}'.encode("utf-8")
        
        #aggiorna index dialoghi e immagini lore
        elif path == PREFIX + "update-index":
            print(clientchoice) # print per debug
            update_progress(clientchoice["current_index"],"current_index")
            return json.dumps({"status": "success"}).encode() 
        
        #aggiorna l'ultima immagine vista nel file json
        elif path == PREFIX + "update-last_image":
            update_progress(clientchoice["last_image"],"last_image")
            return json.dumps({"status": "success"}).encode() 
        
        return json.dumps({"status": "error"}).encode()
    
    


        
    except KeyError as e:
        return f'{{"error":"Missing key {str(e)}"}}'.encode("utf-8")
    except ValueError as e:
        return f'{{"error":"Invalid value {str(e)}"}}'.encode("utf-8")
    except Exception as e:
        return f'{{"error":"An error occurred: {str(e)}"}}'.encode("utf-8")
    

# funzione usata per aggiornare l'index del dialogo e ultima immagine a cui si è arrivati nella storia
def update_progress(data,target):
    json_file = open("Missioni/Missione5/assets/progress.json", "r")  # legge il file json
    parsed_data = json.loads(json_file.read()) # fa il parse in formato json della stringa
    json_file.close()
    parsed_data[target] = data # imposta il campo con i dati 
    converted_data = json.dumps(parsed_data, indent=4) # converte i dati in formato json
    json_file = open("Missioni/Missione5/assets/progress.json", "w") # apre il file in lettura
    json_file.write(converted_data) # scrive sul file json i dati
    json_file.close() # chiude il file
    


if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()