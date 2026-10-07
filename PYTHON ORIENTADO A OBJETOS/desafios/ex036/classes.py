from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:int|float = 0):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor < 0:
            raise ValueError("O valor do pagamento não pode ser negativo.")
        self._valor = valor

    
    @property
    def fvalor(self):
        return f"R${self._valor:,.2f}"

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def __init__(self, valor = 0):
        super().__init__(valor)

    def pagar(self):
        try:
            ##Codigo para efetuar o pagamento via boleto . . .
            return f"Valor de {self.fvalor} pago via {self.__class__.__name__}"
        except ValueError as e:
            return f"Erro ao processar pagamento: {e}"


class Cartao(Pagamento):
    def pagar(self):
        try:
            ##Codigo para efetuar o pagamento via cartao . . . 
            return f"Valor de {self.fvalor} pago via {self.__class__.__name__}"
        except ValueError as e:
            return f"Erro ao processar pagamento: {e}"


class Pix(Pagamento):
    def pagar(self):
        try:
            ##Codigo para efetuar o pagamento via pix . . .
            return f"Valor de {self.fvalor} pago via {self.__class__.__name__}"
        except ValueError as e:
            return f"Erro ao processar pagamento: {e}"


#duck typing

def finalizar_compra(forma, valor):
    try:
        if valor < 0:
            print("O valor do pagamento não pode ser negativo.")
        else:
            a = forma(valor)
            print(a.pagar())
    except:
        print("Nao deu sla kkkk")



