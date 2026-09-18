

class Diario:
    def __init__(self, senhamestra="7UH4RCXsEE"):
        self.__senha = senhamestra.strip()
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError('Ninguem tem permissao de ver a senha')

    @senha.setter
    def senha(self, nova_senha):
        senha = str(input("Digite a senha mestra para alterar a senha: ")).strip()
        if senha == self.__senha:
            self.__senha = nova_senha.strip()
            print("Senha alterada com sucesso!")


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0: 
            self.__segredos.append(msg.strip())
            print(f"Segredo adicionado!")
        

    def ler(self, senha=None):
        senha = senha or str(input("Digite a senha mestra para acessar o diário: ")).strip()
        if senha == self.__senha:
            print('Segredos do diario:')
            for segredo in self.__segredos:
                print(f"- {segredo}")
        else:
            raise PermissionError('Senha inválida! Você nao pode ler meu diário!!')