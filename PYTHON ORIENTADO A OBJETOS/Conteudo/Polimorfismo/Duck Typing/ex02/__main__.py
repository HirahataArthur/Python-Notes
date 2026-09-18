from classes import *


def main():

    a = Numero(200)
    b = Texto('LU')
    c = Lista([1,2,3])
    d = Papel()
    e = Casa()

    tentar_dobrar(a)
    tentar_dobrar(b)
    tentar_dobrar(c)
    tentar_dobrar(d)
    tentar_dobrar(e)



    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == "__main__":
    main()