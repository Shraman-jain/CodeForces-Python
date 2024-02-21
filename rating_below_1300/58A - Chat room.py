# def f(string,i,lst,temp):
#     if i==len(string):
#         lst.append(''.join(temp.copy()))
#         return
#     temp.append(string[i])
#     f(string,i+1,lst,temp)
#     temp.pop()
#     f(string,i+1,lst,temp)
#     return lst

# s=input()
# if len(s)<5:
#     print("NO")
# else:
#     ans=f(s,0,[],[])
#     if 'hello' in ans:
#         print("YES")
#     else:
#         print("NO")

s=input()
temp="hello"
i,j=0,0
while(True):
    if j==5:
        print("YES")
        break
    if i==len(s):
        print("NO")
        break
    if s[i]==temp[j]:
        i+=1
        j+=1
    elif s[i]!=temp[j]:
        i+=1
    
