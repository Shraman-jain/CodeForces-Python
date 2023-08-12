n=int(input())
lst=list(map(int,input().split()))
freq={5:0,0:0}
for i in lst:
    freq[i]+=1

if freq[0]==0:
    print(-1)
else:
    temp=9*(freq[5]//9)
    if temp==0:print(0)
    else:
        ans='5'*(temp)+'0'*(freq[0])
        print(ans)

