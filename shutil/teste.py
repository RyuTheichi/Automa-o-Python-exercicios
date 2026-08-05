def somar(a, b):
    return a + b


def saudacao(nome, saudacao="Oi"):
    return f"{saudacao}, {nome}!"


def logger(func, *args, **kwargs):
    print(f"Chamando {func.__name__} com args={args} e kwargs={kwargs}")
    resultado = func(*args, **kwargs)
    print(f"Resultado: {resultado}")
    return resultado


logger(somar, 3, 4)
logger(saudacao, "Ana", saudacao="Olá")
