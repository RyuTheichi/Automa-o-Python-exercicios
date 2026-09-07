# 1️⃣ Encontre todos os códigos de produto no formato "ABC-1234"
# Texto de exemplo:

#     texto = "Códigos disponíveis: ABC-1234, DEF-5678, GHI-0001, jkl-9999"

import re

texto = "Códigos disponíveis: ABC-1234, DEF-5678, GHI-0001, jkl-9999"

# expressao = r"\w+-\d{4}"

# busca = re.search(expressao, texto)

# if busca:
#     print(busca.group())

expressao = r"\w+-\d{4}"

busca = re.findall(expressao, texto)

if busca:
    print(busca)
