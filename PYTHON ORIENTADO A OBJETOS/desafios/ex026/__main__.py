from classes import *

def main():
    f1 = Horista("Alex", 25, 72)
    f1.cal_sal()
    f1.analisar_sal()

    f2 = Mensalista("Beatriz", 2400)
    f2.cal_sal()
    f2.analisar_sal()



if __name__ == "__main__":
    main()