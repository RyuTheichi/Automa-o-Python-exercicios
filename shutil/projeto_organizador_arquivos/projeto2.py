# Enunciado do projeto
# 📁 Projeto: Organizador de Arquivos por Extensão
# 🎯 Objetivo

# Criar um programa em Python capaz de organizar automaticamente os arquivos de uma pasta, movendo-os para subpastas com base em suas extensões (como .pdf, .png, .txt, etc.). O programa também deve registrar cada movimentação feita em um arquivo de log.
# 📌 Requisitos

# Seu programa deve:

#     Percorrer todos os arquivos de uma pasta chamada organizador. (Arquivo anexado)

#     Identificar a extensão de cada arquivo (exemplo: .pdf, .jpg, .py, etc.).

#     Criar subpastas com os nomes das extensões (caso ainda não existam).

#     Mover os arquivos para as subpastas correspondentes.

#     Registrar todas as ações feitas em um arquivo registro.log, com data, hora, nome do arquivo e destino final.

#     Ao final da execução, exibir no terminal um resumo com:

#         Quantos arquivos foram organizados

#         Quais extensões foram encontradas


from datetime import datetime
from pathlib import Path
import shutil

agora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
arquivos_src = Path("organizador/organizador")
arquivos_organizados = Path("arquivos_organizados")
qntd_arqv = 0
tipo_arqv = set()

for arquivo in arquivos_src.iterdir():
    qntd_arqv += 1
    extensao = arquivo.suffix[1:]
    tipo_arqv.add(extensao)
    subpasta = arquivos_organizados / extensao
    if not subpasta.exists():
        subpasta.mkdir(exist_ok=True, parents=True)
    shutil.copy(arquivo, subpasta / arquivo)
    with open("log.txt", "a") as logger:
        logger.write(f"{agora} {arquivo.name} foi movido para o diretorio {subpasta}\n")
print(f"Foram movidos {qntd_arqv} do tipo {tipo_arqv}")
