# 3. Automatizando extração de arquivos

# Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:

#     Crie uma pasta chamada extraido/.

#     Extraia o conteúdo do .zip dentro da pasta criada.

#     Ao final, liste todos os arquivos extraídos.

import shutil
from pathlib import Path

extraido = Path('extraido')

shutil.unpack_archive('arquivos_secretos.zip','extraido', 'zip')

for arquivo in extraido.iterdir():
    print(f'{arquivo}')