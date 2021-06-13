alcool = 0
gasolina = 0
diesel = 0

while(True):
    codigo = int(input())

    if(codigo == 1):
        alcool += 1

    elif(codigo == 2):
        gasolina += 1

    elif(codigo == 3):
        diesel += 1
    
    elif(codigo == 4):
        break
    
print("MUITO OBRIGADO")
print("Alcool: %d" % alcool)
print("Gasolina: %d" % gasolina)
print("Diesel: %d" % diesel)