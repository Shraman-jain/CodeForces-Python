cnt_10=0
cnt_01=0
cnt_11=0
cnt_00=0
for _ in range( int(input())):
    l,r=map(int,input().split())
    if l==0 and r==0:
        cnt_10+=1
        cnt_01+=1
        cnt_11+=2
    elif l==0 and r==1:
        cnt_10+=2
        cnt_11+=1
        cnt_00+=1
    elif l==1 and r==0:
        cnt_01+=2
        cnt_11+=1
        cnt_00+=1
    elif l==1 and r==1:
        cnt_10+=1
        cnt_01+=1
        cnt_00+=2

print(min(cnt_01,cnt_10,cnt_00,cnt_11))
