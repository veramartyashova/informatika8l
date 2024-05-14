#Написать программу, которая подсчитает количество букв Н в значении выражения, записанного в 24-ой системе счисления. Выражение (в скобках указана система счисления): 105(8) + 5F (37) * 1011 (3) ** BA(15)и
def func (x:str, base: int)-> str:
    "Функция перевода в десятичную систему из системы не больше 37"
    alfavit="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"
    k=len(x)-1
    reuslt=0
    for i in x:
        reuslt+=alfavit.index(i)*base**k 
        k-=1 
    return reuslt
namber =func("108",8)+func("5F",37)*func("1011",3)**func("BA",15)
print ("Значение выражения в десятичной системе", namber)
z=0
while namber>=23:
    y=namber%24
    namber=namber//24
    if y==17:
        z=z+1
print ("Количество букв Н в значении выражения, записанного в 24-ой системе счисления:", z)
