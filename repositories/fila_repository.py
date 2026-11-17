# fila_repository.py — REPOSITORY
# O ÚNICO arquivo que conversa com o banco sobre a fila de espera.
# A ordem da fila é a ordem do id: quem entrou primeiro tem o menor id.
from mysql.connector import IntegrityError

from database.conexao import conectar


def listar():
    """Devolve a fila em ordem de chegada: uma lista de dicionários
    (id, nome, telefone, criado_em). O primeiro da lista é o próximo a ser atendido."""
    sql = ("SELECT f.id, c.nome, c.telefone, f.criado_em "
           "FROM fila_espera f JOIN clientes c ON c.id = f.id_cliente "
           "ORDER BY f.id")
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conexao.close()


def buscar_primeiro():
    """Devolve o primeiro da fila (dicionário) ou None se a fila estiver vazia."""
    sql = ("SELECT f.id, c.nome, c.telefone, f.criado_em "
           "FROM fila_espera f JOIN clientes c ON c.id = f.id_cliente "
           "ORDER BY f.id LIMIT 1")
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchone()
    finally:
        conexao.close()


def contar():
    """Devolve quantas pessoas estão na fila."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM fila_espera")
        return cursor.fetchone()[0]
    finally:
        conexao.close()


def adicionar(id_cliente):
    """Coloca o cliente no fim da fila. Devolve True se deu certo,
    ou False se ele já estiver na fila."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO fila_espera (id_cliente) VALUES (%s)", (id_cliente,))
        conexao.commit()
        return True
    except IntegrityError:   # cliente já está na fila
        return False
    finally:
        conexao.close()


def remover(id_fila):
    """Tira uma pessoa da fila pelo id da fila. Devolve True se removeu."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM fila_espera WHERE id = %s", (id_fila,))
        conexao.commit()
        return cursor.rowcount > 0
    finally:
        conexao.close()
