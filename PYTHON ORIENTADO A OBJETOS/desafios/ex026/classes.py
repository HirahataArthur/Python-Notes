from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto = 0):
        super().__init__()
        self.nome:str = nome 
        self.sal_bruto:float = sal_bruto
        self.salario:float = 0
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def cal_sal(self):
        pass

    def analisar_sal(self):
        analise = f"Nome: [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/])\nSalário Bruto: R${self.sal_bruto:.2f}\nSalário com desconto do INSS: R$[yellow]{self.salario}[/]\nCorresponde a [red]{(self.salario / self.sal_min):.2f} salários minimos[/]."
        analisando = Panel(analise, title= "Análise de salário")
        print(analisando)

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab, sal_bruto = 0):
        super().__init__(nome, sal_bruto)
        self.valor_hora:int = valor_hora
        self.horas_trab:int = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def cal_sal(self):
        taxes = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - taxes
        print(f"Salário calculado com sucesso: R${self.salario}")

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
    
    def cal_sal(self):
        taxes =  self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - taxes
        print(f"Salário calculado com sucesso: R${self.salario}")
    
