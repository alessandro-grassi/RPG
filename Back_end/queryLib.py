"""
Modulo scritto da Simone De Vito 22/02/25 per la connessione a Supabase.
"""
import psycopg2

def getHeaders(tabella:str)->list[str]:
    """
     ritorna una lista rappresentate i nomi delle colonne di una tabella
    :param tabella: Tabella di cui si vogliono le header
    :return: lista di header
    """
    if cursor==None:
        raise ValueError("il modulo queryLib non è stato inizializzato. chiama queryLib.connetti().")
    try:
        cursor.execute(f'SELECT * FROM {tabella} LIMIT 0')
        descr = [desc[0] for desc in cursor.description]
        return descr
    except Exception as e:
        raise ValueError(f"La Query è fallita. Motivo: \n\t{e}")
def disconnetti()->None:
    """
    Chiusura connesione. (se è già chiusa la funzione non fa niente)
    :return: None
    """
    if connection!= None and cursor!=None:
        print("Chiusura connessione...")
        cursor.close()
        connection.close()
        print("Connection closed.")
def execute(SQL:str)->list[tuple]:
    """
    esegue la stringa SQL richiesta.
    :param SQL: stringa SQL da eseguire
    :return: lista di righe rappresentanti il risultato della query
    """
    if cursor==None:
        raise ValueError("il modulo queryLib non è stato inizializzato. chiama queryLib.connetti().")
    try:
        cursor.execute(SQL)
        return cursor.fetchall()
    except Exception as e:
        raise ValueError(f"La Query è fallita. Motivo: \n\t{e}")
    
def execute_no_return(SQL:str)->None:
    """
    esegue la stringa SQL richiesta.
    :param SQL: stringa SQL da eseguire
    :return: None
    """
    if cursor==None:
        raise ValueError("il modulo queryLib non è stato inizializzato. chiama queryLib.connetti().")
    try:
        cursor.execute(SQL)
        connection.commit()
    except Exception as e:
        raise ValueError(f"La Query è fallita. Motivo: \n\t{e}")    

def connetti()->None:
    """
    Connessione a Supabase. Se la connessione era già stabilita,
    viene chiusa e poi riaperta
    :return: None
    """
    disconnetti()
    global cursor
    global connection
    print("Connessione al DB...")
    try:
        print("Connection successful!")

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

    except Exception as e:
        raise ConnectionError(f"La connessione a Supabase è fallita. Motivo: \n\t{e}")
