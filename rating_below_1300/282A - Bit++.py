n=int(input())
x=0
temp=0

for _ in range(n):
    s=input()
    if s[1]=="+":
        x+=1
    elif s[1]=="-":
        x-=1

print(x)
    
