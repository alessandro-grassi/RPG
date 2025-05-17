from Back_end import queryLib
import json

def check_get(path):
    if path.endswith("classi"):
        queryLib.connetti()
        r = queryLib.execute(f''' SELECT * FROM "classi" ''')
        queryLib.disconnetti()
        return json.dumps(r).encode("utf-8") 
    if path.endswith("javascript"):
        with open("./Missioni/greco/javascript.js", "rb") as f:
            msg = f.read()
        return msg
    if path.endswith("index"):
        with open("./Missioni/greco/index.html", "rb") as f:
            msg = f.read()
        return msg


def check_post(path, data):
    if path.endswith("esempio"):
        return
    