# servico_repository.py — REPOSITORY
# O ÚNICO arquivo que conversa com o banco sobre serviços.
from mysql.connector import IntegrityError

from database.conexao import conectar


def listar():
    """Devolve todos os serviços: uma lista de dicionários."""
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, preco FROM servicos ORDER BY id")
        return cursor.fetchall()
    finally:
        conexao.close()


def buscar_por_id(id_servico):
    """Devolve um serviço (dicionário) ou None se não encontrar."""
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, preco FROM servicos WHERE id = %s", (id_servico,))
        return cursor.fetchone()
    finally:
        conexao.close()


def adicionar(nome, preco):
    """Cadastra um serviço. Devolve True se deu certo,
    ou False se já existir um serviço com esse nome."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO servicos (nome, preco) VALUES (%s, %s)", (nome, preco))
        conexao.commit()
        return True
    except IntegrityError:   # nome repetido
        return False
    finally:
        conexao.close()


def atualizar(id_servico, nome, preco):
    """Altera um serviço. Devolve True se deu certo,
    ou False se o nome já pertencer a outro serviço."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("UPDATE servicos SET nome = %s, preco = %s WHERE id = %s",
                       (nome, preco, id_servico))
        conexao.commit()
        return True
    except IntegrityError:   # nome repetido
        return False
    finally:
        conexao.close()


def remover(id_servico):
    """Apaga um serviço pelo id. Devolve True se apagou."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM servicos WHERE id = %s", (id_servico,))
        conexao.commit()
        return cursor.rowcount > 0
    finally:
        conexao.close()