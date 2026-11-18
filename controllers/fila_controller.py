from models import cliente_model
from repositories import cliente_repository
from repositories import fila_repository as repositorio
from views import fila_view as view
from views import mensagens_view as mensagens


def iniciar():
    view.ligar_botoes(entrar, atender)
    atualizar_tabela()


def atualizar_tabela():
    try:
        fila = repositorio.listar()
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    linhas = []
    for posicao, pessoa in enumerate(fila, start=1):
        linhas.append((f"{posicao}º", pessoa["nome"], pessoa["telefone"],
                       pessoa["criado_em"].strftime("%d/%m %H:%M")))
    view.mostrar_fila(linhas)


def entrar():
    telefone = view.ler_telefone()
    mensagem = cliente_model.validar_telefone(telefone)
    if mensagem is not None:
        mensagens.mostrar_atencao(mensagem)
        return
    telefone = cliente_model.apenas_digitos(telefone)

    try:
        cliente = cliente_repository.buscar_por_telefone(telefone)
        if cliente is None:
            mensagens.mostrar_atencao("Cliente não cadastrado. Cadastre na aba Clientes primeiro.")
            return
        deu_certo = repositorio.adicionar(cliente["id"])
        posicao = repositorio.contar()
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return

    if not deu_certo:
        mensagens.mostrar_atencao(f"{cliente['nome']} já está na fila.")
        return

    mensagens.mostrar_aviso(f"{cliente['nome']} entrou na fila na posição {posicao}.")
    view.limpar_telefone()
    atualizar_tabela()


def atender():
    try:
        proximo = repositorio.buscar_primeiro()
        if proximo is None:
            mensagens.mostrar_atencao("Ninguém na fila.")
            return
        repositorio.remover(proximo["id"])
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    mensagens.mostrar_aviso(f"Chamando: {proximo['nome']}!")
    atualizar_tabela()
