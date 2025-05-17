from Back_end import queryLib
import os
import json


PREFIX = "/es/" 
PREFIX_API = PREFIX+"api/"

def check_get(path:str):
    if path == PREFIX+"table-abilita":
        with open("Back_end/esercitazione/page.html", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") 
    elif path == PREFIX+"js-script":
        with open("Back_end/esercitazione/scriptjs.js", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8") 
    elif path == PREFIX_API+"get-abilita":
        results = queryLib.execute("SELECT * FROM abilita")
        return json.dumps()
        