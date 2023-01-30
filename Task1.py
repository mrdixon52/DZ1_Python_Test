import math
num = int(input('Input any number: ' ))
sum = 0
while num >= 10:
    sum = sum + (num % 10)
    num = math.floor(num / 10)
sum = sum + num
print(sum)