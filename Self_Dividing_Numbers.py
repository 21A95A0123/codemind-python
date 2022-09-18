x=int(input())
y=int(input())
c=0
for i in range(x,y+1):
    t=i
    c=0
    s=0
    while(t!=0):
        d=t%10
        t=t//10
        c+=1
        if d==0:
            break
        if i%d==0:
            s+=1
    if s==c:
        print(i,'',end='')