import json
import Back_end.queryLib as ql
""""
test_obj = [
    {
        "nome" : "miss1",
        "descrizione" : "desc1",
        "url" : ".",
        "completata" : True
    },
    {
        "nome" : "miss2",
        "descrizione" : "desc2",
        "url" : ".",
        "completata" : False
    },
    {
        "nome" : "miss3",
        "descrizione" : "desc3",
        "url" : ".",
        "completata" : False
    },
    {
        "nome" : "miss4",
        "descrizione" : "desc4",
        "url" : ".",
        "completata" : True
    },
    {
        "nome" : "miss5",
        "descrizione" : "desc5",
        "url" : ".",
        "completata" : False
    }
]
"""

def check_get(path):
    if path.endswith("missioni"):
        return get_missioni()
    if path.endswith("style"):
        return get_style()
    if path.endswith("script"):
        return get_script()
    if path.endswith("home"):
        return get_home()
    
def check_post(path,cc):
    return 0

def get_style():
    with open("./SceltaMissione/style.css", "rb") as f:
        msg = f.read()
    return msg

def get_script():
    with open("./SceltaMissione/script.js", "rb") as f:
        msg = f.read()
    return msg

def get_home():
    with open("./SceltaMissione/index.html", "rb") as f:
        msg = f.read()
    return msg

def get_missioni():
    obj = []
    ql.connetti()

    create_tables()
    # data = retrieve()
    # obj = parse(data)

    ql.disconnetti
    return json.dumps({"missioni" : obj}).encode("utf-8")

def create_tables():
    ql.execute('''CREATE TABLE IF NOT EXISTS missioni(
               ID_missione BIGSERIAL,
               nome VARCHAR(50) NOT NULL,
               descrizione VARCHAR(200) NOT NULL,
               url VARCHAR(50) NOT NULL,
               img BYTEA,
               PRIMARY KEY(ID_missione));''')
    ql.execute('''CREATE TABLE IF NOT EXISTS progressi(
               ID_progresso BIGSERIAL,
               id_personaggio INTEGER NOT NULL,
               id_missione INTEGER NOT NULL,
               p_comp INT DEFAULT 0,
               PRIMARY KEY(ID_progresspo),
               FOREIGN KEY(id_personaggio) REFERENCES "personaggi".id,
               FOREIGN KEY(id_missione) REFERNCES "missioni".ID_missione);''')

def retrieve():
    return 0

def parse(data):
    return 0