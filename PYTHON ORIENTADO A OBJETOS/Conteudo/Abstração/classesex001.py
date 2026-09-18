from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def Brithday(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
        
    def estudar(self):
        print(f"O aluno {self.nome} está estudando {self.curso} e está na turma {self.turma}")

    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def estudar(self):
        print(f"O Professor {self.nome} é especialista em {self.especialidade} no nivel {self.nivel}")
    
    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def estudar(self):
        print(f"O funcionario {self.nome} nao estuda kkkkkkkkkkkkkk")
    
    def bater_ponto(self):
        pass


