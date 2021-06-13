par = []
impar = []

for i in range(0, 15, 1):
    valor = int(input())

    if((valor % 2) == 0):
        par.append(valor)

    else:
        impar.append(valor)
    
    if(len(par) == 5):
        indice_qtd = 0

        for v in par:
            print("par[%d] = %d" % (indice_qtd, v))
            indice_qtd += 1

        par = []

    if(len(impar) == 5):
        indice_qtd = 0

        for v in impar:
            print("impar[%d] = %d" %(indice_qtd, v))
            indice_qtd += 1

        impar = []

if(len(impar) > 0):
    indice_qtd = 0

    for v in impar:
        print("impar[%d] = %d" %(indice_qtd,v))
        indice_qtd += 1

if(len(par) > 0):
    indice_qtd = 0
    
    for v in par:
        print("par[%d] = %d" %(indice_qtd,v))
        indice_qtd += 1