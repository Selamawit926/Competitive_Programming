import math
friend1=eval(input())
friend2=eval(input())

mid=int(math.ceil((friend1+friend2)/2))
diff1=abs(mid-friend1)
diff2=abs(friend2-mid)
tot=0
for i in range(1,diff1+1):
    tot+=i
for i in range(1,diff2+1):
    tot+=i
print(tot)