for _ in range(int(input())):
    no_of_arr=int(input())
    min_1=[]
    min_2=[]
    beauty=0
    for _ in range(no_of_arr):
        n=int(input())
        lst=list(map(int,input().split()))
        lst.sort()
        min_1.append(lst[0])
        min_2.append(lst[1])
    beauty+=min(min_1)
    min_2.sort()
    beauty+=sum(min_2[1:])
    print(beauty)
        

