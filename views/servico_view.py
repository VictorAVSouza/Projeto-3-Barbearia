from tkinter import ttk

import customtkinter as ctk

from views.janela_view import aba_servicos

formulario = ctk.CTkFrame(aba_servicos)
formulario.grid(row=0, column=0, padx=(0, 10), sticky="n")

entrada_nome = ctk.CTkEntry(formulario, width=250, placeholder_text="Nome do serviço")
entrada_nome.grid(row=0, column=0, padx=15, pady=(15, 8))
entrada_preco = ctk.CTkEntry(formulario, width=250, placeholder_text="Preço (ex.: 25,50)")
entrada_preco.grid(row=1, column=0, padx=15, pady=8)

botao_salvar = ctk.CTkButton(formulario, text="Salvar", width=250)
botao_salvar.grid(row=2, column=0, padx=15, pady=4)
botao_novo = ctk.CTkButton(formulario, text="Novo", width=250)
botao_novo.grid(row=3, column=0, padx=15, pady=4)
botao_excluir = ctk.CTkButton(formulario, text="Excluir", width=250, fg_color="#c0392b")
botao_excluir.grid(row=4, column=0, padx=15, pady=(4, 15))

tabela = ttk.Treeview(aba_servicos, columns=("id", "nome", "preco"), show="headings")
tabela.heading("id", text="ID")
tabela.heading("nome", text="Serviço")
tabela.heading("preco", text="Preço")
tabela.column("id", width=40, anchor="center")
tabela.column("nome", width=300, anchor="center")
tabela.column("preco", width=100, anchor="center")
tabela.grid(row=0, column=1, sticky="nsew")

aba_servicos.grid_columnconfigure(1, weight=1)
aba_servicos.grid_rowconfigure(0, weight=1)


#funcoes
def ligar_botoes(funcao_novo, funcao_salvar, funcao_excluir, funcao_selecionar):
    botao_novo.configure(command=funcao_novo)
    botao_salvar.configure(command=funcao_salvar)
    botao_excluir.configure(command=funcao_excluir)
    tabela.bind("<<TreeviewSelect>>", funcao_selecionar)


def ler_formulario():
    return entrada_nome.get().strip(), entrada_preco.get().strip()


def limpar_formulario():
    entrada_nome.delete(0, "end")
    entrada_preco.delete(0, "end")


def preencher_formulario(nome, preco):
    limpar_formulario()
    entrada_nome.insert(0, nome)
    entrada_preco.insert(0, preco)


def mostrar_servicos(linhas):
    for item in tabela.get_children():
        tabela.delete(item)
    for linha in linhas:
        tabela.insert("", "end", values=linha)


def id_selecionado():
    selecao = tabela.selection()
    if len(selecao) == 0:
        return None
    return int(tabela.item(selecao[0], "values")[0])


def desmarcar_tabela():
    tabela.selection_remove(tabela.selection())