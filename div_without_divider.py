x,n = map(int,input().split())
c = 0
while(x>0):
    x = x-n
    if(x>=0):
        c+=1
print(c)
