from Back_end import queryLib as ql
import json

def check_post(path, cc):
    if path.endswith("complete"):
        return complete(cc)
    
def complete(cc):
    ql.connetti()
    msg = {}
    uid = cc.get("uid","")
    mid = cc.get("mid","")

    query = f"""
            UPDATE progressi
            SET 
                p_comp = 100
            WHERE
                progressi.id_missione = {mid} AND
                progressi.id_personaggio = {uid};
            """
    try:
        ql.execute(query)
        msg["success"] = "Salvataggio avvenuto correttamente"
    except ValueError as e:
        msg["error"] = "Errore nel salvataggio dei dati"
    
    ql.disconnetti()
    return json.dumps(msg).encode("utf-8")
    