conjunto = {}
n = int(input())
aux = input()

for i in range(0, n, 1):
    conjunto.clear()
    porcentagem = 0

    while(True):
        try:
            arvore = input()

            if(arvore == ""):
                break

            if(conjunto.get(arvore)):
                conjunto[arvore] += 1

            else:
                conjunto[arvore] = 1

            porcentagem += 1

        except EOFError:
            break

    for nome, valor in sorted(conjunto.items()):
        valor = 100 + (valor / porcentagem - 1) * 100
        print("%s %.4f" % (nome, valor))

    if(i < (n - 1)):   
        print("")
