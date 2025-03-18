import json
import os
from typing import TextIO

arq_usu = 'usuarios.json'

def carregar_usu():
    if os.path.exists(arq_usu):
        with open(arq_usu, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def salvar_usu(usuarios):
    with open(arq_usu, 'w', encoding='utf-8') as file:
        file: TextIO
        json.dump(usuarios, file, indent=4)  # Agora está correto!
