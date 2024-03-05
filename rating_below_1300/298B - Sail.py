# Trying with Recursion but it is not that complicated and also gives TLE

# def f(sx,sy,ex,ey,t,cnt,lst,arr):
#     if cnt>t:
#         return
#     if sx==ex and sy==ey:
#         lst.append(cnt)
#         return lst
#     pick = f(sx+arr[cnt][0],sy+arr[cnt][1],ex,ey,t,cnt+1,lst,arr)
#     not_pick = f(sx,sy,ex,ey,t,cnt+1,lst,arr)
#     return lst 

# t,sx,sy,ex,ey=map(int,input().split())
# s=input()
# arr=[]
# for i in range(len(s)+1):
#     arr.append([0,0])
# for i in range(len(s)):
#     v=s[i]
#     if v=="S":
#         arr[i][1]=-1
#     if v=="N":
#         arr[i][1]=1
#     if v=="E":
#         arr[i][0]=1
#     if v=="W":
#         arr[i][0]=-1
# # print(arr)

# ans=f(sx,sy,ex,ey,t,0,[],arr)
# # print(ans)
# if len(ans)==0:
#     print(-1)
# else:
#     print(min(ans))


# Simply find the difference and count the direction needed to reach at the end
# and check whether we can get there or not by freq of needed direction in given direction sequence  
t,sx,sy,ex,ey=map(int,input().split())
s=input()      
x_diff=sx-ex
y_diff=sy-ey
# print(x_diff,y_diff)
req={}
if x_diff<0:
    req["E"]=(-1*x_diff)
elif x_diff>=0:
    req["W"]=(x_diff)
if y_diff<0:
    req["N"]=(-1*y_diff)
elif y_diff>=0:
    req["S"]=(y_diff)
# print(req)
flag=False
for i in range(t):
    if s[i] in req and req[s[i]]!=0:
        req[s[i]]-=1
    if sum(list(req.values()))==0:
        print(i+1)
        flag=True
        break
if flag == False:
    print(-1)