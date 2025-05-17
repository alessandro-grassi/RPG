import json
import Back_end.queryLib as ql

def check_get(path):
    if path == "/abilita":
        try:
            ql.connetti()
            ql.cursor.execute("SELECT id FROM abilita")
            righe = ql.cursor.fetchall()
            headers = [desc[0] for desc in ql.cursor.description]
            dati = [dict(zip(headers, riga)) for riga in righe]
            return json.dumps(dati).encode("utf-8")
        except Exception as e:
            return json.dumps({"errore": str(e)}).encode("utf-8")
    return b"Percorso non valido"
