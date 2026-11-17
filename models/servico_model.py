def converter_preco(texto): #converte '25,50' em 25.5, dá ValueError se estiver errada
    preco = float(texto.replace(",", "."))
    if not 0 < preco <= 999999.99:
        raise ValueError("preço fora do limite")
    return round(preco, 2)


def texto_preco(preco): #coloca vírgula e duas casas decimais
    return f"{preco:.2f}".replace(".", ",")


def validar_servico(nome, preco): #bloco com exceção / none se der certo
    if nome == "" or len(nome) > 100:
        return "O nome não pode ficar vazio nem passar de 100 letras."
    try:
        converter_preco(preco)
    except ValueError:
        return "Preço inválido. Use um valor maior que zero. Exemplo: 25,50"
    return None

