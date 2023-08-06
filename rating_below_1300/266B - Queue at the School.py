n,t =map(int,input().split())
st=input()
arr=list(st)
ind=0
while(t>0):
    while(ind<n-1):
        if arr[ind]=="B" and arr[ind+1]=="G":
            arr[ind],arr[ind+1]=arr[ind+1],arr[ind]
            ind+=2
        else:
            ind+=1
    ind=0
    t-=1
print("".join(arr))