# Exercício 1 — Criando um relatório simples

#     Crie um arquivo chamado relatorio.txt que contenha a frase "Estou aprendendo Python!

#     Inclua no final do arquivo a data e hora de criação do arquivo de forma automática

# from datetime import datetime
# from pathlib import Path

# hora = datetime.now().strftime('%d/%m/%Y')
# raiz = Path('')
# (raiz / 'relatorio.txt' ).touch()

# with open('relatorio.txt', 'r+') as file:
#     file.write(hora)
#     file.seek(0)
#     print (file.read())

from datetime import datetime

with open("relatorio.txt", "w+") as relatorio:
    relatorio.write("Estou aprendendo python!\n")
    agora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    relatorio.write(agora)
    relatorio.seek(0)
    print(relatorio.read())
