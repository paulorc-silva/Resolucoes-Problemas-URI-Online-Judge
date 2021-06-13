n = int(input())
num = 1

while(num <= (n * 4)):
    if((num % 4) != 0): 
        print(num, end=' ')

    if((num % 4) == 0):
        print("PUM")
        num += 1
        continue
    
    num += 1