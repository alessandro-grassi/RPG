import sys
from Back_end import queryLib
import json

def ottieni_classi():
    # Connetti al database
    queryLib.connetti()
    
    # Esegui la query per ottenere tutte le classi con i dati richiesti
    listaClassi = queryLib.execute(f'''
        SELECT classi.id, classi."Vigore", classi."Forza" 
        FROM "classi"
    ''')
    
    # Disconnetti dal database
    queryLib.disconnetti()
    
    # Trasforma i dati in formato JSON
    classi_formattate = []
    for classe in listaClassi:
        classi_formattate.append({
            "ID": classe[0],
            "Vigore": classe[1],
            "Forza": classe[2]
        })
    
    # Ritorna la lista delle classi in formato JSON
    return json.dumps(classi_formattate).encode("utf-8")


def ottieni_abilita(classe):
    if classe["class"] == "default":
        return json.dumps([]).encode("utf-8")

    # Connessione al database
    queryLib.connetti()
    
    # Ottenere le statistiche della classe scelta
    statsClasse = queryLib.execute(f'''
        SELECT classi."Forza", classi."Destrezza", classi."Intelligenza", classi."Fede" 
        FROM "classi" 
        WHERE classi.id ='{classe["class"]}'
    ''')[0]
    
    # Ottenere tutte le abilità
    listaAbilita = queryLib.execute(f'''
        SELECT abilita.id, abilita."Forza", abilita."Destrezza", abilita."Intelligenza", abilita."Fede" 
        FROM "abilita"
    ''')
    
    queryLib.disconnetti()
    
    # Filtra le abilità in base alle statistiche della classe
    abilita_permesse = []
    for ab in listaAbilita:
        if statsClasse[0] >= ab[1] and statsClasse[1] >= ab[2] and statsClasse[2] >= ab[3] and statsClasse[3] >= ab[4]:
            abilita_permesse.append({
                "ID": ab[0],
                "Forza": ab[1],
                "Destrezza": ab[2],
                "Intelligenza": ab[3],
                "Fede": ab[4]
            })
    
    # Restituisce l'elenco delle abilità in formato JSON
    return json.dumps(abilita_permesse).encode("utf-8")


def ottieni_statistiche(client_choice):
    """Restituisce le statistiche della classe selezionata dall'utente."""
    
    if client_choice['classe'] == 'default':
        # Se la classe è "default", restituiamo statistiche di default
        return json.dumps([0, 0, 0, 0, 0]).encode('utf-8')
    
    # Connetti al database
    queryLib.connetti()
    
    # Esegui la query per ottenere le statistiche della classe scelta
    stats = queryLib.execute(f'''
        SELECT classi."Vigore", classi."Forza", classi."Destrezza", classi."Intelligenza", classi."Fede" 
        FROM "classi" 
        WHERE classi.id = '{client_choice['classe']}'
    ''')[0]
    
    # Disconnetti dal database
    queryLib.disconnetti()
    
    # Restituisci le statistiche come JSON
    return json.dumps(stats).encode('utf-8')
