n,m=map(int,input().split())
lst=list(map(int,input().split()))

queue=[[i+1,lst[i]] for i in range(n)]


last_child=0
while(len(queue)!=0):
    child=queue.pop(0)
    last_child=child[0]
    if child[1]>m:
        queue.append([child[0],child[1]-m])

print(last_child)

