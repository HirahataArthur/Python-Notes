from rich import print 
from rich.panel import Panel
from rich.traceback import install          
install()


class Barbecue:
    def __init__(self, name, people):
        self.name = name
        self.people = people
        print("[bold blue]Churrasco criado com sucesso![/]")
    
    def analisar(self):
        meat_quantity = self.people * 0.4
        total = meat_quantity * 82.40
        individual_payment = total / self.people
        analise =  Panel(f"Analisando o [green]{self.name}[/] com [bold blue]{self.people} convidados[/]!\nCada convidado vai comer em média 0.4kg de carne e cada kg custa R$82.40\nRecomendo comprar [blue]{meat_quantity:,.1f}kg[/] de carne.\nO custo total será de [red]R${total:,.2f}[/]\nCada pessoa pagará [yellow]R${individual_payment:,.2f}[/] para participar.",
                    title=f"{self.name}",
                    style="bold white",
                    width=80)
        return analise
    

c1 = Barbecue("Churrasco dos amigos", 80)
print(c1.analisar())




        