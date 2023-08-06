n=int(input())
ans=0
for _ in range(n):
    s=list(map(int,input().split()))
    cnt=s.count(1)
    if cnt>=2:
        ans+=1
print(ans)