from rich import print, inspect
from ex010 import Avaliacao

def main():
    av1 = Avaliacao('Alex', 'Matematica')

    av1.nota = 5 ## alterando a nota do aluno, usando o setter criado

    print(f"{av1.nome} tirou {av1.nota} em {av1.discilpina}")
    inspect(av1, private=True)
        

if __name__ == "__main__":
    main()