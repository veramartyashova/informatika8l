def average(*spisok)->float:
    """
    Эта функция вычисляет среднее арифметическое значение неизвестного количества аргументов
    """
    s=0
    n=1
    for i in spisok:
        if type(i) == int or type(i)==float:
            s +=i
            f=s/n
            n=n+1
    return f
print (average ('hello',40.2,90,10,8.5,'hi'))


help(average)