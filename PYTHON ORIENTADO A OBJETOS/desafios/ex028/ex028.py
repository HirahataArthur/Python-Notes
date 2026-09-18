

class Termostato:
    def __init__(self):
        self.__temp = 24


    @property
    def temperatura(self):
        return self.__temp

    @temperatura.setter
    def temperatura (self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f'Temperatura de {valor}{chr(176)} é inválido.')
        if valor < 16:
            self.__temp = 16
        elif valor > 30:
            self.__temp = 30
        else: 
            self.__temp = valor

    @property
    def ftemperatura(self):
        return f'{self.__temp}°C'
