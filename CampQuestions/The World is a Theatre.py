import math
n=input().split(" ")
group=int(n[2])
boys=int(n[0])
girls=int(n[1])

possible=[]
j=0
for i in range(4,boys+1):
    curr=4+j
    diff=group-curr
    if diff<=girls and diff>0:
        possible.append([curr,diff])
    j+=1
# print(possible)
tot=0
for comb in possible:
    boyNum=(math.factorial(boys))//(math.factorial(comb[0])*(math.factorial(boys-comb[0])))
    girlNum=(math.factorial(girls))//(math.factorial(comb[1])*(math.factorial(girls-comb[1])))
    tot+=(boyNum*girlNum)

print(tot)




