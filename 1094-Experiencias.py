n = int(input())
total = 0
coelho = 0
rato = 0
sapo = 0

for leituras in range(0, n, 1):
    cobaia = input().split()
    quantia, tipo = cobaia
    quantia = int(quantia)

    total += quantia

    if(tipo == "C"):
        coelho += quantia

    elif(tipo == "R"):
        rato += quantia

    else:
        sapo += quantia

    p_coelho = (coelho * 100) / total 
    p_rato = (rato * 100) / total 
    p_sapo = (sapo * 100) / total 

print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % coelho)
print("Total de ratos: %d" % rato)
print("Total de sapos: %d" % sapo)
print("Percentual de coelhos: %.2f %%" % p_coelho)
print("Percentual de ratos: %.2f %%" % p_rato)
print("Percentual de sapos: %.2f %%" % p_sapo)