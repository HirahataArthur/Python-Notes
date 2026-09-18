from rich.traceback import install
from rich import print


install() ##mostrar erro de forma bonita

def divisao(x, y):
    return x / y

print(f"[bold blue]{divisao(50, 2)}[/]")