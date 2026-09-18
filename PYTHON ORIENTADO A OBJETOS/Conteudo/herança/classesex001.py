from rich import inspect

class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def Brithday(self):
        self.idade += 1
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        pass



a1 = Aluno("Alex", 30, 'ADS', '2A')
print(a1.__dict__)
inspect(a1, methods=True)