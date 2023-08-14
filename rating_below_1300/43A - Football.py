freq={}
for i in range(int(input())):
    team_name=input()
    freq[team_name]=1+freq.get(team_name,0)

winner=''
max_value=0
for key,value in freq.items():
    if value>max_value:
        max_value=value
        winner=key
print(winner)

