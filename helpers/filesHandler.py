import shutil
import os
# from filecmp import cmpfiles, dircmp
# É possível ler os arquivos de um diretório e colocálos em uma lista:


# def compareFiles(a, b):
#    return dircmp(a, b)


def filesList(destination):
    try:
        return os.listdir(destination)
    except Exception:
        print("Directory not found.")


# É possível mover arquivos através de uma função:
def copyToDir(base, destination):
    for file in filesList(base):
        shutil.copy(f'{base}/{file}', destination)

# É possível veririficar se o arquivo já existe no sistema de arquivos
# , se existir, é possível pedir uma confirmação para tal ação.