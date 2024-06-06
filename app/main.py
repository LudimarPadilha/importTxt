##importando biblioteca e funções
import unittest
import os
from db_access import insertTable, updateTable
from data_processing import data_processor
from warnings import filterwarnings


#Aviso sobre usar a biblioteca SQLAlchemy e não as demais.
filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')

#testes automatizados
def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result.wasSuccessful()

if not run_tests():
    print("Os testes automatizados falharam! Corrija os erros e tente novamente.")
    exit(1)

print("Iniciando o projeto! \n")
print("Iniciando a leitura de dados do arquivo Base.txt!")
leituraBase = data_processor.leituraDados()
print("Foi realizado a leitura de",len(leituraBase),"linhas. \n")

print("Iniciando a inserção de dados na tabela clientes_temp!! \n")
print("Foram inseridos", insertTable.insert_Table(leituraBase),"registros na tabela clientes_temp! \n")

print("Iniciando a higienização de dados na tabela clientes_temp!! \n")
print("Foram alterados", updateTable.executasql(),"registros na tabela clientes_temp! \n")