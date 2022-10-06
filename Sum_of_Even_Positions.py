n=int(input())
l=[int(i)for i in input().split()]
sum=0
for ch in range(0,n,2):
    sum=sum+l[ch]
print(sum)