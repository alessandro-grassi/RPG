from moduli import queryLib
import os

#queryLib.connetti()

def check_get(path):
    if path == "/m5/styletest": # stest get fogli stile
        with open("Missioni/Missione5/html_pages/style-template.css", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
        
    elif path == "/m5/mission-start": # get pagina di start missione
        with open("Missioni/Missione5/missione.html", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == "/m5/mission-start":
        with open("Missioni/Missione5/assets/font.css", "r") as f:
            r = f.read()
            f.close()
            return r.encode("utf-8")
    
    elif path == "/m5/castle-front":
        with open("Missioni/Missione5/assets/castle-front.jpg", "rb") as f:
            r = f.read()
            f.close()
            return r
            
            
def check_post(path,clientchoice):
    pass

if __name__ == "__main__":
    print(
        queryLib.execute('SELECT * FROM classi')
    )
    queryLib.disconnetti()