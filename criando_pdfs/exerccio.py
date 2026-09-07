# 💡 Exercício 1 — Relatório de vendas

# Crie um arquivo PDF chamado relatorio.pdf contendo:

#     Um título centralizado: Relatório de Vendas — Junho 2025

#     Um primeiro parágrafo com o texto:
#     As vendas de junho apresentaram um crescimento significativo em relação ao mês anterior, impulsionadas por campanhas promocionais e novos lançamentos.

#     Um espaçamento de 8 unidades entre os parágrafos

#     Um segundo parágrafo com o texto:
#     A previsão para o próximo mês é de continuidade do crescimento, especialmente no setor de tecnologia.

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Helvetica", size=16)
pdf.cell(0, 10, text="Relatorio de Vendas - Junho 2025", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("Helvetica", size=10)
pdf.multi_cell(
    0,
    10,
    text="As vendas de junho apresentaram um crescimento significativo em relação ao mês anterior, impulsionadas por campanhas promocionais e novos lançamentos.",
    new_x="LMARGIN",
    new_y="NEXT",
)

pdf.ln(8)

pdf.multi_cell(
    0,
    10,
    text="A previsão para o próximo mês é de continuidade do crescimento, especialmente no setor de tecnologia.",
    new_x="LMARGIN",
)

pdf.output("relatorio.pdf")
