print ("Введите трехзначное натуральное число")
x=int (input()) 
c=x%10
b=x//10%10
a=x//100
y=a+b+c
print ("Сумма всех цифр числа равна")
print (y)