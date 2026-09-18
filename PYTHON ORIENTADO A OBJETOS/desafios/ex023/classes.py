from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lados):
        self.lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado, lados = 4):
        super().__init__(lados)
        self.lados = lados
        self.lado = lado
    
    def perimetro(self):
        perimetroQ = self.lado *4
        return perimetroQ
    
    def area(self):
        areaQ = self.lado * self.lado
        return areaQ
    
class Circulo(Poligono):
    def __init__(self, raio, lados= 0):
        super().__init__(lados)
        self.raio = raio

    def perimetro(self):
        perimetroC = 2 * 3.14 * self.raio
        return perimetroC
    
    def area(self):
        areaC = 3.14 * (self.raio * self.raio)
        return areaC
    

    


