#importando a bibliotecas para os testes.
import unittest
import pandas as pd
from data_processing import data_processor

#vamos estar testando a leitura do arquivo e processamento de dados se está correto.
class testdata_processor(unittest.TestCase):
    def setUp(self):
        self.test_arquivo =".Base.txt"
        with open(self.test_arquivo,'w') as f:
            f.write("cpf private incompleto datadaultimacompra ticketmedio ticketdaultimacompra lojamaisfrequente lojadaultimacompra\n")
            f.write("12345678909 1 0 2020-01-01 100.00 200.00 12345678000195 98765432000196\n")

    def tearDown(self):
        import os
        os.remove(self.test_arquivo)

    def test_leituraDados(self):
        dados = data_processor.leituraDados()
        self.assertEqual(len(dados), 49998)

if __name__ == '__main__':
    unittest.main()