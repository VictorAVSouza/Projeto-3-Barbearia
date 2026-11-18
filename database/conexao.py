# conexao.py

import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()   

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
    conexao = conectar()
    print("Conectado ao MySQL, versão", conexao.get_server_info())
    conexao.close()
