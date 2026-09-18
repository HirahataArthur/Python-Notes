class ContaBancaria:
    """
    Cria um conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self._nome = nome
        self.__saldo = saldo

    def __str__(self):
        #return f"A conta {self.id} pertencente a {self.nome} possui saldo restante = R${self.saldo:,.2f}"
        return f"Estado atual: {self.__dict__}";


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de valor R${valor:,.2f} ralizado com sucesso.\nSaldo atual: R${self.__saldo:,.2f}")
    
    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print("Saldo insuficiente!")
        else:
            self.__saldo -= valor
            print(f"Saque no valor de R${valor:,.2f} realizado com sucesso!! \nSaldo atual: R${self.__saldo:,.2f}")
c1= ContaBancaria(1, "Alex", 1000)
print(c1.__doc__) ## Documentação
c1.sacar(-100)
print(c1)
print(c1._ContaBancaria__saldo) ## Atributo privado não pode ser acessado diretamente
