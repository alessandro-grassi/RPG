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
    except KeyError as e:
        return f'{{"error":"Missing key {str(e)}"}}'.encode("utf-8")
    except ValueError as e:
        return f'{{"error":"Invalid value {str(e)}"}}'.encode("utf-8")
    except Exception as e:
        return f'{{"error":"An error occurred: {str(e)}"}}'.encode("utf-8")

if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()