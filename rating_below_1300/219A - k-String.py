# n=int(input())
# s=input()
# new_str=''
# freq={}
# for i in s:
#     freq[i]=1+freq.get(i,0)

# uniq=list(map(str,freq.keys()))
# if len(uniq)==1:
#     if len(s)==n:
#         print(s)
#     else:
#         print(-1)
# elif max(freq.values())!=min(freq.values()):
#     print(-1)
# else:
#     ind=0
#     while(ind<len(s)):
#         # print(ind%n)
#         # print(uniq)
#         # print(uniq[ind%n])
#         new_str+=uniq[ind%n]
#         ind+=1
#     print(new_str)

    
k=int(input())
s=input()
a="abcdefghijklmnopqrstuvwxyz"
b=[]
f=1

for i in range(26):
    b.append(s.count(a[i]))
    if b[i]%k!=0:
        f=0
        break
if f==1 and len(s)%k==0:
    for j in range(k):
        for i in range(26):
            print(a[i]*int(b[i]/k),end='')


else:
    print(-1)
