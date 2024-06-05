#importando as bibliotecas
from db_access import db_connection


#função responsavel por atualizar os dados.  
def executasql(conexao):
  #fazendo a leitura do arquivo SQL.
  with open('.sql/limpezadados.sql') as arqsql:
    comandos = arqsql.read()
    
  #declarando lista vazia.  
  registrosinseridos = []
  conexao = db_connection.consultar()
  with conexao.cursor() as cursor:
   for comandos in comandos.split(';'):
       comandos = comandos.strip()
       if comandos:
          #concatenando os camandos do update com returning
          envioupdate = comandos +" RETURNING *"

          #metodo responsavel por alterar os dados.
          cursor.execute(envioupdate)

          #salvando commit referente as alterações.
          conexao.commit()
        
          #verificando quantos registros foram alterados.      
          registrosinseridos.append((cursor.fetchall()))
       return len(registrosinseridos)
   