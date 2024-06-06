from db_access import db_connection


def insert_Table(dados):
    conexao = db_connection.consultar()
    updados = conexao.cursor()

    #contagem dos registros
    registrosinseridos = []
    
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
        RETURNING id
        """    
    #for f in dados:
    for index, f in dados.iterrows():

     #Metodo responsavel por enviar os dados.
     updados.execute(conteudo,f)

     # Salvando commit referenteas inserções.
     conexao.commit()
     
     # Verificando quantos registros foram inseridos.     
     registrosinseridos.append((updados.fetchall()))
    return len(registrosinseridos)