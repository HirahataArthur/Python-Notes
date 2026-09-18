
class Gafanhoto:
    def __init__(self, n = "", i = 0): #Método construtor/ Parametros

        #Atributos de instância
        self.nome = n
        self.idade = i

    ## Métodos da instância 
    def aniversario(self):
        self.idade = self.idade + 1
    
    def msg(self):
        return f"{self.nome} tem {self.idade} anos."
    
##Declarando objetos
g1 = Gafanhoto("Alex", 30) # Ja com parametros
print(g1.msg())
g1.aniversario()
print(g1.msg())
