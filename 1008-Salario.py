numero = int(input("Digite seu número: "))
hora = int(input("Digite o número de horas trabalhadas: "))
valor = float(input("Digite o valor que você recebe por hora: "))

salario = hora * valor

print("NUMBER = %d" % numero)
print("SALARY = U$ %.2f" % salario)