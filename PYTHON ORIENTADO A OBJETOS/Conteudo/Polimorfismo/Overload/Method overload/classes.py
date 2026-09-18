from functools import singledispatchmethod



class Analisador:


    @singledispatchmethod
    def analisar(self, valor):
        print(f'Nao foi possivel analisar o valor {valor}')

    @analisar.register
    def _(self, valor: int):
        print(f"{valor} é um número inteiro.")

    @analisar.register
    def _(self, valor: str):
        print(f"'{valor}' é uma cadeia de caracteres")

    @analisar.register
    def _(self, valor: list|dict|tuple):
        print(f"{valor} é uma coleção de dados")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um número ponto flutuante (Real)")

    

    