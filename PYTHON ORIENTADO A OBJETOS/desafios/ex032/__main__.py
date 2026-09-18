from ex032 import ContaBancaria
from rich import inspect

def main():

    cc = ContaBancaria(1, 'Alex', 1000.00, 'example_key')
    inspect(cc, private=True)
    cc.nome = 'Alex Example'
    inspect(cc, private=True, methods=True)

if __name__ == "__main__":
    main()