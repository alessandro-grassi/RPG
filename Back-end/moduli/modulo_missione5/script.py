from moduli import queryLib

queryLib.connetti()

def check_get(path):
    pass

def check_post(path,clientchoice):
    pass

if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()