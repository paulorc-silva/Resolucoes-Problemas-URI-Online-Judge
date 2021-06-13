continua = 1

while(True):
    if(continua == 2):
        break
    
    if(continua == 1):
        valido = 0
        media = 0
        while(valido != 2):
            nota = float(input())
            soma = 0
            
            if((nota >= 0) and (nota <= 10)):
                soma += nota
                valido += 1

            else:
                print("nota invalida")

            media += soma / 2

        print("media = %.2f" % media)
        continua = 0
        continue 

    continua = int(input("novo calculo (1-sim 2-nao)\n"))