from abc import ABC, abstractmethod



class Funcionario(ABC):
    def __init__(self, nome:str = '', salario:int|float = 0):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    # alteração: property 'salario' adicionada para expor o salário às subclasses sem acessar __salario diretamente

    @salario.setter
    def salario(self, valor):
        # Validação de tipo: só aceita int/float — evita atribuições inválidas
        if not isinstance(valor, (int, float)):
            raise TypeError("salario deve ser um número (int ou float)")

        # Não permitir valores negativos
        if valor < 0:
            raise ValueError("salario não pode ser negativo")

        # Usar o atributo privado name-mangled para comparar o valor atual e evitar chamar o getter
        # (usar self.__salario também funcionaria aqui porque estamos dentro da mesma classe,
        #  mas acessando o name-mangled torna o comportamento explícito e robusto)
        if hasattr(self, "_Funcionario__salario"):
            atual = self._Funcionario__salario
        else:
            # caso improvável: atributo ainda não exista (ex.: durante construção), assumir 0
            atual = 0

        # Permitir apenas aumentos ou manutenção do salário (proibir diminuições)
        if valor < atual:
            # Bloqueia a diminuição; usar exceção em vez de print para sinalizar corretamente
            raise ValueError("Você não pode diminuir o salário — apenas aumentos são permitidos")

        # Atribuição final: atualiza o atributo privado
        self._Funcionario__salario = valor
        # alteração: setter 'salario' adicionado para permitir apenas aumentos


    def __str__(self):
        return f"{self.nome} é um {self.__class__.__name__}. Recebe R${self.salario:,.2f} e receberá um bônus de R${self.calcular_bonus()}"
    # alteração: __str__ atualizado para usar a property 'salario' (feito pelo assistente)

    @abstractmethod
    def calcular_bonus(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    


    def calcular_bonus(self): ##bonus de 15%
        # alteração: usar property 'salario' em vez de __salario (feito pelo assistente)
        bonus = self.salario * 0.15
        return bonus


class Designer(Funcionario): 
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self): ##Bonus de 8%
        # alteração: usar property 'salario' em vez de __salario (feito pelo assistente)
        bonus = self.salario * 0.08
        return bonus


class Desenvolvedor(Funcionario):
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self): #bonus de 10%
        # alteração: usar property 'salario' em vez de __salario (feito pelo assistente)
        bonus = self.salario * 0.10
        return bonus