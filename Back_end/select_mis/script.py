import json

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
        return json.dumps({"missioni" : test_obj}).encode("utf-8")
    if path.endswith("style"):
        return get_style()
    if path.endswith("script"):
        return get_script()
    

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