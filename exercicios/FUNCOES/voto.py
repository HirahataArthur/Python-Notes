from datetime import date
hoje = date.today().year
def voto(num):
    idade = hoje - num
    if idade >= 65:
        return f'Com {idade} anos o voto é: OPCIONAL'
    if idade < 18:
        if idade >= 16:
            return f'com {idade} anos o voto é: OPCIONAL'
        else:
            return f' com {idade} anos o voto é: NEGADO'
    else:
        return f'com {idade} anos o voto é: OBRIGATÓRIO'

ano = int(input("Em que ano você nasceu? "))
vote = voto(ano)
print(vote)
