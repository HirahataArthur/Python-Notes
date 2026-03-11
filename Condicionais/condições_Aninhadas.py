idade = int(input("Qual é a sua idade? \n"))
if idade == 18:
    print("Você tem a mesma idade que eu!")
elif idade < 18:
    diferenca = 18 - idade
    print("Você é {} anos mais novo do que eu!".format(diferenca))
else:
    diferenca = idade - 18
    print("Você é {} anos mais velho do que eu!".format(diferenca))