#importando a bibliotecas para os testes.
import unittest
import pandas as pd
from db_access import insertTable, db_connection

#Testando a inserção de dados na tabela.
#primeiro, criamos a tabela se caso não existir.
#segundo, inserimos dados.
#terceiro, verificamos se nosso valor de retorno é o esperado.
class test_insertTable(unittest.TestCase):
    def setUp(self):
        self.conexao = db_connection.consultar()
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS clientes_temp(
                                id integer NOT NULL,
                                cpf character varying(18),
                                private integer,
                                incompleto integer,
                                data_da_ultima_compra date,
                                ticket_medio character varying(18),
                                ticket_da_ultima_compra character varying(18),
                                loja_mais_frequente character varying(18),
                                loja_da_ultima_compra character varying(18)
                            );
                            """)
        self.conexao.commit()
        #dados = #['12345678909',1,0,'2020-01-01',100.00,200.00,'12345678000195','98765432000196']
        dados = {
            'id': [1],
            'cpf': ['12345678909'],
            'private' : ['1'],
            'incompleto' : ['0'],
            'data_da_ultima_compra': ['2020-01-01'],
            'ticket_medio character' : ['10000'],
            'ticket_da_ultima_compra' : ['20000'],
            'loja_mais_frequente' : ['12345678000195'],
            'loja_da_ultima_compra': ['98765432000196']
        }

        self.dados = pd.DataFrame(dados)        
    def tearDown(self):
       # self.cursor.execute("DROP TABLE IF EXISTS clientes_temp;")
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def test_insertTable(self):
        dados = self.dados
        ##contagem = insertTable.insert_Table(dados)
        ##self.assertEqual(contagem,1)

if __name__ == '__main__':
    unittest.main()