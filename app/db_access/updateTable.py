#importando as bibliotecas
import glob
from pathlib import Path
from db_access import db_connection

#função responsavel por atualizar os dados.  
def executasql():
  conexao = db_connection.consultar()
  #fazendo a leitura do arquivo SQL. 
  registrosinseridos = [] 
  arquivo = "./sql"
  sql_arquivos = glob.glob(f"{arquivo}/*.sql")
  for file_path in sql_arquivos:
      with open(file_path, "r") as sql_arquivos:
          commands = sql_arquivos.read()
          cur = conexao.cursor()
          cur.execute(commands)
          conexao.commit()
          registrosinseridos.append((cur.fetchall()))
      return len(registrosinseridos)