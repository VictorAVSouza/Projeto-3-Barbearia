#mensagem de aviso e erro
from tkinter import messagebox


def mostrar_atencao(mensagem):
    """Dado digitado errado ou pedido que não dá para fazer."""
    messagebox.showwarning("Atenção", mensagem)


def mostrar_erro(mensagem):
    messagebox.showerror("Erro", mensagem)


def mostrar_erro_banco(erro):
    """Erro do banco: MySQL desligado, senha errada, tabela inexistente..."""
    messagebox.showerror(
        "Erro no banco de dados",
        f"{erro}\n\nConfira se o MySQL está ligado e se o arquivo .env está certo.")


def mostrar_aviso(mensagem):
    """Deu tudo certo."""
    messagebox.showinfo("Sucesso", mensagem)


def confirmar(pergunta):
    """Pergunta Sim/Não. Devolve True se o usuário clicar em Sim."""
    return messagebox.askyesno("Confirmar", pergunta)
