# Exercício prático: Análise de um relatório PDF de vendas

# Descrição do PDF:

# Abra o pdf vendas.pdf
# É um relatório fictício com 5 páginas, cada página contém o nome da loja, a data do relatório e a lista de produtos vendidos com suas quantidades. Alguns produtos aparecem em várias páginas. As datas estão no formato dd/mm/aaaa.

# Exemplo de texto dentro de uma página:

#     Relatório de Vendas - Loja Alpha
#     Data: 01/07/2025

#     Produtos vendidos:
#     Teclado: 10 unidades
#     Mouse: 15 unidades
#     Monitor: 5 unidades
#     Impressora: 2 unidades

# Etapas do exercício

#     Abrir o arquivo e imprimir o número total de páginas.✅

#     Juntar o texto de todas as páginas em uma string única.✅

#     Criar uma função que receba o texto completo e retorne uma lista com todas as datas encontradas no relatório, no formato dd/mm/aaaa.✅

#     Criar uma função que, dada uma lista de produtos (exemplo: ["Mouse", "Monitor"]) e o texto completo, retorne a soma total de unidades vendidas para cada produto, considerando todas as páginas.✅

#         Exemplo de saída:

#             Mouse: 72 unidades
#             Monitor: 31 unidades

#     Gerar um arquivo de texto resumo_vendas.txt contendo um relatório simples, listando os produtos com suas quantidades totais vendidas e as datas de relatório encontradas.
import re
from pypdf import PdfReader
from datetime import datetime

hora_atual = datetime.now().strftime("%d/%m/%Y")


def soma_produtos(arquivo):
    padrao = r"(\w+):\s*(\d+)"
    texto = arquivo
    search = re.findall(padrao, texto)
    lista_produtos = {"Teclado": 0, "Mouse": 0, "Monitor": 0, "Impressora": 0}
    for produtos, quantidades in search:
        if produtos in lista_produtos:
            lista_produtos[produtos] += int(quantidades)
    return lista_produtos


def data(arquivo):
    padrao = r"\d{2}/\d{2}/\d{4}"
    texto = arquivo
    data_search = re.findall(padrao, texto)
    return data_search


with open("vendas.pdf", "rb") as arquivo:
    reader = PdfReader(arquivo)
    print(f"O relatorio de vendas possui {len(reader.pages)} paginas\n")
    todo_texto = ""
    for pagina in reader.pages:
        todo_texto += pagina.extract_text()
    datas_encontradas = data(todo_texto)
    dias = ""

    for dia in datas_encontradas:
        dias += dia
        dias += " | "
    print(f"Relatorio de vendas dos dia {dias}")
    total = soma_produtos(todo_texto)
    print("Total de vendas de produtos:")
    for produto in total:
        print(produto, total[produto])

with open("resumo.txt", "w") as resumo:
    design = "====" * 15
    resumo.write(
        f"{design}\nResumo do relatorio de vendas criado no dia {hora_atual}.\n{design}\n"
    )
    resumo.write(
        f"Este e um resumo com o a soma total das vendas dos dias {dias}\n\nTotal de paginas resumidas:{len(reader.pages)}\nTotal de produtos vendidos:\n"
    )
    for produto in total:
        resumo.write(f"{produto} {total[produto]}\n")
