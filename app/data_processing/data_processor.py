#importando bibliotecas
import pandas as pd
import numpy as np
from pycpfcnpj import cpf, cnpj

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

#Função responsavel por ler o arquivo Base.txt 
#e alterar colunas e validar os campos >> (cpf,lojamaisfrequente,lojadaultimacompra)
def leituraDados():
  with open(r"./Base.txt") as base:
    #Estamos pegando sempre a partir da segunda linha. Já que a primeira é um cabeçalho.
    dadoslist = [tuple(l.split()) for l in base.readlines()[1:]]

  #transformando em um DataFrame, usando COLUM para definir o cabeçalho.
  dados = pd.DataFrame(dadoslist, columns=COLUM)

  #declarando variaveis zeradas
  cpf1 = 0
  cnpj1 = 0
  cnpj2 = 0
  for posicao, linha in dados.iterrows():
  #vamos fazer a verificação por coluna
    cpf1 = (cpf.validate(linha['cpf'])  == True and cpf1 + 1 or 0)
    cnpj1 = (cnpj.validate(linha['lojamaisfrequente']) == True and cpf1 + 1 or 0)
    cnpj2 = (cnpj.validate(linha['lojadaultimacompra']) == True and cpf1 + 1 or 0)

  #Estamos tratando os caracteres 'NULL' para NULL.
  dados.replace('NULL', None, inplace=True) 

  print("Foi verificado que há",cpf1,"CPF validos na coluna cpf do arquivo Base.txt! \n")
  print("Foi verificado que há",cnpj1,"CNPJs validos na coluna lojamaisfrequente do arquivo Base.txt! \n")
  print("Foi verificado que há",cnpj2,"CNPJs validos na coluna lojadaultimacompra do arquivo Base.txt! \n")

  return dados