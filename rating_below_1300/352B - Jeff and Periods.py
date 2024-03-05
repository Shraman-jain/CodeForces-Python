def AP(lst):
    
    d=lst[1]-lst[0]
    for i in range(len(lst)-1):
        if lst[i+1]-lst[i]!=d:
            return 0
    return d

n=int(input())
lst=list(map(int,input().split()))
if n==1:
    print(1)
    print(lst[0],0)
elif len(set(lst))==1:
    print(1)
    print(lst[0],1)
else:
    freq={}
    for index,val in enumerate(lst):
        if val in freq:
            freq[val].append(index)
        else:
            freq[val]=[index]
    all_x=sorted(list(set(lst)))
    all_valid_x={}
    for i in all_x:
        if len(freq[i])==1:
            all_valid_x[i]=0
        else:
            d=AP(freq[i])
            if d!=0:
                all_valid_x[i]=d
    print(len(list(all_valid_x.keys())))
    for i in all_x:
        if i in all_valid_x:
            print(i,all_valid_x[i])


