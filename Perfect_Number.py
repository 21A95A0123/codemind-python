x = int(input())
y = 0
for i in range(1,x):
    if x%i==0:
        y=y+i
if y==x:
    print("True")
else:
    print("False")