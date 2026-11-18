#fila de espera
from tkinter import ttk

import customtkinter as ctk

from views.janela_view import aba_fila

entrada_telefone = ctk.CTkEntry(aba_fila, width=300, placeholder_text="Telefone do cliente cadastrado")
entrada_telefone.grid(row=0, column=0, padx=(0, 8), pady=(0, 8), sticky="w")
TEXTO_SEM_SERVICO = "Selecione o serviço"
caixa_servico = ctk.CTkComboBox(aba_fila, width=300, values=[TEXTO_SEM_SERVICO], state="readonly")
caixa_servico.set(TEXTO_SEM_SERVICO)
caixa_servico.grid(row=0, column=1, padx=(0, 8), pady=(0, 8), sticky="w")
botao_entrar = ctk.CTkButton(aba_fila, text="Entrar na fila")
botao_entrar.grid(row=0, column=2, pady=(0, 8), sticky="w")
botao_atender = ctk.CTkButton(aba_fila, text="Atender próximo")
botao_atender.grid(row=0, column=3, padx=8, pady=(0, 8), sticky="w")

tabela = ttk.Treeview(aba_fila, columns=("posicao", "nome", "telefone", "servico", "entrada"), show="headings")
tabela.heading("posicao", text="Posição")
tabela.heading("nome", text="Nome")
tabela.heading("telefone", text="Telefone")
tabela.heading("servico", text="Serviço")
tabela.heading("entrada", text="Entrou em")
for coluna in ("posicao", "nome", "telefone", "servico", "entrada"):
    tabela.column(coluna, anchor="center")
tabela.column("posicao", width=70)
tabela.column("nome", width=250)
tabela.grid(row=1, column=0, columnspan=5, sticky="nsew")

aba_fila.grid_columnconfigure(4, weight=1)
aba_fila.grid_rowconfigure(1, weight=1)


# Funcoes
def ligar_botoes(funcao_entrar, funcao_atender):
    botao_entrar.configure(command=funcao_entrar)
    botao_atender.configure(command=funcao_atender)


def ler_telefone():
    return entrada_telefone.get().strip()


def limpar_telefone():
    entrada_telefone.delete(0, "end")


def ler_servico():
    return caixa_servico.get()


def limpar_servico():
    caixa_servico.set(TEXTO_SEM_SERVICO)


def mostrar_opcoes_servico(textos):
    """Troca a lista da caixa de serviço, mantendo a escolha se ela ainda existir."""
    escolhido = caixa_servico.get()
    caixa_servico.configure(values=textos if textos else [TEXTO_SEM_SERVICO])
    if escolhido not in textos:
        caixa_servico.set(TEXTO_SEM_SERVICO)


def mostrar_fila(linhas):
    for item in tabela.get_children():
        tabela.delete(item)
    for linha in linhas:
        tabela.insert("", "end", values=linha)