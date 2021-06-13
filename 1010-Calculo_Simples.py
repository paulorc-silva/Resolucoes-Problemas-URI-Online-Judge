peca1 = input("Digite o código da peça 1, o número de peças 1 e o valor unitário de cada peça 1 separados por espaço: ").split()
peca2 = input("Digite o código da peça 2, o número de peças 2 e o valor unitário de cada peça 2 separados por espaço: ").split()

cod1, qtd1, preco1 = peca1
cod2, qtd2, preco2 = peca2

cod1 = int(cod1)
qtd1 = int(qtd1)
preco1 = float(preco1)

cod2 = int(cod2)
qtd2 = int(qtd2)
preco2 = float(preco2)

total = (qtd1 * preco1) + (qtd2 * preco2)

print("VALOR A PAGAR: R$ %.2f" % total)