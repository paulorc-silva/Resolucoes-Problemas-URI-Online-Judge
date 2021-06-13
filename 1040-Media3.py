notas = input("Digite as notas separadas por espaço: ").split()

a, b, c, d = notas

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10

if(media >= 7.0):
    print("Media: %.1f" % media)
    print("Aluno aprovado.")

elif((media >= 5.0) and (media <= 6.9)):
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    exame = float(input("Digite a nota do exame: "))
    
    print("Nota do exame: %.1f" % exame)

    novaMedia = (media + exame) / 2

    if(novaMedia >= 5.0):
        print("Aluno aprovado.")
        print("Media final: %.1f" % novaMedia)

    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % novaMedia)

else:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")