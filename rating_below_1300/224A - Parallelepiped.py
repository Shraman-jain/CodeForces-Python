import math
A1,A2,A3=map(int,input().split())

# A1= LH
# A2= WH
# A3= LW

H=math.sqrt((A1*A2)/A3)
L=A1/H
W=A2/H

print(int(4*L+4*W+4*H))