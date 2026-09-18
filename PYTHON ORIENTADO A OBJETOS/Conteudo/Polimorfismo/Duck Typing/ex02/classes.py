

class Numero:
    def __init__(self, valor: int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2


    def __str__(self):
        return f"Tenho o número {self.valor} dentro"

class Texto:
    def __init__(self, txt: str = ''):
        self.texto = txt

    def __str__(self):
        return f"Tenho o texto '{self.texto}' em mim"

    def dobrar(self):
        self.texto = self.texto + '' + self.texto

class Lista:
    def __init__(self, lista:list = []):
        self.valores = lista

    def __str__(self):
        return f"Tenho os itens {self.valores} dentro da Lista"

    def dobrar(self):
        self.valores = self.valores + self.valores


class Papel:
    def __init__(self):
        self.dobrado = False

    def __str__(self):
        return f"O papel está {'novo' if not self.dobrado else 'dobrado'}"

    def dobrar(self):
        self.dobrado = True 

class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa, muito engraçada . . . "



def tentar_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Encontrei dificuldades em dobrar {objeto.__class__.__name__}")
