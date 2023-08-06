n=int(input())
lst=input()
ind=0
cnt=0
while(ind<n-1):
    if lst[ind]==lst[ind+1]:
        cnt+=1
    ind+=1
print(cnt)