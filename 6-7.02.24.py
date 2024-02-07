N=int(input("введите до какого максимального натурального числа будет осуществлять проверка"))
for i in range(1,N):
    x=i
    if ((x > 3) and not(x < 4)) or (x< 1):
        print(x)
        break
    
