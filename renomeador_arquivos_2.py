import os
from tkinter.filedialog import askdirectory

pasta_base = askdirectory (title="Selecione a pasta base do projeto")
pasta_arquivos = askdirectory(title="Selecione a pasta onde estão os arquivos a serem renomeados")

lista_arquivos = os.listdir(pasta_arquivos)

nome = os.path.basename(pasta_base)
prefixo = nome [:3] + '-'

for arquivo in lista_arquivos:
    print(arquivo)
    if not arquivo [:4] == prefixo:
        os.rename (f'{pasta_arquivos}/{arquivo}', f'{pasta_arquivos}/{prefixo + arquivo}')