s=input()
temp=""
dic={'.':'0','-.':'1','--':'2'}
ans=""
for i in s:
    temp+=i
    if temp in dic:
        ans+=dic[temp]
        temp=""
    
print(ans)