print("Введите первое число")
fizz = int(input())
print("Введите второе число")
buzz = int(input())
num=0
print("Введите количество повторений")
count = int(input())
file=open("result.txt",'a')
for i in range(count):
   if(num==count):
       file.write(list)
   else:
       num+=1
       list = [num]
       if(num % buzz == 0 and num%fizz==0):
           file.write(" FB ")
       elif(num%buzz==0):
           file.write(" B ")
       elif (num%fizz==0):
           file.write(" F ")
       else:
           file.write(str(num))
