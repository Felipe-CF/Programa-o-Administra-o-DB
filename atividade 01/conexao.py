import psycopg2

def conexao():
    try:
        conn = psycopg2.connect(
            dbname="contato",
            user="felipe",
            password="fcf230800",
            host="localhost",
            port="5432"
        )

        return conn
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def criar_contato(conn, id):

    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM pedidos WHERE cliente_id = {id}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                
    except Exception as e:
        print(f"Erro ao ler dados: {e}")

def ver_contato(conn, id):

    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM pedidos WHERE cliente_id = {id}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                
    except Exception as e:
        print(f"Erro ao ler dados: {e}")


def atualizar_contato(conn, id):

    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM pedidos WHERE cliente_id = {id}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                
    except Exception as e:
        print(f"Erro ao ler dados: {e}")


def deletar_contato(conn, id):

    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM pedidos WHERE cliente_id = {id}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                
    except Exception as e:
        print(f"Erro ao ler dados: {e}")