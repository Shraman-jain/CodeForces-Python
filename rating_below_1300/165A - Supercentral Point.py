n=int(input())
coord_list_x=[]
coord_list_y=[]
for _ in range(n):
    x,y=map(int,input().split())
    coord_list_x.append(x)
    coord_list_y.append(y)

cnt=0
for i in range(n):
    upper=False
    lower=False
    left=False
    right=False
    for j in range(n):
        if coord_list_x[j]>coord_list_x[i] and  coord_list_y[i]==coord_list_y[j]:
            right=True
        if coord_list_x[j]<coord_list_x[i] and  coord_list_y[i]==coord_list_y[j]:
            left=True
        if coord_list_x[j]==coord_list_x[i] and  coord_list_y[i]>coord_list_y[j]:
            lower=True
        if coord_list_x[j]==coord_list_x[i] and  coord_list_y[i]<coord_list_y[j]:
            upper=True
    if left and right and upper and lower:
        cnt+=1
print(cnt) 
        
     