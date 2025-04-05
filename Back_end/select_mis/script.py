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
    if path.endswith("style"):
        return get_style()
    if path.endswith("script"):
        return get_script()
    if path.endswith("home"):
        return get_home()
    
def check_post(path,cc):
    uid = cc.uid
    if path.endswith("missioni"):
        return get_missioni(uid)

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

def get_missioni(uid):
    obj = []
    ql.connetti()

    # create_tables()
    data = retrieve(uid)
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
               PRIMARY KEY(ID_progresso),
               FOREIGN KEY(id_personaggio) REFERENCES personaggi(id),
               FOREIGN KEY(id_missione) REFERENCES missioni(ID_missione));''')

def retrieve(uid):
    data = ql.execute(f'''SELECT *
                      FROM
                        missioni,
                        progressi
                      WHERE
                        missioni(ID_missione) = progressi(id_missione) AND
                        progressi(id_personaggio) = {uid};''')

    parsed_data = parse(data)
    return parsed_data

def parse(data):
    parsed_data = []
    for row in data:
        mission = {
            "nome": row["nome"],
            "descrizione": row["descrizione"],
            "url": row["url"],
            "completata": row["p_comp"] == 100  
        }
        parsed_data.append(mission)
    return parsed_data