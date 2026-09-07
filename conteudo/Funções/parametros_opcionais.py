def somar(a, b, c=0): ##c=0 significa que c é um parametro opcional, se ele nao for recebido nao impacta na soma
    s = a + b + c
    print(f"A soma é {s}")

somar(5, 2, 1)
somar(8, 4)