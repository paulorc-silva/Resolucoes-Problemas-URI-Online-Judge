salario = float(input("Digite seu salário: "))

if(salario <= 2000.00):
    print("Isento")

elif((salario >= 2000.01) and (salario <= 3000.00)):
    imposto_renda = (salario - 2000.00) * 0.08

elif((salario >= 3000.01) and (salario <= 4500.00)):
    imposto_renda = (1000.00 * 0.08) + ((salario - 3000.00) * 0.18)
    
else:
    imposto_renda = (1000.00 * 0.08) + (1500 * 0.18) + ((salario - 4500.00) * 0.28)


if(salario > 2000.00):
    print("O valor do imposto de renda é de: R$ %.2f" % imposto_renda)