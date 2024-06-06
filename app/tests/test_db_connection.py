#importando a bibliotecas para os testes.
import unittest
from db_access import db_connection

#testando a conexão com banco de dados.
class test_db_connection(unittest.TestCase):
    def test_consultar(self):
        conexao = db_connection.consultar()
        self.assertIsNotNone(conexao)
        conexao.close()

if __name__ == '__main__':
    unittest.main()