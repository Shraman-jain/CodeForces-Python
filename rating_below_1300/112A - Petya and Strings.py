str1=input()
str2=input()
str1=str1.lower()
str2=str2.lower()

for i in range(len(str2)):
    if str1[i]!=str2[i]:
        if ord(str1[i])<ord(str2[i]):
            print(-1)
            break
        elif ord(str1[i])>ord(str2[i]):
            print(1)
            break
else:
    print(0)