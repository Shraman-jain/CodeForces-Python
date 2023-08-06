word=input()
up_count=0
low_count=0
for i in word:
    if i.islower():
        low_count+=1
    else:
        up_count+=1
if low_count>=up_count:
    print(word.lower())
else:
    print(word.upper())
