n=int(input())
lst=list(map(int,input().split()))
q=int(input())
queries=list(map(int,input().split()))

vasya=0
petya=0

left=[0  for i in range(100005)]
right=[0  for i in range(100005)]

temp=lst[::-1]

for i in range(n):
    left[lst[i]]=i+1

for i in range(n):
    right[temp[i]]=i+1

for i in range(q):
    vasya+=left[queries[i]]
    petya+=right[queries[i]]
    

print(vasya,petya)
