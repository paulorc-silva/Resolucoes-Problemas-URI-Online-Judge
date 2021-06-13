p1 = input("Digite as coordenadas X e Y do ponto 1 divididas por espaço: ").split()
p2 = input("Digite as coordenadas X e Y do ponto 2 divididas por espaço: ").split()

x1, y1 = p1
x1 = float(x1)
y1 = float(y1)

x2, y2 = p2
x2 = float(x2)
y2 = float(y2)

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print("A distância entre os pontos é de: %.4f" % distancia)