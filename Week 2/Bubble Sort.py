a=[6,3,1,5,5,5,7,12,435,7989,23]

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j] :
            a[i],a[j]=a[j],a[i]

print(a)