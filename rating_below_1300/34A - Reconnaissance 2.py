n=int(input())
lst=list(map(int,input().split()))

first_ind,second_ind=0,0
ans=100005
for i in range(len(lst)-1):
    if abs(lst[i]-lst[i+1])<ans:
        first_ind=i+1
        second_ind=i+2
        ans=abs(lst[i]-lst[i+1])

if abs(lst[-1]-lst[0])<ans:
    first_ind=n
    second_ind=1

print(first_ind,second_ind)
