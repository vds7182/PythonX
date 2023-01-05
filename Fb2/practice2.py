print("Введите число")
num = int(input())

list = []
num2 = 2
while num2 * num2 <= num:
   if num % num2 == 0:
       list.append(num2)
       num //= num2
   else:
       num2 += 1
if num > 1:
   list.append(num)

print(list)