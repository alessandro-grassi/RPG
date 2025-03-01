import moduli.queryLib as queryLib
queryLib.connetti()
def check_get(path):
    if path.endswith("get"):
        print("get generica")

def check_post(path, client_choice):
    if path.endswith("post"):
        print("post generica")