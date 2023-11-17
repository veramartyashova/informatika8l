print ("введите координаты первого шахматного поля от 1 до 8")
print ("x1=")
x1=int (input())
print ("y1=")
y1=int (input())
print ("введите координаты второго шахматного поля от 1 до 8")
print ("x2")
x2=int (input())
print ("y2")
y2=int (input())
a1=x1%2
a2=y1%2
b1=x2%2
b2=y2%2
if (a1==0 and a2==0 and b1==0 and b2==0) or (a1==1 and a2==1 and b1==1 and b2==b1) or (a1==0 and a2==1 and b1==0 and b2==1) or (a1==1 and a2==0 and b1==1 and b2==0):
    print ("клетки принадлежат одному цвету")
else:
    print ("клетки не принадлежат одному цвету")