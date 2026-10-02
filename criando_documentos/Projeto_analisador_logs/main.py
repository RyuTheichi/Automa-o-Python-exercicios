# Projeto: Analisador Automático de Logs com Relatório Word
# Objetivo

# Desenvolver um sistema em Python que leia, analise e gere um relatório formatado em Word a partir de arquivos de log de servidor. O projeto deve extrair informações relevantes usando expressões regulares (regex) e apresentar os dados em um documento organizado e fácil de entender.
# Descrição

# Você receberá um arquivo de log no formato texto contendo registros variados, com data, hora, nível do log (INFO, ERROR, WARNING, DEBUG) e mensagens diversas. Seu programa deverá:

#     Ler o arquivo de log completo.

#     Extrair, usando expressões regulares, os seguintes dados de cada linha:

#         Data e hora (exemplo: 2025-07-01 15:24:01)

#         Tipo do log (INFO, ERROR, WARNING, DEBUG)

#         Mensagem do log

#     Gerar um relatório em documento Word (.docx) contendo:

#         Um título claro e descritivo (ex: "Relatório de Análise de Logs").

#         Um parágrafo resumo com o total de ocorrências de cada tipo de log.

#         Uma lista detalhada com todas as mensagens de erro.

#         Uma tabela que mostra a quantidade de registros por dia, divididos por nível de log.

# Requisitos Técnicos

#     Utilizar expressões regulares para extrair informações do texto.

#     Trabalhar com leitura de arquivos texto.

#     Utilizar a biblioteca python-docx para gerar o relatório Word.

#     Aplicar conceitos de agrupamento, contagem e formatação em tabelas no Word.
# Dicas

#     Teste suas expressões regulares com exemplos reais antes de aplicar no arquivo completo.

#     Utilize dicionários para armazenar contagens por tipo e por data.

#     Salve o documento com um nome que contenha a data da geração do relatório, por exemplo: 
from docx import Document
import re
from datetime import datetime

def extrair_log(log):
    lista = []
    padrao = (r'(\d{4}-\d{2}-\d{2})\s*(\d{2}:\d{2}:\d{2})\s*(\w+)\s*(.*)')
    resultados = re.findall(padrao,log)
    for resultado in resultados:
        lista.append({
            'data':resultado[0],
            'hora':resultado[1],
            'tipo':resultado[2],
            'msg':resultado[3]
        })
    return lista

def analisador_log():
    lista_qntd = {}
    with open ('logs.txt','r',encoding='utf-8') as log:
        log_completo = extrair_log(log.read())
        documento = Document()
        documento.add_heading('Relatório de Análise de Logs', 1)
        for resultado in log_completo:
            if resultado['tipo'] in lista_qntd:
                lista_qntd[resultado['tipo']] += 1
            else:
                lista_qntd[resultado['tipo']] = 1
        documento.add_paragraph(f'A quantidade de incidentes dentro deste relatório foram:')
        for tipo , qntd in lista_qntd.items():
            documento.add_paragraph(f'{tipo}: {qntd}', style= 'List Bullet')
        
        documento.add_paragraph('Lista de mensagens de erro:')
        for erro in log_completo:
            if erro == 'ERROR':
                documento.add_paragraph(f'{erro['data']} {erro['hora']}: {erro["msg"]}', style='List Bullet')
        
        documento.add_page_break()

        qntd_dia = {}
        for log in log_completo:
            if log['data'] not in qntd_dia:
                qntd_dia[log['data']] = {}
            if log ['tipo'] not in qntd_dia[log['data']]:
                qntd_dia[log['data']][log['tipo']] = 0
            qntd_dia[log['data']][log['tipo']] += 1

        tabela = documento.add_table(0,5)
        tabela.style ='Light Shading Accent 1'
        cabecalho = tabela.add_row().cells
        cabecalho[0].text = 'Data'
        cabecalho[1].text = 'INFO'
        cabecalho[2].text = 'ERROR'
        cabecalho[3].text = 'WARNING'
        cabecalho[4].text = 'DEBUG'

        for dado in sorted(qntd_dia):
            linha = tabela.add_row()
            linha.cells[0].text = dado
            linha.cells[1].text = str(qntd_dia[dado].get('INFO',0))
            linha.cells[3].text = str(qntd_dia[dado].get('ERROR',0))
            linha.cells[4].text = str(qntd_dia[dado].get('WARNING',0))
            linha.cells[5].text = str(qntd_dia[dado].get('DEBUG', 0))
        data_geracao = datetime.now().strftime('%d-%m-%Y')
        documento.save(f'Relatorio_{data_geracao}.docx')


analisador_log()