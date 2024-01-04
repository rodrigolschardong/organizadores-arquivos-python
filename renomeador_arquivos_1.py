import os
from tkinter.filedialog import askdirectory

caminho = askdirectory (title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

nome = os.path.basename(caminho)
prefixo = nome [:3] + '-'

for arquivo in lista_arquivos:
    if not arquivo [:4] == prefixo:
        os.rename (f'{caminho}/{arquivo}', f'{caminho}/{prefixo + arquivo}')