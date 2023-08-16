"""
recursion-based solution

def f(ind,arr,temp,k,min_len):
    if ind==len(arr):
        return min_len
    if sum(temp)>=k:
        # print(temp)
        min_len=min(min_len,len(temp))
        return min_len
        
    
    temp.append(arr[ind])
    pick=f(ind+1,arr,temp,k,min_len)
    temp.pop()
    not_pick=f(ind+1,arr,temp,k,min_len)
    return min(pick,not_pick)



k=int(input())
arr=list(map(int,input().split()))
if k==0:
    print(0)
elif sum(arr)<k:
    print(-1)
else:
    arr.append(0)
    print(f(0,arr,[],k,15))
    
"""

# greedy
k=int(input())
arr=list(map(int,input().split()))

arr.sort(reverse=True)

months=0
total=0
for i in range(12):
    if total>=k:
        break
    total+=arr[i]
    months+=1


if k==0:
    print(0)
elif sum(arr)<k:
    print(-1)
else:
    print(months)


