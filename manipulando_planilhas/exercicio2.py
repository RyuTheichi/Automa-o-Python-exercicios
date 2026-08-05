# 🟢 Exercício 1 – Dados pontuais

# Abra a aba Alunos e imprima os valores exatos das seguintes células:

#     B2

#     D5

#     E10

from openpyxl import load_workbook

wk = load_workbook("alunos.xlsx")
alunos_dados = wk["Alunos"]

print(
    f"{alunos_dados['B2'].value}, {alunos_dados['D5'].value}, {alunos_dados['E10'].value}"
)

# 🟡 Exercício 2 – Leitura de colunas

# Percorra toda a coluna “Nota Final” e exiba somente os alunos com nota acima de 8.0.

for linha in alunos_dados.iter_cols(values_only=True, min_col=4, max_col=4, min_row=2):
    for dado in linha:
        if dado >= 8:
            print("--" * 2)
            print("Nota final")
            print(dado)

# 🔴 Exercício 3 – Relatório geral

# Percorra todos os registros (exceto o cabeçalho) e imprima um relatório no seguinte formato:

#     ALUNO: Maria Souza
#     CURSO: Python
#     IDADE: 29
#     NOTA FINAL: 9.0
#     MATRÍCULA: 15/02/2023

for linha in alunos_dados.iter_rows(values_only=True, min_row=2):
    ALUNO, CURSO, IDADE, NOTA_FINAL, MATRICULA = linha
    for dado in linha:
        print("--" * 10)
        print(f"""NOME:{ALUNO}
CURSO:{CURSO}
IDADE:{IDADE}
NOTA FINAL:{NOTA_FINAL}
MATRICULA:{MATRICULA.strftime("%d/%m/%Y")}""")
