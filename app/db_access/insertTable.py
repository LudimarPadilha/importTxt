from db_access import db_connection

def insert_Table(dados):
    transition = db_connection.transition('postGre')

    #Responsavel pela estrutura do insert!
    conteudo = """
    INSERT INTO clientes_temp(
            CPF,
            PRIVATE,
            INCOMPLETO,
            DATA_DA_ULTIMA_COMPRA,
            TICKET_MEDIO,
            TICKET_DA_ULTIMA_COMPRA,
            LOJA_MAIS_FREQUENTE,
            LOJA_DA_ULTIMA_COMPRA
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """
    #transition.executemany(conteudo,dados)
    #for f in range(0, len(dados), 2000):
    # dadosF = dados[f:f+20000]
    # transition.executemany(conteudo,dadosF)
    for f in dados:
     #Estamos tratando os caracteres 'NULL' para NULL.
     dadosF = [None if elemento  == 'NULL' else elemento  for elemento  in f]
     #dadosF = (f[5] == 'pandas' and connection_base or connection_base.cursor())

     #dadosF = ["" if elemento  == "'" else elemento  for elemento  in f[5]]
     ##metodo responsavel por enviar os dados.
     transition.execute(conteudo,(dadosF))