# 2️⃣ Leitura de arquivo
# Tente abrir um arquivo chamado relatorio2025.txt e exibir o conteúdo. Trate o erro caso o arquivo não exista.
from pathlib import Path

try:
    relatorio = Path("relatorio.txt")
    open(relatorio)
except FileNotFoundError:
    print("Arquivo nao encontrado")
