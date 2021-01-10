a=[6,6,1,1,5,4,3,4,2,45,12,45]
lst=[0]*(max(a)+1)
lst2=[]

for i in a:
    lst[i]+=1
    

for i in range(0,len(lst)):
    for k in range(0,lst[i]):
        lst2.append(i)
count=0
tot=0
k=7
for i in range(0,len(lst2)-1):
    if lst2[i]==lst2[i+1]:
        continue
    else:
        tot=tot+lst2[i]
        if tot<=k:
            count+=1
        
print(count)
   
print(lst2)
        