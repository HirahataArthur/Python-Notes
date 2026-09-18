from ex031 import Retangulo
from rich import inspect

def main():
    r = Retangulo()

    r.medidas = (3, 2)
    inspect(r, private=True)
    print(r.medidas)


if __name__ == "__main__":
    main()