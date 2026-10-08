from classes import *


def main():
    p1 = Produto("Notebook", 10000.0)
    p2 = Produto("Placa de Vídeo", 1500.0)
    p3 = Produto("Processador", 900.0)

    print(p1)
    print(p2)
    print(p3)
    c1 = Carrinho()
    c2 = Carrinho()
   

    print(c1.total) ## nada no carrinho ainda
    print(c1)


    c2 += p3
    c1 = c1 + p1
    c1 += p2
    c1 += c2 ##Possivel juntar um carrinho no outro
    print(c1)
    print(c1.total)

    



if __name__ == "__main__":
    main();