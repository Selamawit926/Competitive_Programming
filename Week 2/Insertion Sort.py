a=[6,0,3,1,5,5,5,7,34,12,11]

for i in range(1,len(a)):
    for j in range(i-1,-1,-1):
        if a[i]>a[j]:
           continue
        else:
            a[i],a[j]=a[j],a[i]
            i=j
            
print(a)
       
             


