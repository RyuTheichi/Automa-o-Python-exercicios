# 2️⃣ Substitua todas as placas de carro por "PLACA"
# Texto de exemplo:

#     texto = "Os carros estacionados são: KDA-2341, JHU-8877 e MNO-0000"

import re

texto = "Os carros estacionados são: KDA-2341, JHU-8877 e MNO-0000"
padrao = r"\w+-\d{4}"
substituto = re.sub(padrao, "PLACA", texto)
if padrao:
    print(substituto)
