def f(a,b,n,m):
    if a<0 or b<0:return False
    if a**2+b==n and b**2+a==m:
        return True
    else:
        return False

n,m=map(int,input().split())
cnt=0
for a in range(n+1):
    try:
        # print((a-m),((a**2)-n),(a-m)%((a**2)-n))
        if a-m==0:
            if f(a,0,n,m):cnt+=1
        elif (a-m)%((a**2)-n)==0:
            if f(a,(a-m)//((a**2)-n),n,m):
                cnt+=1
    except:
        # print("error",(a-m),((a**2)-n))
        continue
print(cnt)


