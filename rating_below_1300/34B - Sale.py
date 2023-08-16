n,m = map(int,input().split())
lst=list(map(int,input().split()))
neg=[]
for i in lst:
    if i<0:
        neg.append(i)
neg.sort()
if len(neg)>m:
    print(sum(neg[:m])*-1)
else:
    print(sum(neg)*-1)

