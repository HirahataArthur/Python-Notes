from ex033 import Aluno
from rich import inspect


def main():
    a1 = Aluno('Alex', 1995, 'ADS')
    inspect(a1, methods=True, private=True)
    a1.nascimento = 1995
    a1.add_curso('JPG')
    a1.add_curso('ada')
    a1.curso = 'JPG'
    inspect(a1, methods=True, private=True)

if __name__ == "__main__":
    main()