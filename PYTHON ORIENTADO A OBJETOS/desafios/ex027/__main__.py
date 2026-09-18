from classes import Guerreiro, Mago

def main():

    p1 = Guerreiro("Ghost", 1000, "Ferroada")
    p2 = Mago("Shaman Caracol", 500, "Magia de alma")

    p1.atacar(p2, 200)
    p2.curar()
    p1.analisar()
    p2.analisar()
    p2.atacar(p1, 1000)
    p2.atacar(p1, 1000)

    p1.analisar()

    p1.atacar(p2, 200)







if __name__ == "__main__":
    main()