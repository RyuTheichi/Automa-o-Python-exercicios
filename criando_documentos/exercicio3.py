from docx import Document

documento = Document("funcionarios.docx")

for table in documento.tables:
    for linha in table.rows:
        dados = [celula.text for celula in linha.cells]
        print(dados)
