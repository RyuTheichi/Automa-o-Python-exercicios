# Exercício 2 — Contador de letras

# Crie um arquivo chamado mensagem.txt com um parágrafo de texto que você inventar. Depois, escreva um script que conte e exiba quantas letras existem nesse texto.
frase = input("Digite uma frase")

with open("mensagem.txt", "w+") as msg:
    msg.write(frase)
    msg.seek(0)
    message = msg.read()
    print(len(message))
