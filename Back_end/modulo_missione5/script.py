from Back_end import queryLib
import os
import json
#non funziona
import Back_end.modulo_missione5.combactSystem as combactSystem

#queryLib.connetti()
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
        
    elif path == PREFIX+"enemies-images-path":
        with open("Missioni/Missione5/assets/enemies_images.json", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") # encode 
        
    elif path == PREFIX+"mission-scena-2":
        with open("Missioni/Missione5/html_pages/scena_2.html", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
        
    elif path == PREFIX+"enemies-images-path":
        with open("Missioni/Missione5/assets/enemies_images.json", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") # encode 
    
    elif path == PREFIX+"mission-start":
        with open("Missioni/Missione5/assets/font.css", "r") as f: # usare r per richieste sui file
            r = f.read()
            f.close()
            return r.encode("utf-8")
        
    # getter pagine missioni, da cambiare in una funzione generalizzata
    elif path == PREFIX+"mission-scena-1":
        with open("Missioni/Missione5/html_pages/scena_1.html", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == PREFIX+"mission-scena-3":
        with open("Missioni/Missione5/html_pages/scena_3.html", "r") as f:
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
        combactSystem.enemy_attack('provaM5')
        return ('{"result":"'+'0'+'"}').encode("utf-8")
    
    elif path == PREFIX+"enemies-list":
        with open("Missioni/Missione5/assets/Enemies.json", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") # encode
    elif path == PREFIX+"random-chance":
        rand = combactSystem.rand(1, 100)
        return ('{"result":"'+str(rand)+'"}').encode("utf-8")  
    
    # prende javascript missione
    elif path == PREFIX + "script":
        with open("Missioni/Missione5/missione.js") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
        
    elif path == PREFIX + "script-scena-3":
        with open("Missioni/Missione5/html_pages/scena_3.js") as f:
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
        out = combactSystem.get_dialog_index("provaM5")
        out = json.dumps(out, indent=4) # converte in formato json
        return out.encode("utf-8")
     
    #funzione usata per recuperare le immagini in base al nome richiesto
    elif path.startswith(PREFIX+"get-image/"):
        image_name = path.split("/")[3] # fa uno split e prende la 4a cella
        with open("Missioni/Missione5/assets/"+image_name, "rb") as f: # utilizzare rb(read byte) per richieste sulle immagini
            r = f.read()
            f.close()
            return r # restituisce immagine in formato binario
    elif path=="/m5/script-scena-2":
        f = open("Missioni/Missione5/html_pages/scena_2.js")
        r = f.read()
        f.close()
        return r.encode("utf-8")

    elif path== PREFIX + "script-scena-1":
        f = open("Missioni/Missione5/html_pages/scena_1.js", "rb")
        r = f.read()
        f.close()
        return r
    
    # combactSystem
    elif path.startswith(PREFIX_API + "get-enemy-life/"):
        username = path.split("/")[4]
        life = combactSystem.enemy_get_healt(username)
        return ('{"result":"' + str(life) + '"}').encode("utf-8")
    elif path.startswith(PREFIX_API + "get-player-life/"):
        username = path.split("/")[4]
        life = combactSystem.player_get_healt(username)
        return ('{"result":"' + str(life) + '"}').encode("utf-8")
    elif path.startswith(PREFIX_API + "get-player-max-life/"):
        characterId = path.split("/")[4]
        life = combactSystem.get_max_player_healt(characterId)
        return ('{"result":"' + str(life) + '"}').encode("utf-8")
    elif path.startswith(PREFIX_API + "get-ability-list/"):
        characterId = path.split("/")[4]
        attack_list = combactSystem.get_character_abilities(characterId)
        return json.dumps(attack_list).encode("utf-8")
    elif path.startswith(PREFIX_API + "get-ability-data/"):
        abilityName = path.split("/")[4]
        abilityData = combactSystem.get_ability_data(abilityName)
        return json.dumps(abilityData).encode("utf-8")


    else:
        return "Percorso non valido!".encode("utf-8")
    

        
def check_post(path,clientchoice):
    try:

        # combactSystem
        if path == PREFIX_API + "enemy-attack":
            userName = clientchoice["username"]
            characterId = clientchoice["characterId"]
            combactSystem.enemy_attack(userName, characterId)
            return '{"result":"Attacco eseguito con successo"}'.encode("utf-8")
        
        if path == PREFIX_API + "player-attack":
            # recupera il nome dell'utente dalla richiesta
            userName = clientchoice["username"]
            # recupera il nome dell'attacco dalla richiesta
            attackName = clientchoice["attack_name"]
            combactSystem.player_attack(userName, attackName)
            return '{"result":"Attacco eseguito con successo"}'.encode("utf-8")

        #aggiorna index dialoghi e immagini lore
        elif path == PREFIX + "update-index":
            print(clientchoice) # print per debug
            combactSystem.set_current_index("provaM5", clientchoice["current_index"]) # aggiorna l'index del dialogo
            return json.dumps({"status": "success"}).encode() 
        
        #aggiorna l'ultima immagine vista nel file json
        elif path == PREFIX + "update-last_image":
            combactSystem.set_last_image("provaM5",clientchoice["last_image"]) # aggiorna l'index del dialogo
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