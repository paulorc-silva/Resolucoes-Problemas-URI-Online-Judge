codQtd = input("Digite o codigo do item e a quantidade separados por espaço: ").split()

cod, qtd = codQtd

cod = int(cod)
qtd = int(qtd)

if(cod == 1):
    total = qtd * 4.00
    print("Total: R$ %.2f" % total)

elif(cod == 2):
    total = qtd * 4.50
    print("Total: R$ %.2f" % total)

elif(cod == 3):
    total = qtd * 5.00
    print("Total: R$ %.2f" % total)

elif(cod == 4):
    total = qtd * 2.00
    print("Total: R$ %.2f" % total)

else:
    total = qtd * 1.50
    print("Total: R$ %.2f" % total)