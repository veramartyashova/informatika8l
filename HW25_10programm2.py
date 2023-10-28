print ("Введите натуральное число")
y=int(input())
if y>0:
    print ('Делители числа')
    for i in range(1,y):
        c=y%i
        if c==0:
             print (i)
        i=i+1
    print (y)
    print ('end')
else:
    print('Вы ввели не натуральное число')



