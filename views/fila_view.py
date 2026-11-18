#fila de espera
from tkinter import ttk

import customtkinter as ctk

from views.janela_view import aba_fila

entrada_telefone = ctk.CTkEntry(aba_fila, width=300, placeholder_text="Telefone do cliente cadastrado")
entrada_telefone.grid(row=0, column=0, padx=(0, 8), pady=(0, 8), sticky="w")
botao_entrar = ctk.CTkButton(aba_fila, text="Entrar na fila")
botao_entrar.grid(row=0, column=1, pady=(0, 8), sticky="w")
botao_atender = ctk.CTkButton(aba_fila, text="Atender próximo")
botao_atender.grid(row=0, column=2, padx=8, pady=(0, 8), sticky="w")

tabela = ttk.Treeview(aba_fila, columns=("posicao", "nome", "telefone", "entrada"), show="headings")
tabela.heading("posicao", text="Posição")
tabela.heading("nome", text="Nome")
tabela.heading("telefone", text="Telefone")
tabela.heading("entrada", text="Entrou em")
tabela.column("posicao", width=70)
tabela.column("nome", width=250)
tabela.grid(row=1, column=0, columnspan=4, sticky="nsew")

aba_fila.grid_columnconfigure(3, weight=1)
aba_fila.grid_rowconfigure(1, weight=1)


# Funcoes
def ligar_botoes(funcao_entrar, funcao_atender):
    botao_entrar.configure(command=funcao_entrar)
    botao_atender.configure(command=funcao_atender)


def ler_telefone():
    return entrada_telefone.get().strip()


def limpar_telefone():
    entrada_telefone.delete(0, "end")


def mostrar_fila(linhas):
    for item in tabela.get_children():
        tabela.delete(item)
    for linha in linhas:
        tabela.insert("", "end", values=linha)
