from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer:
    def __init__(self, name, nickname, favorite_games = None):
        self.name = name
        self.nickname = nickname
        self.favorite_games = favorite_games or []
        print("Jogador cadastrado com sucesso.")

    def add_game(self, game):
        self.favorite_games.append(game)
        print("Jogo adicionado!")

    def inspect(self):
        self.favorite_games.sort()
        games_formatados = "\n".join([f":video_game: [blue]{game}[/]" for game in self.favorite_games])  # ALTERADO: formata lista em linhas separadas e em azul
        painel = Panel(
            f"Nome real: [white on blue]{self.name}[/]\n"
            f"Jogos favoritos:\n{games_formatados}",  # ALTERADO: agora usa a string formatada
            title=f"Jogador <{self.nickname}>",
            width=40
        )
        return painel
    
p1 = Gamer("Alex", "player_example")
p1.add_game("Hollow knight")
print(p1.inspect())
p1.add_game("Zelda BOTW")
p1.add_game("Minecraft")
print(p1.inspect())

