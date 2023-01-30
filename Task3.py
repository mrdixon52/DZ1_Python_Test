import math
num = int(input('Input number of ticket: ' ))
sum1 = 0
sum2 = 0
while num >= 1000:
    sum1 = sum1 + (num % 10)
    num = math.floor(num / 10)
while num >= 10:
    sum2 = sum2 + (num % 10)
    num = math.floor(num / 10)
sum2 = sum2 + num
if sum1 == sum2:
    print('Yes')
else:
    print('No')