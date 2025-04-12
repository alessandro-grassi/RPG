def check_get(path):
    if path.endswith("get_generica"):
        return funz()

def check_post(path, client_choice):
    if path.endswith("post_generica"):
        return funz222(client_choice)

def funz():
    print("ciao")

def funz222(client_choice):
    nome = client_choice.get("nome", "")
    cognome = client_choice.get("cognome", "")

    print("ciao" + ' ' + nome + cognome)