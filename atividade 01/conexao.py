import psycopg2
from contato import Contato


class Conexao:
    def conexao():
        try:
            conn = psycopg2.connect(
                dbname="loja_virtual",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )

            return conn
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
    
