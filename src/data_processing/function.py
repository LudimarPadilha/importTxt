##importando biblioteca e funções
import pandas as pd
import pandas.io.sql as psql
import re
from src.db_access import db_connection

#Consultado tabelas do PostGres
def consulta_banco(sql, conexao):  
  #fazendo a chamada
  conexao.execute(sql)
  recset = conexao.fetchall()
  for rec in recset:
    #registros.append(rec)
    print(rec)
  #conexao.close()
  #return registros

#Update para tratar os dados com caracteres especiais.
def limpaDados(conexao):
  conexao.execute("""UPDATE CLIENTES_TEMP
                     SET CPF = translate(CPF, '.-/', ''),
                         LOJA_MAIS_FREQUENTE = translate(LOJA_MAIS_FREQUENTE, '.-/', ''),
                         LOJA_DA_ULTIMA_COMPRA = translate(LOJA_DA_ULTIMA_COMPRA, '.-/', '')
                  """,conexao)


#função responsavel por trazar a consulta de banco.
def consultaPandas(sql, conexao):
 dataframe = psql.read_sql(sql, conexao)
 return dataframe


#Vamos criar uma class onde vai ser atribuido a logica para validar CPF.
class validaDados:
  def __init__(self, cpf):
    self.cpf = cpf

  def valida(self):
      #validando se está vazio ou se contem 11 digitos.
     if (not self.cpf) or (len(self.cpf) != 11):
        return False
     
     if not self._digito1(self.cpf) or not self._digito2(self.cpf):
         return False
          
     return True     
  
  @staticmethod
  #Logica para estar pegando os primeiros 9 digitos.
  def _digito1(cpf):
    regraCpf1 = sum (int(a)*b for a, b in zip (cpf[0:9], range(10, 1, -1)))
    regraDigito1 = (regraCpf1 * 10 %11) % 10
    #Aqui vamos estar confrontando as informações se a logica aplicada na variavel regraDigito1 se está correta!
    return (int(cpf[9]) == regraDigito1)

  @staticmethod
  def _digito2(cpf):
    regraCpf2 = sum (int(a)*b for a, b in zip (cpf[0:10], range(11, 1, -1)))
    regraDigito2 = (regraCpf2 * 10 %11) % 10
    #Aqui vamos estar confrontando as informações se a logica aplicada na variavel regraDigito2 se está correta!
    return (int(cpf[10]) == regraDigito2)

  @property
  def cpf(self):
    return self._cpf
  
  @cpf.setter
  def cpf(self, cpf):
    self._cpf = self._so_numeros(cpf)

  @staticmethod
  #Função responsavel por estar retirando caracteres especiais do CPF.
  def _so_numeros(cpf):
    return re.sub(r'[^0-9]','',cpf)
  

