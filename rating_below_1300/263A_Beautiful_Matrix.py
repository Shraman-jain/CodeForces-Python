for i in range(5):
    arr=list(map(int,input().split()))
    if 1 in arr:
        x=i
        for j in range(len(arr)):
            if arr[j] == 1:
                y=j
        print(abs(x-2)+abs(y-2))
                