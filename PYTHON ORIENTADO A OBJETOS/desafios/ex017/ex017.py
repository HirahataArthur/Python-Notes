from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Product:
    def __init__(self, name, price = None):
        self.name = name
        self.price = price

        print("[blue]Produto cadastrado com sucesso!![/]")

    def __str__(self):
        return f"Product: {self.name}\nPrice: R${self.price:,.2f}"

    def tag(self):
        tag = Panel(
            f"--------{self.name}--------\n-------------------------\n--------R${self.price:,.2f}-------", title="Produto", style="green", width=30, title_align="center")
        return tag

p1 = Product("Iphone 17", 17_000)
print(p1)
print(p1.tag())

p2 = Product("Macbook", 25_000)
print(p2)
print(p2.tag())