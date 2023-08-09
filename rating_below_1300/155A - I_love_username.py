n=int(input())
arr=list(map(int,input().split()))[:n]
cnt=0
curr_max=arr[0]
curr_min=arr[0]
for i in range(1,n):
    if arr[i]>curr_max:
        curr_max=arr[i]
        cnt+=1
    elif arr[i]<curr_min:
        curr_min=arr[i]
        cnt+=1

print(cnt)