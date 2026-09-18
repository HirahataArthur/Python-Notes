from abc import ABC, abstractmethod


class Mae(ABC):
    def __init__(self, nome:str="Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com doce de leite.')

    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA com óleo de soja.')


class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite ninho com nutella')


class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA na airfrier')
