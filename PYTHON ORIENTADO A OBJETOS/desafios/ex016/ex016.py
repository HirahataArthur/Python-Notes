from rich import inspect
from rich import print
from rich.traceback import install
install()
from rich.panel import Panel



class Funcionário:
    """
    Definindo uma classe chamada funcionario. 
    Contem atributos de Nome, Setor e Cargo.
    Um método de apresentação.

    """
    def __init__(self, nome, setor, cargo = "Nenhum"): ##Método construtor

        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print("[bold blue]Funcionário cadastrado com sucesso![/]")

    def __str__(self):
        return f"Funcionário: {self.nome} - Setor: {self.setor} - Cargo: {self.cargo}"

    def introduce(self): ##Método de apresentação
        caixa = Panel(
            f"Olá! Meu nome é [green]{self.nome}[/], eu trabalho no setor [yellow]{self.setor}[/] e meu cargo é [bold red]{self.cargo}[/]",
            title=f"Introdução {self.nome}",
            style="blue",
            width=60)
        print(caixa)


f1 = Funcionário("Alex", "Educação", "Professor")
print(f"[bold]{f1}[/]")
f1.introduce()

f2 = Funcionário("Beatriz", "Química", "Perita Criminal")
print(f"[red]{f2}[/]")
f2.introduce()
