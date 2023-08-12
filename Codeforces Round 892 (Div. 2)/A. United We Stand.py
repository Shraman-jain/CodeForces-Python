for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))

    min_lst=min(lst)

    b,c=[],[]

    lst.sort()

    for i in lst:
        if i==min_lst:
            b.append(i)
        else:
            c.append(i)
    if len(b)==0 or len(c)==0:
        print(-1)
    else:
        print(len(b),len(c))
        print(*b)
        print(*c)