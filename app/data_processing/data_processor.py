#importando biblioteca
import re

#cabeçalho base
colum = ['CPF',
         'PRIVATE',
         'INCOMPLETO',
         'DATA_DA_ULTIMA_COMPRA',
         'TICKET_MEDIO',
         'TICKET_DA_ULTIMA_COMPRA',
         'LOJA_MAIS_FREQUENTE',
         'LOJA_DA_ULTIMA_COMPRA'
        ]
#funçôes responsavel pela formatação dos campos.
def string_to_snake_case(caracter):    
    caracter = re.sub("/", " ", caracter)    # substitui / por espaço
    caracter = re.sub(" +", " ", caracter)   # substitui múltiplos espaços por um espaço
    caracter = re.sub(" ", "_", caracter)    # substitui espaço por _
    caracter = re.sub("([a-z0-9])([A-Z])", r"\1_\2", caracter)  # adiciona _ entre letras minúsculas e maiúsculas    
    return caracter
  
def string_to_pascal_case(caracter):
    pascal_case = "".join([palavra.capitalize() for palavra in string_to_snake_case(caracter).split("_")])    
    return pascal_case

#função responsavel por fazer a leitura do arquivo Base.txt
def leituraDados():
  with open(r"./Base.txt") as base:
    dadosF = []
    """
    #Estamos pegando sempre a partir da primeira linha. Já que a primeira é um head.
    for l in (base.readlines()[:1]):
    cabecalho = [string_to_pascal_case(l) for l in colum]
     
    ##inserindo o create table
    insert = "CREATE TABLE clientes_temp (id INTEGER GENERATED ALWAYS AS IDENTITY,\n"

    for m in cabecalho:
    insert += f" {m} VARCHAR(18), \n"

    ##vamos remover a ultima vergula, para poder fechar corretamente metodo de insert no banco.
    insert = insert.rstrip(',\n')+"\n);"
    """
    #Estamos pegando sempre a partir da segunda Linha. Já que a primeira é um head.
    for l in (base.readlines()[1::]):        
        dados = tuple(l.split())
        dadosF.append(dados)

  return dadosF