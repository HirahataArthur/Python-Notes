def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol}gol(s) no campeonato!')




nome = input("Nome do Jogador: ")
gols = (input("Numero de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '': ##tira todos os espaços (.strip()), para saber se msm apos isso ele continua vazio, se sim, chama a função apenas com o parametro de gols
    ficha(gol=gols)
else:
    ficha(nome, gols) ##se ao retirar os espaços resta algo, significa que o usuario preencheu o campo, e chama a função com o parametro 'nome' e gols


