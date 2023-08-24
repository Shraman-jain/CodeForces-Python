n,m=map(int,input().split())
lst=list(map(int,input().split()))

time=lst[0]-1
for i in range(1,len(lst)):
    if lst[i-1]>lst[i]:
        time+=(n-lst[i-1])+(lst[i]-1)+1
    elif lst[i-1]<lst[i]:
        time+=lst[i]-lst[i-1]
    
    
    

print(time)