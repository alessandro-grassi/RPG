# import moduli.queryLib as queryLib
#queryLib.connetti()
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
    if path.endswith("get_text_file"): # Invio di file al client
        file_path = path.split("%")[1].split("-")[0]
        return read_text_file("./Missioni/Missione3" + file_path)
    elif path.endswith("get_binary_file"): # Invio di file al client
        file_path = path.split("%")[1].split("-")[0]
        return read_binary_file("./Missioni/Missione3" + file_path)

def check_post(path, client_choice):
    if path.endswith("post"):
        print("post generica")
        return "ciao post"