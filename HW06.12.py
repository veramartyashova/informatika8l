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
if (x1+x2+y1+y2)%2==0:
    print ("клетки принадлежат одному цвету")
else:
    print ("клетки не принадлежат одному цвету")