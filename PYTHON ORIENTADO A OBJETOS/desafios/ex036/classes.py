from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:int|float = 0):
        self._valor = valor
        self.fvalor = f"R${valor:,.2f}"


    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def __init__(self, valor = 0):
        super().__init__(valor)

    def pagar(self):
        return f"Valor de {self.fvalor} pago via {self.__class__.__name__}"


class Cartao(Pagamento):
    def pagar(self):
        return f"Valor de {self.fvalor} pago via {self.__class__.__name__}"


class Pix(Pagamento):
    def pagar(self):
        return f"Valor de {self.fvalor} pago via {self.__class__.__name__}"


#duck typing

def finalizar_compra(forma, valor):
    try:
        a = forma(valor)
        print(a.pagar())
    except:
        print("Nao deu sla kkkk")



