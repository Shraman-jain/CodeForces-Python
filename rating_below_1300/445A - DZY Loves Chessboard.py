n,m=map(int,input().split())
matrix=[]
for i in range(n):
    s=input()
    matrix.append([i for i in s])

for row in range(n):
    for col in range(m):
        if matrix[row][col]==".":
            if (row+col)&1:
                print('B',end="")
            else:
                print('W',end="")
        else:
            print(matrix[row][col],end="")
    print()
          
