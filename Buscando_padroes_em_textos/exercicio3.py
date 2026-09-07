#  Encontre todos os usuários no formato "@nome_usuario" em um comentário
# Texto de exemplo:

#     texto = "Obrigado @joaopereira e @maria_silva pela ajuda! Também cito @123julio e @_admin"

import re

texto = (
    "Obrigado @joaopereira e @maria_silva pela ajuda! Também cito @123julio e @_admin"
)

padrao = r"\@\w+\_\w+"
busca = re.findall(padrao, texto)
if busca:
    print(busca)
