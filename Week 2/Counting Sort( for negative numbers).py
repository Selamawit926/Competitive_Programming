# from random import randint
# a=[]
# for i in range(0,10): 
#     b=randint(-10,10)
#     a.append(b)
a=[-5,-9,-9,-2,4,1]
lst=[0]*(-min(a)+max(a)+1)
lst2=[]

for i in a:
    if i<0 :
        lst[i-min(a)]+=1
    else:
        lst[i+(-min(a))]+=1
    

for i in range(0,len(lst)):
    for k in range(0,lst[i]):
        lst2.append(i-9)

print(lst)
print(lst2)