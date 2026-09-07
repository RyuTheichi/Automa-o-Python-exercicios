# 👉 Exercício 1
# Dado o texto:

#     texto = "Veículos: CAR-2023, MOTO-2018, BUS-2015"

# Crie uma expressão regular que capture:

#     O tipo do veículo (CAR, MOTO, BUS) como primeiro grupo

#     O ano como segundo grupo

import re

texto = "Veículos: CAR-2023, MOTO-2018, BUS-2015"

padrao = r"(\w+)-(\d{4})"
resultados = re.findall(padrao, texto)

if resultados:
    for resultado in resultados:
        print(f"Foi encontrado o automovel {resultado[0]} com o ano {resultado[1]}")
