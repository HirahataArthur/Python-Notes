from hashlib import sha256
import getpass
from pwinput import pwinput

class ContaBancaria:
    """
    Cria um conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id # protegido
        self._titular = nome #protegido
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f'A conta {self._id} foi criada com sucesso!')

    def __str__(self):
        #return f"A conta {self.id} pertencente a {self.nome} possui saldo restante = R${self.saldo:,.2f}"
        return f"Estado atual: {self.__dict__}";

    def pede_senha(self):
        
        while True:
            senha = str(pwinput('Senha: ')).strip()
            if len(senha) >= 6:
                break
            else: print('formato de senha inávlido (6 ou mais caracteres)')
        return senha

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False



    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de valor R${valor:,.2f} ralizado com sucesso.\nSaldo atual: R${self.__saldo:,.2f}")
    
    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)


        if chave == None:
            chave = self.pede_senha()
        
        
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print("Saldo insuficiente!")
            else:
                self.__saldo -= valor
                print(f"Saque no valor de R${valor:,.2f} realizado com sucesso!! \nSaldo atual: R${self.__saldo:,.2f}")
        else:
            print('Senha não bate! Saque nao autorizado!')

    @property 
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
                print('Nome alterado com sucesso')
            else: print('Nome nao atende aos requisitos de registro (5 caracteres no minimo)')

            
        else: print('senha nao confere')