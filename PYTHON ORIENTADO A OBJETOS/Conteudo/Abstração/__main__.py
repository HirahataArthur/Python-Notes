from rich import inspect
from classesex001 import Aluno, Professor, Funcionario

def main():


    
    a1 = Aluno("Alex", 30, 'ADS', '2A')
    print(a1.__dict__)
    inspect(a1, methods=True)

    p1 = Professor("Alex", 29, "INGLÊS", "3A")
    inspect(p1, methods=True)

    f1 = Funcionario("Alex", 30, "PROFESSOR", "INGLÊS")
    inspect(f1, methods=True)

    f1.estudar()



if __name__ == "__main__":
    main()