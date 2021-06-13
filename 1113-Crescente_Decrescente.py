while(True):
    numeros = input().split()
    a, b = numeros

    a = int(a)
    b = int(b)

    if((a == b)):
        break

    if(a < b):
        print("Crescente")

    else:
        print("Decrescente")
