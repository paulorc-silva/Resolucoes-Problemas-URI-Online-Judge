p = input("Digite as coordenadas X e Y do ponto divididas por espaço: ").split()
x, y = p

x = float(x)
y = float(y)

if((x > 0) and (y > 0)):
    print("O ponto pertence ao quadrante 1")

elif((x < 0) and (y > 0)):
    print("O ponto pertence ao quadrante 2")

elif((x < 0) and (y < 0)):
    print("O ponto pertence ao quadrante 3")

elif((x > 0) and (y < 0)):
    print("O ponto pertence ao quadrante 4")

elif(y == 0):
    print("O ponto está sobre o eixo X")

elif(x == 0):
    print("O ponto está sobre o eixo Y")

else:
    print("O ponto está na origem (X = 0; Y = 0)")