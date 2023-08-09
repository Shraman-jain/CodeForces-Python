def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm (a,b):
    return (a*b)//gcd(a,b)

k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())

# K U L U M U N = K + L + M + N - K ∩ L - K ∩ M - K ∩ N - L ∩ M - L ∩ N - M ∩ N 
#                 + K ∩ L ∩ M + K ∩ L ∩ N + K ∩ M ∩ N + L ∩ M ∩ N - K ∩ L ∩ M ∩ N
# ans is equal to K U L U M U N

ans=0

ans+=d//k
ans+=d//l
ans+=d//m
ans+=d//n



ans-=d//lcm(k,l)
ans-=d//lcm(k,m)
ans-=d//lcm(k,n)
ans-=d//lcm(l,m)
ans-=d//lcm(l,n)
ans-=d//lcm(m,n)


ans+=d//lcm(lcm(k,l),m)
ans+=d//lcm(lcm(k,l),n)
ans+=d//lcm(lcm(k,m),n)
ans+=d//lcm(lcm(l,m),n)

ans-=d//lcm(lcm(lcm(k,l),m),n)

print(ans)