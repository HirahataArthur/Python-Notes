from abc import ABC, abstractmethod
from random import randint
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
        self.vivo = True
    
    def atacar(self, alvo, força):
        if not self.vivo:
            print(f"[red]{self.nome} está morto e não pode atacar![/]")
            return
        
        dano = randint(0, força)
        print(f"[yellow]{self.nome}[/]([green]{self.vida}[/]) atacou [red]{alvo.nome}[/]([green]{alvo.vida}[/]) com {self.golpes} de força [green]{força}[/]!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"[blue]{self.nome}[/]([green]{self.vida}[/]) recebeu [red] dano de {dano}[/]!")
        
        if self.vida == 0:
            self.vivo = False
            self.morrer()
    
    def analisar(self):
        print(f"[green]{self.nome}[/]: Vida - {self.vida}")
    
    @abstractmethod
    def curar(self):
        pass
    
    @abstractmethod
    def morrer(self):
        pass



class Guerreiro(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)

    def curar(self):
        if not self.vivo:
            print(f"[red]{self.nome} está morto e não pode se curar![/]")
            return
        
        cura = randint(0, 30)
        self.vida += cura
        print(f"[green]{self.nome}[/]([green]{self.vida}[/]) se curou utilizando ataduras e recuperou [yellow]{cura} pontos de vida[/]!")
    
    def morrer(self):
        print(f"[red]{self.nome}[/]([green]{self.vida}[/]) morreu em batalha!")


class Mago(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
    

    def curar(self):
        if not self.vivo:
            print(f"[red]{self.nome} está morto e não pode se curar![/]")
            return
        
        cura = randint(0, 100)
        self.vida += cura
        print(f"[green]{self.nome}[/]([green]{self.vida}[/]) se curou conjurando um feitiço e recuperou [yellow]{cura} pontos de vida[/]!") 
    
    def morrer(self):
        print(f"[red]{self.nome}[/]([green]{self.vida}[/]) morreu em batalha!")

        