
from rich import inspect, print
from ex029 import Diario


def main():
    d = Diario('12345')
    d.escrever('uMal ona em maa')
    d.escrever('Sla mais oq escrever')
    d.escrever('sla sla sla')

    try:
        d.ler()
    except Exception as e:
        print(f'[red]Erro: {e}[/red]')
        

if __name__ == "__main__":
    main()