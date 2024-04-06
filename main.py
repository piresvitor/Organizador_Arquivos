import os 
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
lista_arquivos.sort()

locais = {
    "Imagens":{".png", ".jpg", ".jpeg", ".webp"},
    "Planilhas":{".csv", ".xlsx"},
    "Videos":{".mp4", ".mkv"},
    "Pdf":{".pdf"},
    "XML":{".xml"},
    "Textos":{".doc", ".txt",".docx"}
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
