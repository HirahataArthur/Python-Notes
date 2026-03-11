for c in range(0, 51):
    s = c%2
    if s == 0:
        print(c)
print("Fim")

##Alternativa a isso: (Mesmo resultado)

for c in range(0, 51, 2):
    print(c)