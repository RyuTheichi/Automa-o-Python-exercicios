# 👉 3️⃣ Lista e índice
# Dada a lista ["Python", "Excel", "API"], tente acessar um índice informado pelo usuário. Trate o erro se o índice não existir e mostre uma mensagem amigável.

lista = ["Python", "Excel", "API"]
try:
    indice = int(input("Digite o indice que gostaria de acessar:\n"))
    print(f"{lista[indice]}")
except IndexError:
    print("Indice inexistente, tente novamente")
except ValueError:
    print("Dado invalido , utilize apenas numeros")
