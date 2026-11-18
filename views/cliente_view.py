# aba dos cliente
from tkinter import ttk

import customtkinter as ctk

from views.janela_view import aba_clientes

# ---------- Formulário ----------
formulario = ctk.CTkFrame(aba_clientes)
formulario.grid(row=0, column=0, padx=(0, 10), sticky="n")

entrada_nome = ctk.CTkEntry(formulario, width=250, placeholder_text="Nome")
entrada_nome.grid(row=0, column=0, padx=15, pady=(15, 8))
entrada_telefone = ctk.CTkEntry(formulario, width=250, placeholder_text="Telefone com DDD")
entrada_telefone.grid(row=1, column=0, padx=15, pady=8)
entrada_email = ctk.CTkEntry(formulario, width=250, placeholder_text="E-mail")
entrada_email.grid(row=2, column=0, padx=15, pady=8)
entrada_nascimento = ctk.CTkEntry(formulario, width=250, placeholder_text="Nascimento (dd/mm/aaaa)")
entrada_nascimento.grid(row=3, column=0, padx=15, pady=8)
entrada_problema = ctk.CTkEntry(formulario, width=250, placeholder_text="Problema com produto químico")
entrada_problema.grid(row=4, column=0, padx=15, pady=8)

botao_salvar = ctk.CTkButton(formulario, text="Salvar", width=250)
botao_salvar.grid(row=5, column=0, padx=15, pady=4)
botao_novo = ctk.CTkButton(formulario, text="Novo", width=250)
botao_novo.grid(row=6, column=0, padx=15, pady=4)
botao_excluir = ctk.CTkButton(formulario, text="Excluir", width=250, fg_color="#c0392b")
botao_excluir.grid(row=7, column=0, padx=15, pady=(4, 15))

#buscar tabela
entrada_busca = ctk.CTkEntry(aba_clientes, placeholder_text="Buscar por nome ou telefone...")
entrada_busca.grid(row=0, column=1, sticky="new")

colunas = ("id", "nome", "telefone", "email", "nascimento", "idade", "tipo", "quimico")
titulos = ("ID", "Nome", "Telefone", "E-mail", "Nascimento", "Idade", "Tipo", "Produto químico")
tabela = ttk.Treeview(aba_clientes, columns=colunas, show="headings")
for coluna, titulo in zip(colunas, titulos):
    tabela.heading(coluna, text=titulo)
    tabela.column(coluna, width=100, anchor="center")
tabela.column("id", width=40, anchor="center")
tabela.grid(row=0, column=1, pady=(45, 0), sticky="nsew")

aba_clientes.grid_columnconfigure(1, weight=1)
aba_clientes.grid_rowconfigure(0, weight=1)


# funcoes
def ligar_botoes(funcao_novo, funcao_salvar, funcao_excluir, funcao_selecionar, funcao_buscar):
    botao_novo.configure(command=funcao_novo)
    botao_salvar.configure(command=funcao_salvar)
    botao_excluir.configure(command=funcao_excluir)
    tabela.bind("<<TreeviewSelect>>", funcao_selecionar)
    entrada_busca.bind("<KeyRelease>", funcao_buscar)


def ler_formulario():
    return (entrada_nome.get().strip(), entrada_telefone.get().strip(),
            entrada_email.get().strip(), entrada_nascimento.get().strip(),
            entrada_problema.get().strip())


def ler_busca():
    return entrada_busca.get().strip()


def limpar_formulario():
    for entrada in (entrada_nome, entrada_telefone, entrada_email,
                    entrada_nascimento, entrada_problema):
        entrada.delete(0, "end")


def preencher_formulario(nome, telefone, email, nascimento, problema):
    limpar_formulario()
    entrada_nome.insert(0, nome)
    entrada_telefone.insert(0, telefone)
    entrada_email.insert(0, email)
    entrada_nascimento.insert(0, nascimento)
    entrada_problema.insert(0, problema)


def mostrar_clientes(linhas):
    """Apaga a tabela e escreve de novo. Cada linha é uma tupla na ordem das colunas."""
    for item in tabela.get_children():
        tabela.delete(item)
    for linha in linhas:
        tabela.insert("", "end", values=linha)


def id_selecionado():
    """Devolve o id da linha clicada, ou None se não houver."""
    selecao = tabela.selection()
    if len(selecao) == 0:
        return None
    return int(tabela.item(selecao[0], "values")[0])


def desmarcar_tabela():
    tabela.selection_remove(tabela.selection())