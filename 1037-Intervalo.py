numero = float(input("Digite um número: "))

if((numero >= 0) and (numero <= 25)):
    print("Intervalo [0,25]")

elif((numero > 25) and (numero <= 50)):
    print("Intervalo (25,50]")

elif((numero > 50) and (numero <= 75)):
    print("Intervalo (50,75]")

elif((numero > 75) and (numero <= 100)):
    print("Intervalo (75,100]")

else:
    print("Fora de intervalo")