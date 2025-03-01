def check_get(path):
    if path.endswith("get_generica"):
        return funz()

def check_post(path, client_choice):    
    if path.endswith("post_generica"):
        return funz2(client_choice)

def funz():
    print ("Ciao")

def funz2(client_choice):
    nome = client_choice.get("nome","")
    cognome = client_choice.get("cognome","")
    print("Ciao", nome)