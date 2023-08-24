word=input().lower()
vowel=['a','e','i','o','u','y']
new_word=""
for i in word:
    if i not in vowel:
        new_word+="."
        new_word+=i
print(new_word)