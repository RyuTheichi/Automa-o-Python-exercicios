# Exercício 1 – Cadastro simples

# Crie um arquivo chamado cadastro.xlsx com uma aba chamada Pessoas.
# Adicione os seguintes dados nas células manualmente (com planilha["A1"] = ...):

#     | Nome     | Cidade         |
#     |----------|----------------|
#     | João     | Recife         |
#     | Marina   | São Paulo      |
#     | Otávio   | Belo Horizonte |

# E salve o arquivo

from openpyxl import Workbook

wk = Workbook()
informacao_pessoas = wk.active

informacao_pessoas.title = "Informacoes dos usuarios"
informacao_pessoas["A1"] = "Nome"
informacao_pessoas["A2"] = "Joao"
informacao_pessoas["A3"] = "Marina"
informacao_pessoas["A4"] = "Otavio"

informacao_pessoas["B1"] = "Cidade"
informacao_pessoas["B2"] = "Recife"
informacao_pessoas["B3"] = "Sao Paulo"
informacao_pessoas["B4"] = "Belo Horizonte"

# Exercício 2 – Adicionando dados com append

# No mesmo arquivo cadastro.xlsx, adicione mais duas pessoas na aba Pessoas utilizando o método append():

#     Letícia, Porto Alegre

#     Gustavo, Salvador

informacao_pessoas.append(["Leticia", "Porto Alegre"])
informacao_pessoas.append(["Gustavo", "Salvador"])

# Exercício 3 – Multiplas abas e estrutura de planilha

#     Crie uma nova aba chamada Visitas.

#     Escreva a estrutura da tabela:

#     | Data       | Visitantes |
#     |------------|------------|
#     | 01/01/2025 | 134        |
#     | 02/01/2025 | 156        |

#     Na aba Visitas, sobrescreva o número de visitantes do dia 01/01/2025 para 142

wk.create_sheet("Visitas")

planilha_visitas = wk["Visitas"]

planilha_visitas.append(["Data", "Visitantes"])
planilha_visitas.append(["01/01/2025", 134])
planilha_visitas.append(["02/01/2025", 156])
planilha_visitas["B2"] = 142

wk.save("cadastro.xlsx")
