valores = input("Digite os valores de A, B e C separados por um espaço: ").split()

a, b, c = valores

a = float(a)
b = float(b)
c = float(c)

delta = (b ** 2) - 4 * a * c

if((delta <= 0) or (a == 0)):
    print("Impossivel calcular")

else:
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)