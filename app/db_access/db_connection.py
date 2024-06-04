#importando bibliotecas
import psycopg2 as psy
import os
from urllib.parse import urlparse


def connection_postgres():
    try:
        database_url = os.getenv('DATABASE_URL')
        result = urlparse(database_url)

        connection = psy.connect(
                        host ='localhost',
                        port = 5432,
                        user = 'postgres',
                        password='123456' 
                        )
        print("Conexão com PostGreSQL estabelecida com sucesso! \n")
    except psy.Error as e:
        print(f"Falha ao conectar a PostGres: {e}")

    transition_postGres = connection.cursor()
    connection.autocommit = True

    transition_postGres.execute('DROP DATABASE if exists dbclientes;')
    transition_postGres.execute('CREATE DATABASE dbclientes;')
    return connection
    

def transition(server):
    #Realizando conexão com o banco de dados
    try:
        connection_base = psy.connect(
                            database = 'db_clientes',
                            user = 'postgres',
                            password='123456',
                            host ='localhost',
                            port = 5432
                            )
        connection_base.autocommit = True 
        
        transition = (server == 'pandas' and connection_base or connection_base.cursor())

        print("Conexão com o Banco clientes estabelecida com sucesso! \n")
    except psy.Error as e:
        print(f"Falha ao conectar ao banco de dados: {e}")
    return transition
    #finalizando
    ##transition_postGres.close()