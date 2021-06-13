while(True):
    texto = input()

    if(texto == '*'):
        break

    texto = texto.split(' ')
    cont = 0

    for i in range(0, (len(texto) - 1), 1):
        if((texto[i][0].lower()) == (texto[i + 1][0].lower())):
            cont += 1

    if(cont + 1 == len(texto)):
        print('Y')
    
    else:
        print('N')