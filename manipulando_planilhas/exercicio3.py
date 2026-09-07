# Enunciado de Exercício: Estilizando planilhas com openpyxl
# 📝 Exercício – Diário de Leituras

# Você deve criar uma planilha chamada diario_leituras.xlsx para registrar os livros que você está lendo no mês.
# Estrutura esperada

#     A1:D1 → título mesclado: "Diário de Leituras – Agosto 2025".

#     A2:D2 → cabeçalho com colunas: Livro, Autor, Data de Início, Progresso (%).

#     Linhas seguintes → registros fictícios de livros.

# Requisitos de estilização

#     Título (linha 1):

#         Mesclar células A1:D1.

#         Centralizar o texto.

#         Fundo azul escuro (1F497D).

#         Fonte branca, negrito, tamanho 14.

#     Cabeçalho (linha 2):

#         Fonte branca em negrito.

#         Fundo cinza escuro (4f4f4f).

#         Bordas finas.

#     Linhas dos livros:

#         Alternar cores de fundo (efeito zebrado: uma linha branca, outra cinza claro).

#         Coluna "Livro" e "Autor" alinhadas à esquerda.

#         Coluna "Data de Início" alinhada ao centro, formatada como DD/MM/YYYY.

#         Coluna "Progresso (%)" alinhada à direita, formatada como número percentual com uma casa decimal (0.0%).

#     Bordas finas em todas as células da tabela.


from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from datetime import datetime

wb = Workbook()
planilha = wb.active
planilha.title = "Livros"
fino = Side(style="thin")
hora = datetime.now().strftime("%Y/%d/%m")

# 1. Título
planilha.merge_cells("A1:D1")
planilha["A1"] = "Diario de Leituras - Agosto 2026"
planilha["A1"].alignment = Alignment(horizontal="center")
planilha["A1"].fill = PatternFill(fgColor="1F497D", fill_type="solid")
planilha["A1"].font = Font(bold=True, size=14, color="FFFFFF")

# 2. Cabeçalho
planilha.append(["Livro", "Autor", "Data de inicio", "Progresso"])
for celula in planilha[2]:
    celula.font = Font(bold=True, color="FFFFFF")
    celula.fill = PatternFill(fgColor="4f4f4f", fill_type="solid")

# 3. Inserção de Dados
planilha.append(["Os Irmaos Karamazov", "Fiodor Dostoieviski", hora, 1])
planilha.append(
    ["Rapido e Lento, duas formas de se pensar", "Daniel Kahneman", hora, 0.6]
)
planilha.append(["Introducao a Ciencia da Economia", "FIESP", hora, 0.1])

# 4. PRIMEIRO: Aplica as Bordas e Cores Alternadas (Zebra)
for linha in planilha.iter_rows():
    for celula in linha:
        celula.border = Border(fino, fino, fino, fino)
        if celula.row <= 2:
            continue
        if celula.row % 2 == 0:
            celula.fill = PatternFill(fgColor="FFFFFF", fill_type="solid")
        else:
            celula.fill = PatternFill(fgColor="D3D3D3", fill_type="solid")

# 5. POR ÚLTIMO: Aplica a formatação de porcentagem (Garante que não será sobrescrita)
for celula in planilha["D"][2:]:
    celula.number_format = "0%"

wb.save("livros.xlsx")
