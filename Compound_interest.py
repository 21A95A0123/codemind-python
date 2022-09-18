p,r,t=[int(x)for x in input().split()]
ci=p*pow((1+r/100),t)
print('%.2f'%ci)