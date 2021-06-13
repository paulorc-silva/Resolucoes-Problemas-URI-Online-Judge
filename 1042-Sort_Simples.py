valores = input().split()

a, b, c = valores

a = int(a)
b = int(b)
c = int(c)

lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort()

[print(item) for item in lista]
print("")
print(a)
print(b)
print(c)