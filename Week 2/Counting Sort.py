a=[6,6,1,1,5]
count=0
lst=[0]*len(a)
j=len(a)-1

print(lst)

for i in range(0,len(a)):
    if max(a)==a[i]:
        count=a.count(max(a))
        for k in range(0,count):
            lst[j]=a[i]
            j-=1
            a.remove(a[i])
   
print(lst)
        
    