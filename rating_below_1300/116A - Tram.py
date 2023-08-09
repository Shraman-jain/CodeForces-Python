n=int(input())
curr_cap=0
min_cap=0
for i in range(n):
    a,b=map(int,input().split())
    curr_cap-=a
    curr_cap+=b
    min_cap=max(curr_cap,min_cap)
print(min_cap)
