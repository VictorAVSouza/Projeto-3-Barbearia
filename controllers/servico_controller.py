from models import servico_model as model
from repositories import servico_repository as repositorio
from views import servico_view as view
from views import mensagens_view as mensagens


def iniciar():
    view.ligar_botoes(novo, salvar, excluir, selecionar)
    atualizar_tabela()


def atualizar_tabela():
    try:
        servicos = repositorio.listar()
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    linhas = []
    for s in servicos:
        linhas.append((s["id"], s["nome"], "R$ " + model.texto_preco(s["preco"])))
    view.mostrar_servicos(linhas)


def novo():
    view.limpar_formulario()
    view.desmarcar_tabela()


def selecionar(evento=None):
    id_servico = view.id_selecionado()
    if id_servico is None:
        return
    try:
        s = repositorio.buscar_por_id(id_servico)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    if s is None:
        return
    view.preencher_formulario(s["nome"], model.texto_preco(s["preco"]))


def salvar():
    nome, texto = view.ler_formulario()

    mensagem = model.validar_servico(nome, texto)
    if mensagem is not None:
        mensagens.mostrar_atencao(mensagem)
        return

    preco = model.converter_preco(texto)
    id_servico = view.id_selecionado() 
    try:
        if id_servico is None:
            deu_certo = repositorio.adicionar(nome, preco)
        else:
            deu_certo = repositorio.atualizar(id_servico, nome, preco)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return

    if not deu_certo:
        mensagens.mostrar_erro("Já existe um serviço com esse nome.")
        return

    mensagens.mostrar_aviso("Serviço salvo!")
    novo()
    atualizar_tabela()


def excluir():
    id_servico = view.id_selecionado()
    if id_servico is None:
        mensagens.mostrar_atencao("Clique em um serviço da tabela para excluir.")
        return
    if not mensagens.confirmar("Excluir este serviço?"):
        return
    try:
        removeu = repositorio.remover(id_servico)
    except Exception as erro:
        mensagens.mostrar_erro_banco(erro)
        return
    if not removeu:
        mensagens.mostrar_erro("Esse serviço não existe mais.")
    novo()
    atualizar_tabela()
