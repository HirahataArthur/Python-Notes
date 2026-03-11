n1 = int(input("Digite o número do qual pretende obter a tabuada:\n >>> "))
n2 = int(input("Digite até qual número deseja multiplicar o anterior: \n >>>"))
for c in range(1, n2+1):
    s = n1 * c
    print("{} vezes {} = {}".format(n1, c, s))