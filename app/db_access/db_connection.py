#importando bibliotecas
import psycopg2 as psy

def consultar():
    #Realizando conexão com o banco de dados
    try:
        connection_base = psy.connect(
                            database = 'db_clientes',
                            user = 'postgres',
                            password='postgres',
                            host ='db',
                            port = 5432
                            )
        connection_base.autocommit = True 
        print("Conexão com o Banco clientes estabelecida com sucesso! \n")
    except psy.Error as e:
        print(f"Falha ao conectar ao banco de dados: {e}") 
    return connection_base