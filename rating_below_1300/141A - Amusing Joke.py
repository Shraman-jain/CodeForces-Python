str1=input()
str2=input()
str3=input()

new=str1+str2
frq1={}
frq2={}
for i in new:
    frq1[i]=1+frq1.get(i,0)

for i in str3:
    frq2[i]=1+frq2.get(i,0)

if frq2.keys()!=frq1.keys():
    print("NO")
else:
    for key,value in frq2.items():
        if frq1[key]==value:
            continue
        else:
            print("NO")
            break
       
    else:
        print("YES")