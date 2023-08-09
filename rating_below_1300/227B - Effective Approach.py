n=int(input())
lst=list(map(int,input().split()))
q=int(input())
queries=list(map(int,input().split()))

vasya=0
petya=0

temp=lst[::-1]

for i in range(q):
    for j in range(n):
        if lst[j]==queries[i]:
            vasya+=j+1
            break

    for j in range(n):
        if temp[j]==queries[i]:
            petya+=j+1
            break

print(vasya,petya)
