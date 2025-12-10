from moduli import queryLib

queryLib.connetti()

def check_get(path):
    pass

def check_post(path, clientchoice):
    pass

if __name__ == "__main__":
    risultato = queryLib.execute("SELECT * FROM classi")
    for tupla in risultato:
        print(tupla)
    queryLib.disconnetti()