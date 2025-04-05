import json
import Back_end.queryLib as ql

def check_get(path):
    if path.endswith("style"):
        return get_style()
    if path.endswith("script"):
        return get_script()

def get_style():
    with open("./././Missioni/Missione1/style.css", "rb") as f:
        msg = f.read()
    return msg

def get_script():
    with open("./././Missioni/Missione1/script.js", "rb") as f:
        msg = f.read()
    return msg