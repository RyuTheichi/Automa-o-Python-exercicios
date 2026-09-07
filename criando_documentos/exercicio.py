# Exercício 1 — Gerar um contrato simples

# Crie um arquivo Word chamado contrato.docx com o seguinte conteúdo:

#     Um título centralizado com o texto "Contrato de Prestação de Serviço".

#     Um parágrafo com o texto "Este contrato tem como objeto a prestação de serviços de desenvolvimento de software."

#     Uma lista com marcadores contendo as obrigações do contratante:

#         Fornecer as informações necessárias

#         Realizar os pagamentos no prazo

#         Disponibilizar os recursos necessários

#     Uma lista numerada contendo as obrigações do contratado:

#         Executar o serviço conforme combinado

#         Cumprir os prazos estabelecidos

#         Comunicar o andamento do trabalho

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

documento = Document()

titulo = documento.add_heading("", level=1)
titulo.add_run("Contrato de Prestação de Serviço").font.size = Pt(16)
titulo.alignement = WD_ALIGN_PARAGRAPH.CENTER
p1 = documento.add_paragraph()
p1.text = "Este contrato tem como objeto a prestação de serviços de desenvolvimento de software."


documento.add_paragraph("Obrigações do contratante:")
documento.add_paragraph("Fornecer as informações necessárias:", style="List Bullet")
documento.add_paragraph("Realizar os pagamentos no prazo", style="List Bullet")
documento.add_paragraph("Disponibilizar os recursos necessários", style="List Bullet")


documento.add_paragraph("Obrigações do contratado:")
documento.add_paragraph("Executar o serviço conforme o combinado", style="List Bullet")
documento.add_paragraph("Cumprir os prazos estabelecidos", style="List Bullet")
documento.add_paragraph("Comunicar o andamento do trabalho", style="List Bullet")

documento.save("contrato.docx")
