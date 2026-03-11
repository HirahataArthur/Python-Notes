def escreva(string):
    for c in string:
        print("~~", end='')
    print()
    print(f"  {string}")
    for c in string:
        print("~~", end='')
        

string = str(input("Escreva seu nome"))
escreva(string)