from datetime import date, datetime


def apenas_digitos(telefone): #remove caracteres especiais
    return "".join(c for c in telefone if c.isdigit())


def validar_telefone(telefone): #da mensagem de erro / none se der certo
    digitos = apenas_digitos(telefone)
    if len(digitos) < 8 or len(digitos) > 15:
        return "Telefone inválido. Digite de 8 a 15 números, com DDD."
    return None


def converter_data(texto): #converte '25/03/1998' em data, dá ValueError se estiver errada
    data = datetime.strptime(texto, "%d/%m/%Y").date()
    if data > date.today():
        raise ValueError("data no futuro")
    return data


def calcular_idade(nascimento):
    hoje = date.today()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade


def tipo_cliente(nascimento):
    if calcular_idade(nascimento) >= 18:
        return "Adulto"
    return "Menor de idade"


def validar_cliente(nome, telefone, email, nascimento, problema): #bloco com exceção
    if nome == "" or len(nome) > 100:
        return "O nome não pode ficar vazio nem passar de 100 letras."
    mensagem = validar_telefone(telefone)
    if mensagem is not None:
        return mensagem
    if "@" not in email or "." not in email or len(email) > 120:
        return "Digite um e-mail válido. Exemplo: nome@exemplo.com"
    try:
        converter_data(nascimento)
    except ValueError:
        return "Data inválida. Use dd/mm/aaaa e não use data no futuro."
    if len(problema) > 150:
        return "O problema com produto químico aceita no máximo 150 letras."
    return None


