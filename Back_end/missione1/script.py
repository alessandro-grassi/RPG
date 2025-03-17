#from moduli import queryLib as q

#q.connetti()
#print(
#    q.execute('SELECT * FROM classi')
#)
#q.disconnetti()

def check_get(path):
    if path.endswith("get_generica"):
    
        dizionario = {'kevin':'1'}
        return dizionario.encode("utf-8")
        

def funz():
    return "ciao".encode("utf-8")


def check_post(path,client_choice):
    if path.endswith("post_generica"):
        return f2(client_choice)

def f2(client_choice):
    nome = client_choice.get("nome").encode("utf-8")
    return nome