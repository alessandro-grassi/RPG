def check_get(path):
    if path.endswith("get_generica"):
        return 'ciao'.encode("utf-8")
    elif path == "/missione1/index":
        with open("Missioni/Missione1/index.html", "r") as file:  # Leggi il file index.html
            content = file.read()
            file.close()
            return content.encode("utf-8")  # Restituisci il contenuto in formato bytes   
    
        




def check_post(path,client_choice):
    if path.endswit ("post_generica"):
        return f2(client_choice)

def f2(client_choice):
    nome = client_choice.get("nome").encode("utf-8")
    return nome