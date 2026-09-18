
from rich import print, inspect
class Avaliacao:
    def __init__(self, nome, discilpina, nota = 0):
        self.nome = nome,  
        self.discilpina = discilpina
        self._nota = nota # ATRIBUTO PROTEGIDO, que não pode ser acessado diretamente fora da classe, mas pode ser acessado através de MÉTODOS ACESSORES (GETTERS E SETTERS)


    ##criando atributo validavel

    @property 
    def nota(self): ## GETTER
        return self._nota

    @nota.setter
    def nota(self, valor): ## SETTER
        if 0 < valor <= 10: ## se a nota estiver entre 0 e 10, ela é atribuida ao atributo protegido
            self._nota = valor
        else: 
            print("Nota inválida")  




