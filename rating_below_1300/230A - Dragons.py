s,n=map(int,input().split())
level=[]
for _ in range(n):
    dh,bon=map(int,input().split())
    level.append((dh,bon))

temp=sorted(level, key=lambda x: x[1],reverse=True)
temp=sorted(level, key=lambda x: x[0])
for lvl in temp:
    dh,bon=lvl
    if dh>=s:
        print("NO")
        break
    else:
        s+=bon

else:
    print("YES")