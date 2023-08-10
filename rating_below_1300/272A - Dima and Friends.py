n=int(input())
lst=list(map(int,input().split()))
total_finger=sum(lst)

cnt=0

for i in range(1,6):
    if (total_finger+i)%(n+1)!=1:
        cnt+=1
print(cnt)