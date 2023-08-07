n=int(input())
if n%2!=0:
    print(-1)
else:
    arr=[i+1 for i in range(n)]
    ind=0
    while(ind<len(arr)-1):
        arr[ind],arr[ind+1]=arr[ind+1],arr[ind]
        ind+=2
    print(*arr)