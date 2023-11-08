print ("введите количество чисел")
n=int (input ())
z=0
for i in range (n):
    print ("ввидите Число")
    x=int (input())
    a=x%3
    if a==0:
        z=z+1
print ("количество чисел кратное 3 равно")
print (z)
       