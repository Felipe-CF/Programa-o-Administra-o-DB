import psycopg2
from psycopg2 import sql
from conexao import Conexao
from contato import Contato


def criar_contato(conn, contato):

    try:
        with conn.cursor() as cursor:

            cursor.execute(f"INSERT INTO contato(nome, email, endereco, telefone, cep) \
                            VALUES('{contato.nome}', '{contato.email}', '{contato.endereco}', '{contato.telefone}', '{contato.cep}')")
            conn.commit()
                
    except Exception as e:
        print(f"Erro ao ler dados: {e}")

def ver_contato(conn, id):

    try:
        with conn.cursor() as cursor:

            cursor.execute(f"SELECT * FROM contato")

            row = cursor.fetchall()

            row = row[0]

            contato = Contato(row[0], row[1], row[2], row[3], row[4], row[5])
            # for row in rows:
            print(contato)
                
    except Exception as e:
        print(f"Erro ao ler dados: {e}")


# def atualizar_contato(conn, id):

#     try:
#         with conn.cursor() as cursor:
#             cursor.execute(f"SELECT * FROM pedidos WHERE cliente_id = {id}")
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
                
#     except Exception as e:
#         print(f"Erro ao ler dados: {e}")


# def deletar_contato(conn, id):

#     try:
#         with conn.cursor() as cursor:
#             cursor.execute(f"SELECT * FROM pedidos WHERE cliente_id = {id}")
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
                
#     except Exception as e:
#         print(f"Erro ao ler dados: {e}")





if __name__ == '__main__':

    print("TP - Trabalho Prático 2")

    conn = Conexao.conexao()

    while(True):
        print("1 - Criar um novo contato")

        print("2 - Listar contato(s)")

        print("3 - Atualizar um conato")

        print("4 - Deletar um conato")

        print("5 - Sair")
        
        opcao = int(input('Digite a opcao '))

        if opcao == 1:
        

            nome = input("Digite o nome: ")

            cep = input("Digite o CEP: ")

            endereco = input("Digite o endereço: ")

            telefone = input("Digite o telefone: ")

            email  = input("Digite o email: ")

            contato = Contato(None, nome, email, endereco, telefone, cep)

            if conn:
                criar_contato(conn, contato)

                conn.close()

        elif opcao == 2:

            if conn:
                query_opcao = int(input("Digite o id do pedido: "))

                ver_contato(conn, query_opcao)
                
                conn.close()

        # elif opcao == 3:
        #     conn = conexao()
        #     if conn:
        #         init = input("Digite a data de inicio (YYYY-MM-DD): ")
        #         end = input("Digite a data de fim (YYYY-MM-DD): ")
        #         list_client_data(conn, init, end)
        #         conn.close()

        # elif opcao == 4:
        #     conn = conexao()
        #     if conn:
        #         pedidos_clientes_respectivos(conn)
        #         conn.close()

        elif opcao == 5:
            break

        else:
            print("Opção inválida")



