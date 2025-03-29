import sys
from Back_end import queryLib

def aggiungi_personaggio(nome, classe, abilita):
    queryLib.connetti()
    b=a
    a= queryLib.execute(f'''INSERT INTO "personaggi" (Nome, id_classe) VALUES ('{nome}','{classe}')''')
    queryLib.disconnetti()



def check_get(path):
    


def check_post(path, client_choice):