def validaDadosCPFeCNPJ(insert):   
   #Tratamento para retirar caracteres especiais, deixando apenas numeros da list inteiro.
   if insert != None:
    inteiro = ([int(numeros) for numeros in insert if numeros.isdigit()])
    
    #logica para pegar o CPF:
    if len(inteiro) == 11:
      validaDigit1 = False
      validaDigit2 = False

      #Aplicando a logica para validar o resultado. #Usaremos as funções zip e range.
      ##################    VALIDANDO O PRIMEIRO DIGITO   ##################
      #primeiro pegamos os primeiros 9 digitos da variavel inteiro.
      #Depois fazemos a leitura de cada posição e multiplicamos os valores entre ordem decrescente começando de 10 e terminando em 2.
      #Exemplo, se o primeiro digito for 4 para posição 10, então será feito 4 * 10, assim retornando o valor 40.
      regraCpf_1 = sum (a*b for a, b in zip (inteiro[0:9], range(10, 1, -1)))
      regraDigito_1 = (regraCpf_1 * 10 %11) % 10

      #Aqui vamos estar confrontando as informações se a logica aplicada na variavel regraCpf está correta!
      validaDigit1 = (inteiro[9] == regraDigito_1 and True or False)

          ##################    VALIDANDO O SEGUNDO DIGITO   ##################
      #Estamos usando a mesma logica anterior, apenas mudamos para pegar um digito a mais.    
      regraCpf2 = sum (a*b for a, b in zip (inteiro[0:10], range(11, 1, -1)))
      regraDigito2 = (regraCpf2 * 10 %11) % 10

      validaDigit2 = (inteiro[10] == regraDigito2 and True or False)

      #Aqui estaremos validando 
      return (validaDigit1 == True and validaDigit2 == True) and True or False
        
    else:
      if len(inteiro) == 14:
          validaCnpj1 = False
          validaCnpj2 = False

          #Aplicando a logica para validar o resultado. #Usaremos as funções zip e range.
          ##################    VALIDANDO O PRIMEIRO DIGITO   ##################
          #primeiro pegamos 12 primeiras posições da variavel inteiro.
          regraReceita1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
          somaCnpj1 = sum(int(a) * b for a, b in zip(inteiro[:12], regraReceita1))
          resto1 = somaCnpj1 % 11
          regraDigito1 = 0 if resto1 < 2 else 11 - resto1

          #Aqui vamos estar confrontando as informações se a logica aplicada na variavel regraCpf está correta!
          validaCnpj1 = inteiro[12] == regraDigito1

              ##################    VALIDANDO O SEGUNDO DIGITO   ##################
          #Estamos usando a mesma logica anterior, mudamos a regra para verificar o segundo digito.
          regraReceita2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
          somaCnpj2 = sum(int(a) * b for a, b in zip(inteiro[0:13], regraReceita2))
          resto2 = somaCnpj2 % 11
          regraDigito2 = 0 if resto2 < 2 else 11 - resto2

          validaCnpj2 = inteiro[13] == regraDigito2
          #Aqui estaremos validando 
          return (validaCnpj1 == True and validaCnpj2 == True) and True or False
      else:  
       return False
       

#função responsavel por fazer consultas no banco e gravar na variavel df
def consultaDataFrame():
#Carregando dados para variavel
  df = consultaPandas('select * from CLIENTES_TEMP order by id', db_connection.transition('pandas'))

  countcpf = 0
  for cpf in df['cpf']:
    verri = validaDados(cpf)
    if (verri.valida() == True):
        countcpf = countcpf + 1
  print("Foi verificado",countcpf,"CPF no campo 'cpf' validos na busca, referente a",df['cpf'].count(),"inseridos! \n")

  #Quantidade de CNPJ Validos.
  countcnpj = 0
  for cnpj in df['loja_mais_frequente']:
    if (validaDadosCPFeCNPJ(cnpj) == True):
        countcnpj = countcnpj + 1

  print("Foi verificado",countcnpj,"registros no campo 'loja_mais_frequente' com CNPJ validos na busca, referente",df['loja_mais_frequente'].count(),"inseridos! \n")

  #Quantidade de CNPJ Validos.
  countcnpj = 0
  for cnpj in df['loja_da_ultima_compra']:
    if (validaDadosCPFeCNPJ(cnpj) == True):
        countcnpj = countcnpj + 1

  print("Foi verificado",countcnpj,"registros no campo 'loja_da_ultima_compra' com CNPJ validos na busca, referente",df['loja_da_ultima_compra'].count(),"inseridos! \n")

  #Qual é variedade de CNPJ nas colunas loja_mais_frequente e loja_da_ultima_compra.
  print("Relação de CNPJ com mais registros no campo 'loja_mais_frequente'",df['loja_mais_frequente'].value_counts().to_frame(),"\n")
  print("Relação de CNPJ com mais registros no campo 'loja_da_ultima_compra'",df['loja_da_ultima_compra'].value_counts().to_frame(),"\n")
