from operator import itemgetter as ig

n, m = map(int, input().split())

while(n != 0):
    lista_modulo = []

    for leitura in range(0, n, 1):
        num = int(input())

        if(num >= 0):
            modulo = num % m
        
        else:
            modulo = -(abs(num) % m)
            
        if((num % 2) != 0):
            lista_modulo.append((num, modulo, 0, 1, 0))
            
        else:
            lista_modulo.append((num, modulo, 1, 0, 1))
         
    lista_modulo1 = sorted(lista_modulo, key=ig(0), reverse = True)
    lista_modulo2 = sorted(lista_modulo1, key=ig(4))
    lista_modulo3 = sorted(lista_modulo2, key=ig(3), reverse = True)
    lista_modulo4 = sorted(lista_modulo3, key=ig(2))
    lista_modulo_impar = sorted(lista_modulo4, key=ig(1))

    lista_modulo5 = sorted(lista_modulo, key=ig(0))
    lista_modulo6 = sorted(lista_modulo5, key=ig(4))
    lista_modulo7 = sorted(lista_modulo6, key=ig(3), reverse = True)
    lista_modulo8 = sorted(lista_modulo7, key=ig(2))
    lista_modulo_par = sorted(lista_modulo8, key=ig(1))

    print(n, m)

    for i in range(0, n, 1):
        if((lista_modulo_impar[i][0] % 2) != 0):
            print(lista_modulo_impar[i][0])

        else:
            print(lista_modulo_par[i][0])

 
    n, m = map(int, input().split())

print('0 0')