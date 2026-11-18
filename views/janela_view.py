#janela principal e as abas
from tkinter import ttk

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Barbearia Abobrinha")
janela.geometry("1150x640")
janela.minsize(950, 520)

estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure("Treeview", background="#2b2b2b", foreground="#ffffff",
                 fieldbackground="#2b2b2b", rowheight=28, borderwidth=0)
estilo.configure("Treeview.Heading", background="#1f6aa5", foreground="white",
                 relief="flat", font=("Arial", 10, "bold"))
estilo.map("Treeview", background=[("selected", "#1f6aa5")])

titulo = ctk.CTkLabel(janela, text="Barbearia Abobrinha",
                      font=ctk.CTkFont(size=22, weight="bold"))
titulo.pack(padx=20, pady=(16, 0), anchor="w")

abas = ctk.CTkTabview(janela)
abas.pack(padx=12, pady=(4, 12), fill="both", expand=True)
aba_clientes = abas.add("Clientes")         # add() devolve o frame da aba
aba_fila = abas.add("Fila de espera")
aba_servicos = abas.add("Serviços")
