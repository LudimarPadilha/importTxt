##importando biblioteca e funções
from src.db_access import db_connection
from src.db_access import createTable
from src.db_access import insertTable
from src.data_processing import data_processor
from src.data_processing import function
from warnings import filterwarnings


def starproject():
    #Aviso sobre usar a biblioteca SQLAlchemy e não as demais.
    filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')

    print("Iniciando conexão!")
    db_connection.connection_postgres()

    print("Iniciando a criação da tabela!")
    createTable.creat_Table()

    print("Iniciando a leitura de dados do arquivo Base.txt!")
    leituraBase = data_processor.leituraDados()
    print("Foi realizado a leitura de",len(leituraBase),"linhas. \n")

    print("Iniciando a inserção de dados na tabela clientes_temp!! \n")
    insertTable.insert_Table(leituraBase)

    #Atualizando as informações do campos que contem caractes especiais.
    function.limpaDados(db_connection.transition('postGres'))

    #Função responsavel por chamar consultas realizadas atravez do pandas.
    function.consultaDataFrame()