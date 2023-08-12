n=int(input())
lst=list(map(int,input().split()))

min_city=min(lst)
town_no=0
flag=False
for i in range(len(lst)):
    if lst[i]==min_city and flag==False:
        town_no=i+1
        flag=True
    elif lst[i]==min_city and flag==True:
        print("Still Rozdil")
        break
else:
    print(town_no)