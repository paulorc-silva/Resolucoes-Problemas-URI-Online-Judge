n = int(input("Digite um número: "))

for par in range(2, (n + 1), 2):
    if((par % 2) == 0):
        quadrado = par ** 2
        print("%d^2 = %d" % (par, quadrado))