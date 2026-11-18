from models import cliente_model as model
from repositories import cliente_repository as repositorio
from views import cliente_view as view
from views import mensagens_view as mensagens


def iniciar():
    view.ligar_botoes(novo, salvar, excluir, selecionar, buscar)
    atualizar_tabela()


def atualizar_tabela():
    termo = view.ler_busca()
    try:
        if termo == "":
            clientes = repositorio.listar()
        else:
            clientes = repositorio.buscar(termo)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return

    linhas = []
    for c in clientes:
        nascimento = c["data_nascimento"]
        linhas.append((c["id"], c["nome"], c["telefone"], c["email"],
                       nascimento.strftime("%d/%m/%Y"),
                       model.calcular_idade(nascimento),
                       model.tipo_cliente(nascimento),
                       c["problema_quimico"]))
    view.mostrar_clientes(linhas)


def novo():
    view.limpar_formulario()
    view.desmarcar_tabela()


def buscar(evento=None):
    novo()
    atualizar_tabela()


def selecionar(evento=None):
    id_cliente = view.id_selecionado()
    if id_cliente is None:
        return
    try:
        c = repositorio.buscar_por_id(id_cliente)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    if c is None:
        return
    problema = c["problema_quimico"]
    if problema == "Nenhum":
        problema = ""
    view.preencher_formulario(c["nome"], c["telefone"], c["email"],
                              c["data_nascimento"].strftime("%d/%m/%Y"), problema)


def salvar():
    nome, telefone, email, nascimento, problema = view.ler_formulario()

    mensagem = model.validar_cliente(nome, telefone, email, nascimento, problema)
    if mensagem is not None:
        mensagens.mostrar_atencao(mensagem)
        return

    telefone = model.apenas_digitos(telefone)
    data = model.converter_data(nascimento)
    if problema == "":
        problema = "Nenhum"

    id_cliente = view.id_selecionado()
    try:
        if id_cliente is None:
            deu_certo = repositorio.adicionar(nome, telefone, email, data, problema)
        else:
            deu_certo = repositorio.atualizar(id_cliente, nome, telefone, email, data, problema)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return

    if not deu_certo:
        mensagens.mostrar_erro("Já existe um cliente com esse telefone.")
        return

    mensagens.mostrar_aviso(f"Cliente salvo! Tipo: {model.tipo_cliente(data)}.")
    novo()
    atualizar_tabela()


def excluir():
    id_cliente = view.id_selecionado()
    if id_cliente is None:
        mensagens.mostrar_atencao("Clique em um cliente da tabela para excluir.")
        return
    if not mensagens.confirmar("Excluir este cliente? Ele também sai da fila de espera."):
        return
    try:
        removeu = repositorio.remover(id_cliente)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    if not removeu:
        mensagens.mostrar_erro("Esse cliente não existe mais.")
    novo()
    atualizar_tabela()
