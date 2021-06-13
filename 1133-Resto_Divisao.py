x = int(input())
y = int(input())

if(x < y):
    for num in range((x + 1), y, 1):
        if(((num % 5) == 2) or ((num % 5) == 3)):
            print(num)

else:
    for num in range((y + 1), x, 1):
        if(((num % 5) == 2) or ((num % 5) == 3)):
            print(num)