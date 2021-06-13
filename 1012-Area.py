valores = input("Digite três valores separados por um espaço: ").split()

a, b, c = valores

a = float(a)
b = float(b)
c = float(c)

areaTri = (a * c) / 2

areaCirc =  3.14159 * (c ** 2)

areaTra =  ((a + b) * c) / 2

areaQuad = b ** 2

areaRet = a * b

print("TRIANGULO: %.3f" % areaTri)
print("CIRCULO: %.3f" % areaCirc)
print("TRAPEZIO: %.3f" % areaTra)
print("QUADRADO: %.3f" % areaQuad)
print("RETANGULO: %.3f" % areaRet)