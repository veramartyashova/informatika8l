print("введите натуральное число")
x=int(input ())
for i in range (2, x-1):
    if x%i==0:
        print ("число непростое")
        break
else:
    print ("число простое")