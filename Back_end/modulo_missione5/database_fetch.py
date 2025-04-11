import psycopg2

user = "[USERNAME]"
port = 6543
dbname = "personaggi"
host = ""

try: 
    connection = psycopg2.connect (
        user=user,
        host=host,
        port=port,
        dbname=dbname
    )
    print("Connection successful")
    cursor:psycopg2.extensions.cursor = connection.cursor()
except Exception as e:
    raise ConnectionError(f"Connessione Fallita: {e}")

cursor.execute('SELECT "id", "Nome", "Livello", "Vigore", "Vigore", "Forza", "Destrezza", "Intelligenza", "Fede", "id_classe", FROM personaggi;')
result = cursor.fetchall()
print(result)

cursor.close()
connection.close()
print("Connection closed")
