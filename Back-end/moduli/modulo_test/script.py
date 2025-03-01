from moduli import queryLib

queryLib.connetti()

def check_get(path):
    if path.endswith("get_generica"):
        return funz()

def check_post(path, client_choice):
    if path.endswith("post_generica"):
        return funz2(client_choice)
    
def funz():
    print("ciao")

def funz2(client_choice):
    nome = client_choice.get("nome", "")
    cognome = client_choice.get("cognome", "")
    print("ciao " + nome)


    #
    # risultato = queryLib.execute('SELECT "id", "Vigore" FROM classi')
    # for tupla in risultato:
    #    print(tupla)
    #
    # header = queryLib.getHeaders("classi")
    # print(header)
    
print(queryLib.execute("SELECT * FROM classi"))
queryLib.disconnetti()