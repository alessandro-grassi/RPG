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

def check_get(path):
    if path.endswith("missioni"):
        return {"missioni" : test_obj}

def check_post(path,cc):
    return 0