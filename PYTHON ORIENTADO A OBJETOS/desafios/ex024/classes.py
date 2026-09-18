from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def __init__(self):
        pass



    def preparar(self):
        print(f"---INICIANDO O PREPARO---\n1. {self.ferver_agua()}\n2. {self.misturar()}\n3. {self.servir()}\n---Bebida pronta---")

    def ferver_agua(self):
        return "Ferver água a 100 graus Celsius."


    ##Métodos abstratos
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def __init__(self):
        super().__init__()
    def misturar(self):
        return "Passando agua pressurizada pelo pó de café moído."
    def servir(self):
        return "Servindo em xicara pequena."


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        return "Megulhando sachê de ervas na agua."

    def servir(self):
        return "Servindo na caneca de porcelana com limão"
    
class LeiteQuente(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        return "Passando vapor pressurizado pelo bico do leite."
    
    def servir(self):
        return "Servindo na caneca grande, já com café."