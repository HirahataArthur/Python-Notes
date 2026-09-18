from rich import print
from rich.table import Table

table = Table(title="Tabela de preços")

table.add_column("[on blue]Nome[/]")
table.add_column("Preço")
table.add_row("Lapis", "R$3,00")


print(table)
