valores = input("Digite três valores separados por um espaço: ").split()

a, b, c = valores

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b)) / 2

maior = (maiorAB + c + abs(maiorAB - c)) / 2

print("%d eh o maior" % maior)