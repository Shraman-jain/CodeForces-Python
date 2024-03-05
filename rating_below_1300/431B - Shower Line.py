def cal(m,lst):
    return 2*(m[lst[2]][lst[3]]+m[lst[3]][lst[2]]+m[lst[3]][lst[4]]+m[lst[4]][lst[3]])+m[lst[0]][lst[1]]+m[lst[1]][lst[0]]+m[lst[1]][lst[2]]+m[lst[2]][lst[1]]
from itertools import permutations
matrix=[]
for i in range(5):
    matrix.append(list(map(int,input().split())))
l = list(permutations(range(0, 5)))
ans=0
for i in l:
    ans=max(ans,cal(matrix,i))
print(ans)