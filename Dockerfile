# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório local atual para o diretório de trabalho dentro do contêiner
COPY . .

# Defina o comando padrão para ser executado quando o contêiner iniciar
CMD ["python", "app/main.py"]
