print("Введите первое число")
fizz = int(input())
print("Введите второе число")
buzz = int(input())
num=0
print("Введите количество повторений")
count = int(input())
for i in range(count):
   if(num==count):
       print(list)
   else:
       num+=1
       list = [num]
       if(num % buzz == 0 and num%fizz==0):
           print("FB")
       elif(num%buzz==0):
           print("B")
       elif (num%fizz==0):
           print("F")
       else:
           print(num)
input()
