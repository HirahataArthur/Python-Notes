from classes import *


def main():
    a = PDF('Epstein Files', 2_000_000)
   
    b = DOC('Redação enem', 2_400_000)


    abrir_arquivo(a)
    abrir_arquivo(b)
    print(a.nomec)


if __name__ == "__main__":
    main()