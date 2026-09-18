from rich import print
from rich.traceback import install
install()

class Pen:
    def __init__(self, name, state = "Tampado"):
        self.name = name
        self.state = state


    def destampar(self):
        self.state = "Destampado"
        print("Caneta destampada")
    
    def tampar(self):
        self.state = "Tampado"
        print("Caneta Tampada")


    def write(self, text = ""):
        self.name = self.name.strip().upper()
        if self.state != "Destampado":
            return "A caneta está tampada"
        else:
            cores = {
                "AZUL": "blue",
                "VERDE": "green",
                "VERMELHO": "red"
            }   
            if self.name in cores:
                return f"[{cores[self.name]}]{text}[/]"
            else:
                return "Opção inválida"
            
    def line_break(self, number):
        for i in range(number):
            print()
    
    
        
c1 = Pen("VERDE")
c2 = Pen("vermelho")
c3 = Pen("AZul")


print(c1.write("Sla"))
c1.destampar()
print(c1.write("OLA MUNDO"))
c1.tampar()
print(c1.write("Ola mundo"))