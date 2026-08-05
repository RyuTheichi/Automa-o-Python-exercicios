# 1. Cópia simples com estrutura

# Crie um script que:

#     Crie uma pasta imagens.

#     Coloque 2 arquivos fictícios .png dentro dela

#     Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup.

import shutil
from pathlib import Path

imagens = Path('imagens')
backup = Path('backup')
if not imagens.exists():
    imagens.mkdir(parents=True, exist_ok=True)
    print (f'Pasta {imagens} criada com sucesso ')
if not backup.exists():
    backup.mkdir(parents=True, exist_ok=True)
(imagens / 'img.png').touch() 
(imagens / 'img2.png').touch()


for arquivo in imagens.glob('*.png'):
    shutil.copy(arquivo ,'backup')

