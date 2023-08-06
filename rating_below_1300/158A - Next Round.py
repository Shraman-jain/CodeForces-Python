n,k=map(int,input().split())
scores=list(map(int,input().split()))
kscore=scores[k-1]
cnt=0
for i in range(n):
    if scores[i]>=kscore and scores[i]>0:
        cnt+=1
print(cnt)