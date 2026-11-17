# cliente_repository.py — REPOSITORY
# O ÚNICO arquivo que conversa com o banco sobre clientes.
# O resto do sistema só chama estas funções e nunca escreve SQL.
from mysql.connector import IntegrityError

from database.conexao import conectar


def listar():
    """Devolve todos os clientes: uma lista de dicionários, em ordem alfabética."""
    sql = ("SELECT id, nome, telefone, email, data_nascimento, problema_quimico "
           "FROM clientes ORDER BY nome")
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conexao.close()


def buscar(termo):
    """Devolve os clientes que têm o termo no nome ou no telefone."""
    sql = ("SELECT id, nome, telefone, email, data_nascimento, problema_quimico "
           "FROM clientes WHERE nome LIKE %s OR telefone LIKE %s ORDER BY nome")
    padrao = f"%{termo}%"   # só o VALOR da busca é montado aqui; o SQL continua com %s
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql, (padrao, padrao))
        return cursor.fetchall()
    finally:
        conexao.close()


def buscar_por_id(id_cliente):
    """Devolve um cliente (dicionário) ou None se não encontrar."""
    sql = ("SELECT id, nome, telefone, email, data_nascimento, problema_quimico "
           "FROM clientes WHERE id = %s")
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql, (id_cliente,))
        return cursor.fetchone()
    finally:
        conexao.close()


def buscar_por_telefone(telefone):
    """Devolve um cliente (dicionário) ou None se não encontrar."""
    sql = ("SELECT id, nome, telefone, email, data_nascimento, problema_quimico "
           "FROM clientes WHERE telefone = %s")
    conexao = conectar()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql, (telefone,))
        return cursor.fetchone()
    finally:
        conexao.close()


def adicionar(nome, telefone, email, nascimento, problema):
    """Cadastra um cliente. Devolve True se deu certo,
    ou False se o telefone já estiver cadastrado."""
    sql = ("INSERT INTO clientes (nome, telefone, email, data_nascimento, problema_quimico) "
           "VALUES (%s, %s, %s, %s, %s)")
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (nome, telefone, email, nascimento, problema))
        conexao.commit()
        return True
    except IntegrityError:   # telefone repetido
        return False
    finally:
        conexao.close()


def atualizar(id_cliente, nome, telefone, email, nascimento, problema):
    """Altera um cliente. Devolve True se deu certo,
    ou False se o telefone já pertencer a outro cliente."""
    sql = ("UPDATE clientes SET nome = %s, telefone = %s, email = %s, "
           "data_nascimento = %s, problema_quimico = %s WHERE id = %s")
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (nome, telefone, email, nascimento, problema, id_cliente))
        conexao.commit()
        return True
    except IntegrityError:   # telefone repetido
        return False
    finally:
        conexao.close()


def remover(id_cliente):
    """Apaga um cliente pelo id. Devolve True se apagou."""
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexao.commit()
        return cursor.rowcount > 0
    finally:
        conexao.close()
