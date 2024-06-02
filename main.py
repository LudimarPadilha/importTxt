##importando funções
import subprocess
import time
from src import functions

# Executa o Docker Compose
subprocess.run("docker-compose up -d", shell=True)

# Aguarda alguns segundos para garantir que os contêineres estejam prontos
time.sleep(3)

#Executando o projeto
functions.starproject()

# Desliga os contêineres depois que a função functions.starproject() terminar!
subprocess.run("docker-compose down", shell=True)