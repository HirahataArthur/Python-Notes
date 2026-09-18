

class Retangulo:
    def __init__(self, altura = 1, base = 1):
        self._altura = altura
        self._base = base
        self._area = None


    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
            self._area = self._altura * self._base
        else:
            raise ValueError('Valor inválido para altura')


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor > 0:
            self._base = valor
            self._area = self._altura * self._base
            
        else: 
            raise ValueError('Valor inválido para base')

    @property
    def area(self):
        return self._area

    @property
    def medidas(self):
        return f"Altura = {self._altura} \nBase = {self._base} \nArea = {self._area}"

    @medidas.setter 
    def medidas(self, valor):
        if isinstance(valor, (tuple, list)) and len(valor) == 2:
            x, y = valor
            if x > 0 and y > 0:
                    self._base = y      # base
                    self._altura = x    # altura
                    self._area = self._altura * self._base
            else:
                raise ValueError('Valores devem ser maiores que 0')
        else:
            raise ValueError('medidas deve ser uma tupla ou lista com 2 valores')