from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str=''):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e está emitindo um som.')
        

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acaba de dizer 'QUACK QUACK'")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acaba de dizer 'au au au'.")

class Spitz(Cachorro):
    pass

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acaba de dizer 'RUF RUF RUF'")


class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acaba de dizer 'Miau miau'")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acaba de dizer 'PÓ PÓ PÓ'")
