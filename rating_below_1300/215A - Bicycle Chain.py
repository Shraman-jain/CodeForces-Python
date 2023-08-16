n=int(input())
gear1=list(map(int,input().split()))
m=int(input())
gear2=list(map(int,input().split()))
freq={}
for i in gear1:
    for j in gear2 :
        if j%i==0:
            freq[j//i]=1+freq.get(j//i,0)

print(freq[max(freq.keys())])
