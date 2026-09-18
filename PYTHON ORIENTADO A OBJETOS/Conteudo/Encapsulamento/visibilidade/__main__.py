from ex002 import ContaBancaria;
def main():
    c2= ContaBancaria(2, "Maria", 5000)
    print(c2.__doc__) ## Documentação
    print(c2)
    c2.depositar(-500)
    c2.sacar(-100)

if __name__ == "__main__":
    main()



