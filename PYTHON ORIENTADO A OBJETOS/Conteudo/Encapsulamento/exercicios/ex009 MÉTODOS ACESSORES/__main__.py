from rich import print, inspect
from ex009 import Avaliacao

def main():
    av1 = Avaliacao('Alex', 'Matematica')

    av1.set_nota(8.5) ## alterando a nota do aluno, usando o método setter criado   

    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.discilpina}")

    
        

if __name__ == "__main__":
    main()