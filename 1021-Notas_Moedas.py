valor = float(input("Digite o valor necessário: "))

n100 = valor // 100
resto = valor % 100

n50 = resto // 50
resto = resto % 50

n20 = resto // 20
resto = resto % 20

n10 = resto // 10
resto = resto % 10

n5 = resto // 5
resto = resto % 5

n2 = resto // 2
resto = resto % 2

m1 = resto // 1
resto = resto % 1

m50 = resto // 0.5
resto = resto % 0.5

m25 = resto // 0.25
resto = resto % 0.25

m10 = resto // 0.1
resto = resto % 0.1

m05 = resto // 0.05
resto = resto % 0.05

m01 = resto // 0.01
resto = resto % 0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % n100)
print("%d nota(s) de R$ 50.00" % n50)
print("%d nota(s) de R$ 20.00" % n20)
print("%d nota(s) de R$ 10.00" % n10)
print("%d nota(s) de R$ 5.00" % n5)
print("%d nota(s) de R$ 2.00" % n2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % m1)
print("%d moeda(s) de R$ 0.50" % m50)
print("%d moeda(s) de R$ 0.25" % m25)
print("%d moeda(s) de R$ 0.10" % m10)
print("%d moeda(s) de R$ 0.05" % m05)
print("%d moeda(s) de R$ 0.01" % m01)