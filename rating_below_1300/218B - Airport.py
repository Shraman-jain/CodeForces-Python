n,m =map(int,input().split())
org_lst=list(map(int,input().split()))
lst=org_lst.copy()
max_ans=0
passenger=n
while(passenger!=0):
    lst.sort()
    max_ans+=lst[-1]
    lst[-1]-=1
    passenger-=1

lst=org_lst.copy()
min_ans=0
passenger=n
while(passenger!=0):
    if lst[0]==0:
        lst.pop(0)
        continue
    lst.sort()
    min_ans+=lst[0]
    lst[0]-=1
    passenger-=1

print(max_ans,min_ans)
        
