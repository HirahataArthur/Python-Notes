from abc import ABC, abstractmethod
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, data_nova:int):
        if data_nova < 1950 or data_nova > date.today().year:
            raise ValueError(f'Ano {data_nova} é inválido')
        else:
            self._nascimento = data_nova
    
    @property 
    def idade(self):
        
        idade = date.today().year - self._nascimento
        return idade

    @idade.setter
    def idade(self, valor = None):
        raise PermissionError('voce nao pode alterar a idade, mude o ano de nascimento')




class Aluno(Pessoa):

    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso
        print('Aluno registado com sucesso')


    def add_curso(self, curso_novo):
        curso_novo = curso_novo.strip().upper()

        if curso_novo in Aluno.cursos_oficiais:
            raise ValueError('Curso ja existente')
        if len(curso_novo) >= 3 and len(curso_novo) <= 5:
            Aluno.cursos_oficiais.append(curso_novo)
            print(f'Curso {curso_novo} adicionado com sucesso')
        else: print('Formato de curso inválido')


    @property 
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in Aluno.cursos_oficiais:
            self._curso = None
            raise ValueError('Opção de curso inválida, fora da lista de cursos oficiais')
        else:
            self._curso = curso
            print(f'Curso do aluno {self._nome} alterado para {self._curso}')


        