movimento = input().split()

origem, destino = movimento

j = abs(ord(origem[0]) - ord(destino[0]))
i = abs(int(origem[1]) - int(destino[1]))

if((j == 1) and (i == 2)) or ((j == 2) and (i == 1)):
    print('VALIDO')
else:
    print('INVALIDO')