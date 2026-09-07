#  Exercício 2 — Cartaz

# Crie um arquivo PDF chamado cartaz.pdf contendo:

#     Uma imagem (anexada nos recursos) centralizada com largura de 50 mm

#     Um texto abaixo da imagem: Evento Python 2025 — Inscreva-se já!

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("python_banner.png", w=50, x="CENTER")

pdf.set_font("Helvetica", size=10)
pdf.cell(0, 10, "Evento Python 2025 - Inscreva-se já!", align="C")

pdf.output("cartaz.pdf")
