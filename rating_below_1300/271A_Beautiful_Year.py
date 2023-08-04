n=int(input())
n+=1
while(True):
    if len(list(str(n)))==len(set(list(str(n)))):
        break
    n+=1
print(n)
