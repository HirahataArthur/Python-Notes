from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Controller:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5
    
    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
    
        def liga_desliga(self):
            self.ligado = not self.ligado


    def mostrar_tv(self):

        conteudo = ''
        if self.ligado == False:
            conteudo = f":stop_sign:[red] A TV está desligada.[/]"
        else:
            conteudo = f"CANAL ="
            for canal in range(Controller.canal_min, Controller.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f" [yellow on yellow]{canal}[/]"    
                else : 
                    conteudo += f" {canal}"
            conteudo += f"\nVOLUME = "
            for volume in range(Controller.volume_min, Controller.volume_max +1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else: 
                    conteudo += "[black on white] [/]"
        tv = Panel(conteudo, title = "[ TV ]", width=30)
        print(tv)

    def canal_Mais(self):
        if self.ligado: 
            if self.canal_atual == Controller.canal_max:
                self.canal_atual = Controller.canal_min
            else:
                self.canal_atual += 1
    def canal_Menos(self):
        if self.ligado:
            if self.canal_atual == Controller.canal_min:
                self.canal_atual = Controller.canal_max
            else: 
                self.canal_atual -= 1
    def volume_Mais(self):
        if self.ligado:
            if self.volume_atual != Controller.volume_max:
                self.volume_atual += 1
    def volume_Menos(self):
        if self.ligado:
           if self.volume_atual != Controller.volume_min:
                self.volume_atual -= 1

c = Controller()

while True:
    c.mostrar_tv()
    comando = str(input(f" < CH{c.canal_atual} >   - VOL{c.volume_atual} +  "))

    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.canal_Mais()
        case '<': 
            c.canal_Menos()
        case '-':
            c.volume_Menos()
        case '+':
            c.volume_Mais()
    print("\n" * 10)     




    