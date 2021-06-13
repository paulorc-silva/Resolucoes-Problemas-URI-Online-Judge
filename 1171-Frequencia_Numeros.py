n = int(input())
numeros = {}

for leitura in range(0, n, 1):
    num = int(input())

    if(num in numeros):
        numeros[num] += 1

    else:
        numeros[num] = 1

id = numeros.keys()
id = sorted(id)

for key in id:
    print("%d aparece %d vez(es)" %(key, numeros[key]))