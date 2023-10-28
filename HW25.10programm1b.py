print ("Введите натуральное число")
x=(input())
z=len(x)
b=0
x=int(x)
for i in range(z):
    a=x%10
    b=a+b
    x=x//10
print ("Сумма всех цифр числа равна")
print (b)