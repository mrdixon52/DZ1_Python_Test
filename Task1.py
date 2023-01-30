import math
num = int(input('Input any number: ' ))
sum = 0
while num >= 10:
    sum = sum + (num % 10)
    num = math.floor(num / 10)
sum = sum + num
print(sum)

#Второй способ решения
# num = input("Enter number: ")
# sum = 0
# for i in num:
#     sum = sum + int(i)
# print(sum)