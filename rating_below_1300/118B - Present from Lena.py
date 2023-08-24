def func(ind):
    s=[]
    for i in range(ind+1):
        s.append(str(i))

    return " ".join(s)

n=int(input())
ind=0
cnt=2*n
while(ind<=n):
    print(" "*(cnt)+func(ind)+func(ind)[::-1][1:])
    cnt-=2
    ind+=1

ind-=1
cnt+=2
    
while(ind>0):
    ind-=1
    cnt+=2
    print(" "*(cnt)+func(ind)+func(ind)[::-1][1:])
    

