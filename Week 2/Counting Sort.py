a=[6,6,1,1,5,4,3,4,2,45,12,45]
# from random import randint
# a=[]
# for i in range(0,10): 
#     b=randint(1,10000)
#     a.append(b)

lst=[0]*(max(a)+1)
lst2=[]

for i in a:
    lst[i]+=1
    

for i in range(0,len(lst)):
    for k in range(0,lst[i]):
        lst2.append(i)
   
print(lst2)
   

    