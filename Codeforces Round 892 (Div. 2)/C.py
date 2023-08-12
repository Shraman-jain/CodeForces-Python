for _ in range(int(input())):
    n=int(input())
    ans=0
    new_n=(n//2)+1
    ss=(new_n*(new_n+1)*((2*new_n)+1))/6
    last=n
    for i in range(new_n+1,n+1):
        ss+=(i)*last
        last-=1
    

