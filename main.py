import sys
from collections import deque

servicos = {
    1: {"nome": "Corte de cabelo", "preco": 30.00},
    2: {"nome": "Barba", "preco": 20.00},
    3: {"nome": "Sombrancelha", "preco": 15.00},
    4: {"nome": "Corte de cabelo + Barba + Sombrancelha", "preco": 55.00},
    5: {"nome": "Corte de cabelo + Barba", "preco": 40.00},
    }

clientes = []
fila = deque()

# ------------------------------------------------------------------
# FUNÇÕES para evitar repeticao
# ------------------------------------------------------------------

def ler_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            return int(valor)
        try:
            return int(valor)
        except ValueError:
            print("Digite apenas números inteiros (ou Enter para cancelar).")




def ler_preco(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        if valor == "":
            return None
        try:
            preco = float(valor)
            if preco <= 0:
                print("O preco precisa ser maior que zero.")
                continue
            return preco
        except ValueError:
            print("Preco inválido. Exemplo: 25.50")



def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Este campo não pode ficar vazio.")


def apenas_digitos (telefone):
    return "".join(c for c in telefone if c.isdigit())



def achar_cliente_por_telefone(telefone):
    telefone = apenas_digitos(telefone)
    for cliente in clientes:
        if cliente["telefone"] == telefone:
            return cliente
    return None

# ------------------------------------------------------------------
# CLIENTES
# ------------------------------------------------------------------

def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = ler_texto("Nome do cliente: ")
    telefone = apenas_digitos(ler_texto("Telefone do cliente: "))

    if len(telefone) < 8:
        print("Telefone inválido.")
        return
    
    if achar_cliente_por_telefone(telefone):
        print("Ja existe um cliente com esse telefone.")
        return

    clientes.append({"nome": nome, "telefone": telefone})
    print(f"Cliente {nome} cadastrado com sucesso!")



def buscar_cliente():
    print("\n--- BUSCAR CLIENTE ---")
    telefone = ler_texto("Telefone do cliente: ")
    cliente = achar_cliente_por_telefone(telefone)

    if cliente:
        print(f"Cliente encontrado: {cliente['nome']} - Telefone: {cliente['telefone']}")
    else:
        print("Cliente não encontrado.")




# ------------------------------------------------------------------
# FILA DE ESPERA
# ------------------------------------------------------------------




def entrar_na_fila():
    print("\n--- Entrar na Fila de espera ---")
    nome = ler_texto("Nome do cliente: ")
    fila.append(nome)
    print(f"Cliente {nome} entrou na fila! Posição na fila: {len(fila)}")



def mostrar_fila():
    print("\n=== Fila de atendimento ===")
    if not fila:
        print("A fila está vazia.")
        return
    for i, cliente in enumerate(fila, start=1):
        print(f"{posicao}º - {nome}")


def atender_proximo():
    print("\n--- Atender próximo ---")
    if not fila:
        print("Ninguem na fila.")
        return
    nome = fila.popleft()
    print(f"Chamando: {nome}!")

# ------------------------------------------------------------------
# SERVIÇOS
# ------------------------------------------------------------------


def listar_servicos():
    print("\n=== Lista de Serviços ===")
    if not servicos:
        print("Nenhum serviço cadastrado.")
        return
    for id_servico, dados in servicos.items():
        print(f"ID: {id_servico} | {dados['nome']} | R$ {dados['preco']:.2f}")


def adicionar_servico():
    print("\n--- Adicionar Serviço ---")
    nome = ler_texto("Nome do serviço: ")
    preco = ler_preco("Preço do serviço: R$ ")
    if preco is None:
        print("Cadastro cancelado.")
        return

    novo_id = max(servicos) + 1 if servicos else 1
    servicos[novo_id] = {"nome": nome, "preco": preco}
    print("Servico adicionado com sucesso!")


def alterar_servicos():
    print("\n--- Alterar Serviço ---")
    if not servicos:
        print("Nenhum serviço cadastrado.")
        return

    listar_servicos()
    id_servico = ler_inteiro("ID do serviço a alterar (Enter cancela): ")
    if id_servico is None:
        return
    if id_servico not in servicos:
        print("Servico não encontrado.")
        return

    atual = servicos[id_servico]
    print("Deixe em branco para manter o valor atual.")


    novo_nome = input(f"Novo nome [{atual['nome']}]: ").strip()
    if novo_nome:
        atual["nome"] = novo_nome


    novo_preco = ler_preco(f"Novo preço [{atual['preco']:.2f}]: R$ ")
    if novo_preco is not None:
        atual["preco"] = novo_preco

        print("Servico alterado com sucesso!")



def excluir_servico():
    print("\n--- Excluir Serviço ---")
    if not servicos:
        print("Nenhum serviço cadastrado.")
        return

    listar_servicos()
    id_servico = ler_inteiro("ID do serviço a excluir (Enter cancela): ")
    if id_servico is None:
        return
    if id_servico not in servicos:
        print("Servico não encontrado.")
        return

    nome = servicos[id_servico]["nome"]
    confirmacao = input(f"Excluir '{nome}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        del servicos[id_servico]
        print(f"Servico '{nome}' excluido com sucesso!")
    else:
        print("Exclusão cancelada.")


# ------------------------------------------------------------------
# SAIR
# ------------------------------------------------------------------


def sair_sistema():
    print("Encerrando o sistema da Barbearia Abobrinha. Até logo!")
    sys.exit()



# ------------------------------------------------------------------
# MENU
# ------------------------------------------------------------------

OPCOES = {
    "1": ("Cadastrar cliente", cadastrar_cliente),
    "2": ("Buscar cliente (telefone)", buscar_cliente),
    "3": ("Mostrar fila", mostrar_fila),
    "4": ("Entrar na fila de espera", entrar_na_fila),
    "5": ("Atender próximo da fila", atender_proximo),
    "6": ("Adicionar serviço", adicionar_servico),
    "7": ("Alterar serviço", alterar_servicos),
    "8": ("Listar serviços", listar_servicos),
    "9": ("Excluir serviço", excluir_servico),
    "0": ("Sair", sair_sistema),
}

def menu():
    while True:
        print("\n======================================")
        print(" Bem-vindo à Barbearia Abobrinha!")
        print("======================================")
        for tecla, (descricao, _) in OPCOES.items():
            print(f"{tecla}. {descricao}")
        print("======================================")

        opcao = input("Escolha uma opção: ").strip()


        if opcao in OPCOES:
            OPCOES[opcao][1]()
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    menu()