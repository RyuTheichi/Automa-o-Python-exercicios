def cadastro():
    ano_atual = 2026
    try:
        ano_nascimento = int(input("Digite o ano em que voce nasceu:\n"))
        if ano_nascimento > ano_atual or ano_nascimento < 1900:
            raise ValueError("Ano invalido")
    except ValueError as erro:
        if str(erro) == "Ano invalido":
            print(erro)
        else:
            print("Digite apenas numeros!")

    else:
        print(f"Cadastro realizado! Idade:{ano_atual - ano_nascimento}")
    finally:
        print("Sessao de cadastro encerrada.")


cadastro()
