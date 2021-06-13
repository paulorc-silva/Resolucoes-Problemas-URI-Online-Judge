tempo = int(input("Digite o tempo de duração em segundos: "))

if(tempo < 60):
    print("00:00:%d" % tempo)

elif(tempo < 3600):
    minuto = tempo // 60
    segundo = tempo % 60  

    print("00:%d:%d" % (minuto, segundo))

else:
    hora = tempo // 3600
    minuto = (tempo // 60) % 60
    segundo = tempo % 60

    print("%d:%d:%d" % (hora, minuto, segundo))
