matrix=[[True for i in range(3)] for i in range(3)]
 
for i in range(3):
    lst=list(map(int,input().split()))
    for j in range(len(lst)):
        if lst[j]%2!=0:
            up=i-1
            down=i+1
            left=j-1
            right=j+1
            if up>=0:
                matrix[up][j]=not matrix[up][j]
            if down<3:
                matrix[down][j]=not matrix[down][j]
            if left>=0:
                matrix[i][left]=not matrix[i][left]
            if right<3:
                matrix[i][right]=not matrix[i][right]
            matrix[i][j]=not matrix[i][j]
for i in range(3):
    for j in range(3):
        print(int(matrix[i][j]),end="")
    print()



            