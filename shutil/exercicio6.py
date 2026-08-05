# Exercício 3 — Filtrando logs por palavra-chave

# Baixe o arquivo logs.txt anexado, e escreva um programa que:

#     Leia todas as linhas do arquivo

#     Peça ao usuário uma palavra-chave (como ERROR, INFO, WARNING, etc...)

#     Mostre apenas as linhas que contenham essa palavra-chave.


with open("acesso.log", "r", encoding="utf-8") as log:
    palavra_chave = input(
        "Digite a palavra que gostaria de encontrar:(ERROR || INFO || WARNING)\n"
    ).upper()
    for linha in log:
        if palavra_chave in linha:
            print(linha)
