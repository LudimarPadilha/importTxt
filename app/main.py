##importando biblioteca e funções
from db_access import insertTable, updateTable
from data_processing import data_processor
from warnings import filterwarnings


#Aviso sobre usar a biblioteca SQLAlchemy e não as demais.
filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')

print("Iniciando o projeto! \n")
print("Iniciando a leitura de dados do arquivo Base.txt!")
leituraBase = data_processor.leituraDados()
print("Foi realizado a leitura de",len(leituraBase),"linhas. \n")

print("Iniciando a inserção de dados na tabela clientes_temp!! \n")
print("Foram inseridos", insertTable.insert_Table(leituraBase),"registros na tabela clientes_temp! \n")

print("Iniciando a higienização de dados na tabela clientes_temp!! \n")
print("Foram alterados", updateTable.executasql(leituraBase),"registros na tabela clientes_temp! \n")