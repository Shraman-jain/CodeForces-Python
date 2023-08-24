player=input()
cnt=0
prev=player[0]
for i in range(1,len(player)):
    if player[i]==prev:
        
        cnt+=1
        if cnt>=6:
            print("YES")
            print("if",player[i],prev,cnt)
            break
    else:
        cnt=0
        prev=player[i]
        print("else",player[i],prev,cnt)
else:
    print("NO")