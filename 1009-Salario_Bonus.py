nome = input("Digite seu nome com letras maiúsculas: ")
salario = float(input("Digite seu salário: "))
vendas = float(input("Digite o valor total das vendas efetuadas: "))

bonus = vendas * 0.15

novoSalario = salario + bonus

print("TOTAL = R$ %.2f" % novoSalario)