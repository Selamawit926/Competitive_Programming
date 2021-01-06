
a=[-5,-9,-2,4,1]
lst=[0]*(-min(a)+max(a)+1)
lst2=[]
#print(a[-9])


for i in a:
    if i<0 :
        lst[-(max(a)-i)]+=1
    else:
        lst[i]+=1
    

for i in range(0,len(lst)):
    for k in range(0,lst[i]):
        lst2.append(i)

print(lst)