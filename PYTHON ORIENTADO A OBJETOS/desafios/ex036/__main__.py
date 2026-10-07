from classes import *

def main():
    finalizar_compra(Pix, 4000)
    finalizar_compra(Boleto, -5000)
    finalizar_compra(Cartao, 200)
    finalizar_compra(Cartao, 200)

    p1 = Pix()
    p1.valor = 1000
    print(p1.fvalor)
    print(p1.pagar())

if __name__ == "__main__":
    main()