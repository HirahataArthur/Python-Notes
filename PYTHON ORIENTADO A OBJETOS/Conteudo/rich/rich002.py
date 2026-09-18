from rich import print
from rich.panel import Panel

caixa = Panel("[white]Este é um painel de exemplo[/]", title="mensagem", style="red", width=25)
print(caixa)