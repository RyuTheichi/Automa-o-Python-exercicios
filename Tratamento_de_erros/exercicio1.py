# 👉 1️⃣ Conversão segura
# Peça ao usuário que informe um número. Converta para inteiro usando try-except e exiba o número convertido ou uma mensagem de erro se a conversão falhar.
# valor = None
# try:
#     valor = int(input("Digite o numero que gostaria de converter:\n"))
# except ValueError as erro:
#     print("Valor invalido!")

# print(valor)

# try:
#     valor = int(input("Digite o numero que gostaria de converter:\n"))
# except ValueError as erro:
#     print("Valor invalido!")
# else:
#     print(valor)

try:
    valor = int(input("Digite o valor numerico a qual gostaria de converter:\n"))
except ValueError as valor:
    print("Valor Invalido!")
print(str(valor))
