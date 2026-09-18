from classes import Moto,Caminhao,Drone
from rich import print
from rich.table import Table
def main():
    dist = 49
    t1 = Caminhao(dist)
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{t1.cal_frete()}")


    def tabela():
    
        tabela = Table(title="--Frete Tabela--")
        tabela.add_column("Distância")
        tabela.add_column("Tipo")
        tabela.add_column("Frete")
        tabela.add_row(f"{dist}km", "Moto", f"R${(dist * 0.5):.2f}")
        if dist < 50: preco_caminhao = "Distancia minima 50km."
        else: 
            precoC = dist * 1.2
            preco_caminhao = f"R${precoC:.2f}"
        tabela.add_row(f"{dist}km", "Caminhao", preco_caminhao)
        if dist > 10: preco_drone = "Distancia maxima 10km"
        else: 
            precoD = dist * 9.5
            preco_drone = f"R${precoD:.2f}"
        tabela.add_row(f"{dist}km", "Drone", preco_drone)
        print(tabela)

    tabela()

if __name__=="__main__":
    main()