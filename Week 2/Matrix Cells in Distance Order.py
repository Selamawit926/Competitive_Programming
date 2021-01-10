row=2
col=2
r0=0
c0=1
lst2=[]
lst3=[]
for i in range(0,row):
    for j in range(0,col):
        d=abs(r0-i)+abs(c0-j)
        lst3.append(d)
        lst2.append([i,j])
        

print(lst3)
# for i in range(0,len(lst3)-1):
#     for j in range(i+1,len(lst3)):
#         if lst3[i]>lst3[j] :
#             lst3[i],lst3[j]=lst3[j],lst3[i]
#             lst2[i],lst2[j]=lst2[j],lst2[i]
lst=[0]*(max(lst3)+1)
lst4=[]

for i in lst3:
    lst[i]+=1
    

for i in range(0,len(lst)):
    for k in range(0,lst[i]):
        lst4.append(lst2[i])
   

print(lst3)
print(lst4)

           
# lst6=[0]*(max(lst3)+1)
# lst7=[]

# for i in lst3:
#     lst6[i]+=1
    

# for i in range(0,len(lst6)):
#     for k in range(0,lst6[i]):
#         lst7.append(i)


# for i in range(0,len(lst7)):
#     for j in range(0,len(di)):
#         if di[j]==lst7[i] and lst2[j] not in lst4:
#             lst4[i]=lst2[j]
