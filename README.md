# Importação Txt

## Instruções de Instalação e Configuração

### Requisitos

Antes de iniciar a instalação, certifique-se de que você tem os seguintes requisitos atendidos:

 - Docker
 - Docker Compose

### Passos de Instalação

 1. **Clone o Repositório**
 
    ```shell
    git clone https://github.com/LudimarPadilha/importTxt'
    ```

 3. **Configuração do Docker-Compose**
    Será necessario verificar se o arquivo ***docker-compose.yml*** está presente no diretorio raiz do projeto. Esté arquivo é responsavel pela configuração necessária para iniciar os contêineres Docker.

 4. **Construir e Iniciar os Contêineres**
    
    Execute o seguinte comando para construir e iniciar os contêineres Docker:
    
    ```shell
    docker-compose up --build
    ```
    Esse comando ira baixar as imagens que foram definidas no arquivo ***docker-compose.yml***

### Estrutura do Projeto
    
```
  
  ├── app
  │   ├── data_processing
  │   └── db_access
  │   └── sql
  │   └── main.py
  ├── db
  ├── README.md
  └── docker-compose.yml
 ```

 **.app** Nele contem o codigo fonte do projeto.
 
   **-  data_processing** Nele contem a estrutura de leitura. Junto com uma trativa de caracteres e validação.
   
   **-  db_access** Contem os metodos de conexão para banco criado, junto com as insereções de dados e atualizações de dados.

   **-  sql** Contem o arquivo responsavel para higienização de dados.
   
   **-  main.py** Arquivo responsavel por starta o projeto.
   
**.db** Nesse diretorio contem um arquivo com a estrutura do banco de dados.

**.README.md** Arquivo responsavel por instruções.

**.docker-compose.yml** Responsavel por construir e iniciar os contêineres

### Estrutura do Banco de Dados
  ```
  CREATE TABLE public.clientes_temp (
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
  ```
    ## Alterações e Inclusões
    ```
    CREATE TABLE public.clientes_temp (
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
    ```
  
    ## Campo sequencial (Auto Incremental)
    
    ```
      ALTER TABLE public.clientes_temp ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
          SEQUENCE NAME public.clientes_temp_id_seq
          START WITH 1
          INCREMENT BY 1
          NO MINVALUE
          NO MAXVALUE
          CACHE 1
      );
    ```
     Alteração reealizado para gerar automaticamente o valor da coluna id da tabela clientes_temp.
  

  ### Arquitetura
  A arquitetura do projeto segue uma abordagem de microserviços utilizando contêineres Docker. Cada Serviço da aplicação é isolado em um contêiner separado, permitindo escalabilidade e facilidade de manutenção.
  
   #### Compooentes principais.
 - **Aplicação Web (app):** Está é a parte principal da aplicação, contendo todo o código relacionado ao projeto.
 - **Banco de Dados (db):** Este diretório contém a configuração e os scripts necessários para o banco de dados. O Banco de dados é executado em um contêiner separado, garantindo isolamento e independência
 - **Docker-compose:** Arquivo responsavel por definir os serviços, redes e volumes necessários para a aplicação. Isso inclui definições para a aplicação web e o banco de dados.

  ### Solução Técnica
  - **Isolamento com Docker:** Utilizando a ferramenta Docker, cada componente da aplicação é executado em um ambiente isolado, o que facilita o desenvolvimento, testes e implantação.
  - **Facilidade com Docker-compose:** Executando apenas o comando ***docker-compose up***, todos os serviços necessários são iniciados, praticamente um processo de setup.
  - **Portabilidade:** A utilização de contêineres Docker torna a aplicação portátil, permitindo que ela seja executado em qualquer ambiente que suporte Docker.

## FIM  