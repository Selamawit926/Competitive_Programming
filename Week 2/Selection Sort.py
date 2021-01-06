a=[6,3,1,5,5,5,7,34,12]

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]>a[j]:
            continue
        else:
            a[i],a[j]=a[j],a[i]

print(a)