n = int(input("Digite a quantidade de médias que deseja realizar: "))

for valores in range(0, n, 1):
    val = input("Digite os 3 valores para calcular a média divididos por espaço: ").split()
    v1, v2, v3 = val

    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)

    media = ((v1 * 2) + (v2 * 3) + (v3 * 5)) / 10
    print("A média dos valores digitados é: %.1f" % media)