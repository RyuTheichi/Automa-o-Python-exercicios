# 🥇 Exercício — Sorteio de Prêmios em uma Festa

# Você está organizando uma festa e tem 5 prêmios diferentes para sortear entre os convidados.

#     Cada convidado só pode ganhar um único prêmio.

#     Os prêmios também não podem se repetir (obviamente).

#     No final, mostre qual convidado ganhou qual prêmio.

# Use as seguintes listas:

#     convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
#     premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

import random

convidados = ["Ana", "Lucas", "Joao", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

premios_recebidos = random.sample(premios, k=5)

contador = 0

while contador < 5:
    print(f"{convidados[contador]} recebeu {premios_recebidos[contador]}")
    contador += 1
