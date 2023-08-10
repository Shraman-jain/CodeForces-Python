n=int(input())
lst=list(map(int,input().split()))

ind=0
while(n>0):
    curr_ind=ind%7
    n-=lst[curr_ind]
    ind+=1
print(curr_ind+1)