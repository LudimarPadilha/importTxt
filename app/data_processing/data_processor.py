#importando bibliotecas
import pandas as pd
import numpy as np
from pycpfcnpj import cpf, cnpj

#função responsavel por fazer a leitura do arquivo Base.txt
"""
def leituraDados():
  with open(r"./Base.txt") as base:
    dadosF = []
    #Estamos pegando sempre a partir da segunda Linha. Já que a primeira é um head.
    for l in (base.readlines()[1::]):        
        dados = tuple(l.split())
        dadosF.append(dados)

  return dadosF
##########################################CODIGO COMENTADO##################################################
"""


##Estrutura de colunas que serão implementadas no cabeçalho do dataFrame.
COLUM  = ['cpf',
         'private',
         'incompleto',
         'datadaultimacompra',
         'ticketmedio',
         'ticketdaultimacompra',
         'lojamaisfrequente',
         'lojadaultimacompra'
        ]

def leituraDados():
   with open(r"./Base.txt") as base:
    # Declarando uma lista vazia.
    dadoslist = []
    # Estamos pegando sempre a partir da segunda linha. Já que a primeira é um cabeçalho.
    for l in base.readlines()[1:]:
      dados = tuple(l.split())
      dadoslist.append(dados)      
      #convertendo uma lista em um DataFrame
      df = pd.DataFrame(dadoslist, columns=COLUM)
    return df
#dadosF = [None if elemento  == 'NULL' else elemento  for elemento  in f]
leituraDados()

Dados = leituraDados()
Dados = Dados.replace('NULL', np.nan, inplace=True);

#declarando variaveis zeradas
cpf1 = 0
cnpj1 = 0
cnpj2 = 0
for posicao, linha in Dados.iterrows():
    #vamos fazer a verificação por coluna
    cpf1 = (cpf.validate(linha['cpf'])  == True and cpf1 + 1 or 0)
    cnpj1 = (cnpj.validate(linha['lojamaisfrequente']) == True and cpf1 + 1 or 0)
    cnpj2 = (cnpj.validate(linha['lojadaultimacompra']) == True and cpf1 + 1 or 0)

print("Foi veriricado que há",cpf1,"CPF validos na coluna cpf do arquivo Base.txt! \n")
print("Foi veriricado que há",cnpj1,"CNPJs validos na coluna lojamaisfrequente do arquivo Base.txt! \n")
print("Foi veriricado que há",cnpj2,"CNPJs validos na coluna lojadaultimacompra do arquivo Base.txt! \n")