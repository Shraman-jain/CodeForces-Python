num=int(input())
cnt=0
for i in range(len(str(num))):
    if str(num)[i]=='4' or str(num)[i]=='7':
        cnt+=1
if cnt==4 or cnt==7:
    print("YES")
else:
    print("NO")