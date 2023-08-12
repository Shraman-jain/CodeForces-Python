
# it is correct but it's giving TLE 
"""
n,k=map(int,input().split())
even_lst=[i for i in range(1,n+1) if i%2==0]
lst=[i for i in range(1,n+1) if i%2]
lst.extend(even_lst)
print(lst[k-1])

"""

n,k=map(int,input().split())

# if n is odd
if n%2:
    no_of_odd=(n//2)+1
else:
    no_of_odd=n//2
if k<=(no_of_odd):
    print((k*2)-1)
else:
    print((k-no_of_odd)*2)
