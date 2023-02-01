# def smaller(num,nums):
#     newNum=num//2
#     if newNum==0:
#         return -1
#     if newNum in nums:
#        newNum=smaller(newNum,nums)
#     else:
#         return newNum
#     return newNum


# n=eval(input())
# inp=input().split(" ")
# lst=[int(x) for x in inp]
# lst.sort()
# nums=set(lst)
# maxi=-1
# for i in range(len(lst)-1,-1,-1):
#     maxi=lst[i]
#     newNum=smaller(maxi,nums)
#     nums=set(lst)
#     if newNum==-1:
#         break
#     lst[i]=newNum
    

# for i in lst:
#     print(i,end=" ")

5,4,3,2,1
5,9,12,14,15