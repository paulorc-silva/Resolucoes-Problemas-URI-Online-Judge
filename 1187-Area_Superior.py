o = input()
acima = 0
cont = 0

for i in range(0, 12, 1):
    for j in range(0, 12, 1):
        valor = float(input())

        if(((j - i) >= 1) and ((j + i) <= 10)):
            acima += valor
            cont += 1

    if(i == 5):
        break

if(o == "S"):
    print("%.1f" % acima)

else:
    print("%.1f" % (acima / cont))