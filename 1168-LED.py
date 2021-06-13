# Versão original (Eu que fiz)
n = int(input())
led = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}

for leituras in range(0, n, 1):
    qtd = 0
    num = input()

    for value in num:
        for key in range(0, 10, 1):
            if(int(value) == key):
                qtd += led[key]
                break

    print("%d leds" % qtd)

'''======================================================'''
# Versão otimizada (Web)
n = int(input())
led = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)

for leituras in range(0, n, 1):
    qtd = 0
    num = input()

    for value in num:
        qtd += led[int(value)]
        
    print("%d leds" % qtd)