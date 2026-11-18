# conexao.py
# Guarda os dados de acesso ao MySQL em um só lugar.
# A senha NÃO fica escrita aqui: ela vem do arquivo .env (que não vai para o GitHub).
import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()   # lê o arquivo .env da pasta do projeto

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": 3306,
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "barbearia_abobrinha"),
}


def conectar():
    """Abre e devolve uma conexão com o banco."""
    return mysql.connector.connect(**CONFIG)


if __name__ == "__main__":
    # Teste rápido, no terminal:  python database/conexao.py
    # Se der erro, a mensagem diz o que está errado (veja "Erros comuns" no README).
    conexao = conectar()
    print("Conectado ao MySQL, versão", conexao.get_server_info())
    conexao.close()
