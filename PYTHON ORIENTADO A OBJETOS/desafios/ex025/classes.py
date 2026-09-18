from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def cal_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50
        self.frete = self.distancia * self.fator
    
    def cal_frete(self):       
        return f"Frete para transporte de moto para a distancia de {self.distancia}km: R${self.frete:.2f}"
    

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20
        self.frete = self.distancia * self.fator

    def cal_frete(self):
        if self.distancia < 49:
            return "Distancia invalida para esta opção de transporte."
        else:  
            return f"Frete para transporte de caminhao para a distancia de {self.distancia}km: R${self.frete:.2f}"

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50
        self.frete = self.distancia * self.fator
    
    def cal_frete(self):
        if self.distancia > 10:
            return "Distancia invalida para este tipo de transporte."
        else:
            return f"Frete para transporte de drone para a distancia {self.distancia}km: R${self.frete:.2f}"
        

class Carro(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.00
        self.frete = self.distancia * self.fator
    
    def cal_frete(self):
        return f"Frete para transporte de carro para a distancia de {self.distancia}km: R${self.frete:.2f}"
    
class Navio(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.30
        self.frete = self.distancia * self.fator
    
    def cal_frete(self):
        if self.distancia < 100:
            return "Distancia invalida para este tipo de transporte."
        else:
            return f"Frete para transporte de navio para a distancia de {self.distancia}km: R${self.frete:.2f}"