from moduli import queryLib
queryLib.connetti()


def check_get(path):
    pass
def check_post(path,clientchoice):
    pass


def funz():
    #header = queryLib.getHeaders("classi")
    #print(header)
    risultato = queryLib.execute('SELECT * FROM classi')
    for tupla in risultato:
        print(tupla[0])
    queryLib.disconnetti()