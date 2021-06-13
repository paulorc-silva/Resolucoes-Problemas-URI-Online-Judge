idade = int(input("Digite a sua idade em dias: "))

ano = idade // 365 
mes = (idade % 365) // 30
dia = (idade % 365) % 30

print("Você tem:", ano, "ano(s),", mes, "mes(es),", dia, "dia(s)")