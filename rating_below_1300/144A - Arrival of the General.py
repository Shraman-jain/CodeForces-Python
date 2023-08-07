n=int(input())
arr=list(map(int,input().split()))

max_arr=max(arr)
min_arr=min(arr)

max_dist=1000
min_dist=0

for i in range(len(arr)):
    if arr[i]==min_arr:
        min_dist=max(min_dist,i)

for i in range(len(arr)):
    if arr[i]==max_arr:
        max_dist=min(max_dist,i)

if max_dist<min_dist:
    ans=(max_dist)+(n-1-min_dist)
    print(ans)
else:
    ans=(max_dist)+(n-1-(min_dist+1))
    print(ans)