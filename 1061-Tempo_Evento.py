di = input().split()
hms_inicio = input().split(" : ")
df = input().split()
hms_fim = input().split(" : ")

di = int(di[1])
df = int(df[1])

hi = int(hms_inicio[0])
mi = int(hms_inicio[1])
si = int(hms_inicio[2])

hf = int(hms_fim[0])
mf = int(hms_fim[1])
sf = int(hms_fim[2]) 
#==================================

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24

inicio = si + mi * minuto_seg + hi * hora_seg + di * dia_seg
fim = sf + mf * minuto_seg + hf *hora_seg + df * dia_seg

if(inicio < fim):
    tempo = fim - inicio
    dia = int(tempo / dia_seg)

    tempo = tempo % dia_seg
    hora = int(tempo / hora_seg)

    tempo = tempo % hora_seg
    minuto = int(tempo / minuto_seg)

    tempo = tempo % minuto_seg
    segundo = tempo

print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % minuto)
print("%d segundo(s)" % segundo)