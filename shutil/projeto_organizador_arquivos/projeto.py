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

from pathlib import Path
from datetime import datetime
import shutil

agora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
arq_qntd = 0
tipo_arq = set()

organizador = Path("projeto_organizador_arquivos/organizador/organizador")
arquivos_organizados = Path("projeto_organizador_arquivos/arquivos_organizados")
log_file = Path("projeto_organizador_arquivos/log.txt")


for arquivo in organizador.iterdir():
    arq_qntd += 1
    extensao = arquivo.suffix[1:]
    tipo_arq.add(extensao)
    subpasta = arquivos_organizados / extensao
    if not subpasta.exists():
        subpasta.mkdir(exist_ok=True, parents=True)
    shutil.copy(arquivo, subpasta / arquivo.name)
    with open(log_file, "a") as logger:
        logger.write(
            f"{agora} O arquivo {arquivo.name} foi movido para a pasta {subpasta}\n"
        )
print(f"Foram organizados {arq_qntd} arquivos com as extensoes do tipo {tipo_arq}")
