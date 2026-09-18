from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel



class Mensagem:
    def __init__(self, mensagem:str = '', tipo = None, icone = None):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    @property
    def mensagem(self):
        return self._mensagem

    def mostrar(self):
        panel = Panel(self.mensagem, title= ":speech_balloon: AVISO :speech_balloon:", width=50)
        print(panel)


class Alerta(Mensagem):
    def __init__(self, mensagem = '', tipo=None, icone=None):
        super().__init__(mensagem, tipo, icone)

    def mostrar(self):
        panel = Panel(f"[bold black]{self.mensagem}[/]", width=50, style="on yellow", border_style="bold black", title=":warning: ALERTA :warning:" )
        print(panel)


class Erro(Mensagem):
    def __init__(self, mensagem = '', tipo=None, icone=None):
        super().__init__(mensagem, tipo, icone)

    def mostrar(self):
        panel = Panel(f"[bold yellow]{self.mensagem}[/]", width=50, style="on red", border_style="bold yellow", title=":no_entry_sign: ERRO :no_entry_sign:" )
        print(panel)
        

