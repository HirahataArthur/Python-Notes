

## DECLARAÇÃO DE CLASSE
## class + nome da classe começando com letra maiuscula (MinhaClasse)
## area de declaraçao de atributos e metodos

## DECLARAÇÃO DE OBJETOS
## objeto = MinhaClasse() ----- Chamada de instanciação/ Método construtor, construindo o objeto


##EX:

class Gafanhoto:
    def __init__(self): #Método construtor

        #Atributos de instância
        self.nome = ""
        self.idade = 0

    ## Métodos da instância 
    def aniversario(self):
        self.idade = self.idade + 1
    
    def msg(self):
        return f"{self.nome} tem {self.idade} anos."
    
##Declarando objetos
g1 = Gafanhoto()
g1.nome = "Alex"
g1.idade = 30
print(g1.msg())
g1.aniversario()
print(g1.msg())

g2 = Gafanhoto()
g2.nome = "Beatriz"
g2.idade = 30
g2.aniversario()
print(g2.msg())
