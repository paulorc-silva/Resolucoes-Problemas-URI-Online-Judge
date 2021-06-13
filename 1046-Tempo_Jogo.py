horas = input().split()

hora_inicial, hora_final = horas
hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

if(hora_inicial < hora_final):
    tempo = hora_final - hora_inicial

else:
    tempo = (24 - hora_inicial) + hora_final

print("O JOGO DUROU %d HORA(S)" % tempo) 
