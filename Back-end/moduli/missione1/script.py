def check_get(path):
    if path.endswith("get_generica"):
        return funz()
        

def funz():
    return "ciao"


def check_post(path,client_choice):
    if path.endswith("post_generica"):
        return f2(client_choice)

def f2(client_choice):
    nome = client_choice.get("nome")
    return nome