from classes import *

def main():
    a = Carteira(100)
    b = Carteira(100)
    print(a == b)
    a += 50
    b -= 10
    print(a, b)
    print(a == b)
    


if __name__ == "__main__":
    main()