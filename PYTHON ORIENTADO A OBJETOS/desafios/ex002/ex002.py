class ContaBancaria:
    """
    Cria um conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        #return f"A conta {self.id} pertencente a {self.nome} possui saldo restante = R${self.saldo:,.2f}"
        return f"Estado atual: {self.__dict__}";


    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de valor R${valor:,.2f} ralizado com sucesso.\nSaldo atual: R${self.saldo:,.2f}")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque no valor de R${valor:,.2f} realizado com sucesso!! \nSaldo atual: R${self.saldo:,.2f}")

