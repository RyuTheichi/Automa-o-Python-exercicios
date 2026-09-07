# 👉 Exercício 2 – Mensagens de sistema
# Um log contém mensagens no formato:

#     texto = "[INFO] Processo iniciado em 12:45\n[WARNING] Uso de memória alto às 13:05\n[ERROR] Falha crítica às 13:15"

# Encontre todas as mensagens com o tipo (INFO, WARNING, ERROR) como grupo 1 e o horário como grupo 2.

import re

texto = "[INFO] Processo iniciado em 12:45\n[WARNING] Uso de memória alto às 13:05\n[ERROR] Falha crítica às 13:15"

padrao = r"(\[\w+\]).+ (\d{2}\:\d{2})"

erros = re.findall(padrao, texto)


if erros:
    for erro in erros:
        print(
            f"Foram encontrados os seguintes tipos de erros {erro[0]} no horario {erro[1]}"
        )
