import PyPDF2
import os
from tkinter.filedialog import askdirectory

merger = PyPDF2.PdfMerger()

caminho = askdirectory (title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
lista_arquivos.sort()

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'{caminho}\{arquivo}')
    
merger.write(f"{caminho}\PDF Único.pdf")