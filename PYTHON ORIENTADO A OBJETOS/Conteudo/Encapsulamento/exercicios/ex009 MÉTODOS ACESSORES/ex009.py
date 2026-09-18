
from rich import print, inspect
class Avaliacao:
    def __init__(self, nome, discilpina, nota = 0):
        self.nome = nome,  
        self.discilpina = discilpina
        self._nota = nota

    ##para mexer na nota, que agora é um atributo protegido, utilizamos os MÉTODOS ACESSORES:
    
    def get_nota(self): ## MÉTODO GETTER
       return self._nota


    def set_nota(self, valor): ##MÉTODO SETTER
        if 0 < valor <= 10: ## se a nota estiver entre 0 e 10, ela é atribuida ao atributo protegido
            self._nota = valor
        else: 
            print("Nota inválida")      