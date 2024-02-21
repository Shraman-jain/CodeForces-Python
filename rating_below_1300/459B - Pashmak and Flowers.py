n=int(input())
beauty=list(map(int,input().split()))
max_beauty = 0
min_beauty = 1e9 
for i in beauty:
    min_beauty = min(i,min_beauty)
    max_beauty = max(i,max_beauty)
max_beauty_cnt = beauty.count(max_beauty)
min_beauty_cnt = beauty.count(min_beauty)
if max_beauty==min_beauty:
    print(0,((n-1)*n)//2)
else:
    print(max_beauty-min_beauty,max_beauty_cnt*min_beauty_cnt)  
