def check_get(path):
    if path.endswith("cookie.js"):
        f = open("SceltaPersonaggio/cookies.js","r")
        r=f.read()
        f.close()
        return r.encode("utf-8")
    return "".encode("utf-8")
def check_post(a,b):
    return "".encode("utf-8")