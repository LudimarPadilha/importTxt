#importando funções
from src.db_access import db_connection
#from src.data_processing import data_processor


def creat_Table():
  transition = db_connection.transition('postGre')

  ##dropando a tabela clientes_temp
  transition.execute("DROP TABLE IF EXISTS clientes_temp")

  #criando a tabela clientes_temp
  try:
      sql = """
         CREATE TABLE clientes_temp (
                  id INTEGER GENERATED ALWAYS AS IDENTITY,
                  CPF VARCHAR(18),
                  PRIVATE INTEGER,
                  INCOMPLETO INTEGER,
                  DATA_DA_ULTIMA_COMPRA DATE NULL,
                  TICKET_MEDIO VARCHAR(18) NULL,
                  TICKET_DA_ULTIMA_COMPRA VARCHAR(18) NULL,
                  LOJA_MAIS_FREQUENTE VARCHAR(18),
                  LOJA_DA_ULTIMA_COMPRA VARCHAR(18)
               );         
               """
      #sql = data_processor.leituraDados('cabecalho')

      transition.execute(sql)      
      print("Tabela clientes_temp criada com Sucesso!! \n")
  except:  
      print("Não foi possivel criar a tabela clientes_temp! \n")
      #finalizando a transação
      #transition.close()