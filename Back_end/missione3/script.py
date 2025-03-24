# import moduli.queryLib as queryLib
#queryLib.connetti()
def read_file(path):
    f = open(path, "rb")
    f_content = f.read()
    f.close()
    return f_content

def check_get(path):
    if path.endswith("get_file"): # Invio di file al client
        file_path = path.split("%")[1].split("-")[0]
        return read_file("./Missioni/Missione3" + file_path)

def check_post(path, client_choice):
    if path.endswith("post"):
        print("post generica")
        return "ciao post"