from models import cliente_model
from repositories import cliente_repository
from repositories import fila_repository as repositorio
from repositories import servico_repository
from models import servico_model
from views import fila_view as view
from views import janela_view
from views import mensagens_view as mensagens


# texto da caixa de serviço -> id do serviço
servicos_por_texto = {}


def iniciar():
    view.ligar_botoes(entrar, atender)
    janela_view.abas.configure(command=ao_trocar_aba)
    atualizar_servicos()
    atualizar_tabela()


def ao_trocar_aba():
    if janela_view.abas.get() == "Fila de espera":
        atualizar_servicos()


def atualizar_servicos():
    try:
        servicos = servico_repository.listar()
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    servicos_por_texto.clear()
    for s in servicos:
        texto = f"{s['nome']} - R$ {servico_model.texto_preco(s['preco'])}"
        servicos_por_texto[texto] = s["id"]
    view.mostrar_opcoes_servico(list(servicos_por_texto.keys()))


def atualizar_tabela():
    try:
        fila = repositorio.listar()
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    linhas = []
    for posicao, pessoa in enumerate(fila, start=1):
        servico = pessoa["servico"] if pessoa["servico"] is not None else "—"
        linhas.append((f"{posicao}º", pessoa["nome"], pessoa["telefone"], servico,
                       pessoa["criado_em"].strftime("%d/%m %H:%M")))
    view.mostrar_fila(linhas)


def entrar():
    telefone = view.ler_telefone()
    mensagem = cliente_model.validar_telefone(telefone)
    if mensagem is not None:
        mensagens.mostrar_atencao(mensagem)
        return
    telefone = cliente_model.apenas_digitos(telefone)

    id_servico = servicos_por_texto.get(view.ler_servico())
    if id_servico is None:
        mensagens.mostrar_atencao("Escolha o tipo de serviço antes de entrar na fila.")
        return

    try:
        cliente = cliente_repository.buscar_por_telefone(telefone)
        if cliente is None:
            mensagens.mostrar_atencao("Cliente não cadastrado. Cadastre na aba Clientes primeiro.")
            return
        if servico_repository.buscar_por_id(id_servico) is None:
            mensagens.mostrar_atencao("Esse serviço não existe mais. Escolha outro.")
            atualizar_servicos()
            return
        deu_certo = repositorio.adicionar(cliente["id"], id_servico)
        posicao = repositorio.contar()
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return

    if not deu_certo:
        mensagens.mostrar_atencao(f"{cliente['nome']} já está na fila.")
        return

    mensagens.mostrar_aviso(f"{cliente['nome']} entrou na fila na posição {posicao}.")
    view.limpar_telefone()
    view.limpar_servico()
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
    if proximo["servico"] is None:
        mensagens.mostrar_aviso(f"Chamando: {proximo['nome']}!")
    else:
        mensagens.mostrar_aviso(f"Chamando: {proximo['nome']}!\nServiço: {proximo['servico']}")
    atualizar_tabela()