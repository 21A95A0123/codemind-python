n=int(input())
a=0
b=1
c=a+b
while n>0:
    a=b
    b=c
    c=a+b
    if c+1>n:
        break
if c==n:
    print('True')
else:
    print('False')