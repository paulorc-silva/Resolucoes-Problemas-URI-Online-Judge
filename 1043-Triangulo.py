valores = input("Digite os valores de cada lado do triangulo separados por espaço: ").split()

a, b, c = valores

a = float(a)
b = float(b)
c = float(c)

if ((a + b > c) and (a + c > b) and (b + c > a)):
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
    
else:
    areaTra = ((a + b) * c) / 2
    print("Area = %.1f" % areaTra)