from Back_end import queryLib as ql
import json

def check_get(path):
    if path.endswith("index"):
        return get_index()
    if path.endswith("script"):
        return get_script()
    if path.endswith("getData"):
        return get_data()

def check_post(path):
    print()

def get_index():
    with open("./demo_db/index.html", "rb") as f:
        msg = f.read()
    return msg

def get_script():
    with open("./demo_db/script.js", "rb") as f:
        msg = f.read()
    return msg

def get_data():
    ql.connetti()
    print(ql.getHeaders("classi"))
    data = ql.execute('''SELECT classi.id, classi."Vigore", classi."Forza", classi."Destrezza", classi."Intelligenza", classi."Fede" FROM classi''')
    ql.disconnetti()
    return json.dumps({"dati": data}).encode("utf-8")