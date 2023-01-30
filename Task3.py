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

#Второй способ решения
# num = input('Enter number of ticket: ')
# sum1 = int(num[0]) + int(num[1]) + int(num[2])
# sum2 = int(num[3]) + int(num[4]) + int(num[5])
# if sum1 == sum2:
#     print('Yes')
# else:
#     print('No')