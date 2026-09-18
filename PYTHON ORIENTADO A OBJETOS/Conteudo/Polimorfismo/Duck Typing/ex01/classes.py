

class Porta:
    def abrir(self):
        print(f"Gira a maçaneta e empurra/puxa a porta")

class Empresa:
    def abrir(self):
        print(f"Abre um novo cnpj")

class Ovo:
    def abrir(self):
        print(f"Quebra a casca em uma superficie lisa")

class Pedra:
    pass


## MÉTODO DUCK TYIPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Nao consegui abrir {objeto.__class__.__name__}')