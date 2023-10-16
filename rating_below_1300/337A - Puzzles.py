n,m=map(int,input().split())
lst=list(map(int,input().split()))[:m]
lst.sort()
ans=lst[-1]
for i in range(0,m-n+1):
    ans=min(ans,lst[i:i+n][-1]-lst[i:i+n][0])
print(ans)

