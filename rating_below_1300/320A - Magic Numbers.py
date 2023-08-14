def f(n):
    n=str(n)
    for i in range(len(n)):
        
        if n[i]!='1' and  n[i]!='4':
            return False
        elif n[0]=='4':
            return False
        elif '444' in n:
            return False
        else:
            continue

    return True


n=int(input())
if f(n):
    print("YES")
else:
    print("NO")
