par = 0
impar = 0
positivo = 0
negativo = 0

for cont in range(1, 6, 1):
    num = float(input("Digite um número positivo ou negativo: "))

    if((num % 2) == 0):
        par += 1

    elif((num % 2) != 0):
        impar += 1

    if(num > 0):
        positivo += 1
    
    elif(num < 0):
        negativo += 1
    
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")