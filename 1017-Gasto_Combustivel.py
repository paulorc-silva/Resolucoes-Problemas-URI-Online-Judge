tempo = int(input("Digite o tempo gasto na viagem em horas: "))
velocidade = float(input("Digite a velocidade em Km/h: "))

distancia = velocidade * tempo

litro = distancia / 12

print("%.3f" % litro)