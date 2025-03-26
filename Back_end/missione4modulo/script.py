import json #simulo il db

#qualche json per simulare il db
a = '{ "obiettivo": "scopri chi ha rapito Aldo Moro", "ricompensa": "titolo di Kung Fury", "tentativi": 5, "soluzione": "" }'

def check_get(path):
    if path.endswith("dettagli"):
        return getDettagli()

def check_post(path, client_choice):
    if path.endswith("post_generica"):
        return funz222(client_choice)

def getDettagli():
    


def funz222(client_choice):
    nome = client_choice.get("nome", "")
    cognome = client_choice.get("cognome", "")

    print("ciao" + ' ' + nome + cognome)