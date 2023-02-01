# def check(i,di,dest):
#     if i==dest:
#         return True
    
#     if di[i] not in di:
#         return False
#     ans=check(di[i],di,dest)
#     return ans

n= input().split(" ")
lst=input().split(" ")
dest=int(n[1])
index=1
found=False
while index<=len(lst):
    index+=int(lst[index-1])
    if index==dest:
        found=True
        break
if found:
    print("YES")
else:
    print("NO")
# for i in range(1,len(lst)+1):
#     di[i]=i+int(lst[i-1])


# # print(di)
# values=di.values()
# valueSet=set(values)
# if dest not in valueSet:
#     print("NO")
# else:
#     ans=check(di[1],di,dest)
#     if ans==True:
#         print('YES')
#     else:
#         print('NO')
