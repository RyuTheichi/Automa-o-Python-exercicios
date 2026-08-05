# 2. Mover e renomear arquivos automaticamente

# Crie um script que:

#     Verifica se existe um arquivo chamado relatorio.txt.

#     Move esse arquivo para uma pasta chamada relatorios_antigos.

#     Durante a movimentação, renomeie o arquivo para relatorio_backup.txt.

import shutil
from pathlib import Path

relatorios = Path('relatorios')
relatorios_antigos = Path('relatorios_antigos')

if not relatorios.exists() or relatorios_antigos.exists():
    relatorios.mkdir(parents=True, exist_ok=True)
    relatorios_antigos.mkdir(parents=True,exist_ok=True)

(relatorios / 'relatorios.txt').touch()
(relatorios / 'relitorio.txt').touch()

for relatorio in relatorios.glob('*relatorio*.txt'):
    shutil.move(relatorio , 'relatorios_antigos/relatorio_backup.txt')