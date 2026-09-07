# 💡 Exercício 3 — Apresentação

# Crie um arquivo PDF chamado apresentacao.pdf contendo:

#     Um parágrafo com o texto:
#     Bem-vindo ao curso **Python Automático**! Esperamos que você aproveite a jornada de aprendizado.

#     Um espaçamento de 6 unidades

#     Um segundo parágrafo com o texto:
#     Este curso foi preparado para iniciantes em automação com Python.

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Helvetica", size=10)
pdf.cell(
    0,
    10,
    "Bem-vindo ao curso **Python Automático**! Esperamos que você aproveite a jornada de aprendizado.",
    new_x="LMARGIN",
    new_y="NEXT",
    markdown=True,
)

pdf.ln(6)

pdf.cell(0, 10, "Este curso foi preparado para iniciantes em automação com Python.")

pdf.output("apresentacao.pdf")
