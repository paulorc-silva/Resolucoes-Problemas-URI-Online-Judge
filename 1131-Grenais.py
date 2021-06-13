continua = 1
grenal = 0
v_inter = 0
v_gremio = 0
empate = 0

while(True):
    if(continua == 2):
        break
    
    if(continua == 1):
        grenal += 1
        gols = input().split()
        inter, gremio = gols

        inter = int(inter)
        gremio = int(gremio)

        if(inter > gremio):
            v_inter += 1

        elif(inter < gremio):
            v_gremio += 1
        
        else:
            empate += 1

        continua = 0
        continue

    continua = int(input("Novo grenal (1-sim 2-nao)\n"))
    continue

print("%d grenais" % grenal)
print("Inter:%d" % v_inter)
print("Gremio:%d" % v_gremio)
print("Empates:%d" % empate)

if(v_inter > v_gremio):
    print("Inter venceu mais")

elif(v_inter < v_gremio):
    print("Gremio venceu mais")

else:
    print("Nao houve vencedor")