import re, json

from Back_end import queryLib as ql

def read_binary_file(path):
    f = open(path, "rb")
    f_content = f.read()
    f.close()
    return f_content
def read_text_file(path):
    f = open(path, "r")
    f_content = f.read()
    f.close()
    return f_content.encode("utf-8")

def check_get(path):
    if path.endswith("get_text"): # Invio di file al client
        char_position = re.search("/", path[1:len(path)]).regs[0][1]
        file_path = path[char_position:len(path)].split("-")[0]
        return read_text_file("./Missioni/Missione3" + file_path)
    elif path.endswith("get_binary"): # Invio di file al client
        char_position = re.search("/", path[1:len(path)]).regs[0][1]
        file_path = path[char_position:len(path)].split("-")[0]
        return read_binary_file("./Missioni/Missione3" + file_path)
    elif path.endswith("db_lib.js"): # Invio di file al client
        return read_text_file("./db_lib.js")
    elif path.endswith("personaggio"): # Invio di file al client
        print(path)
        characterId = path.split("/")[4]
        ql.connetti()
        characterFromDB = ql.execute(f"SELECT * FROM personaggi p WHERE p.id = {characterId}")[0]
        print(characterFromDB)
        character = {
            "name": characterFromDB[1],
        }
        return json.dumps(character).encode("utf-8")

def check_post(path, client_choice):
    if path.endswith("post"):
        print("post generica")
        return "ciao post".encode("utf-8")