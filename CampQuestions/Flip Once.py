from collections import defaultdict
import copy
def reverse(org,left,right):
    while left<=right:
        org[left],org[right]=org[right],org[left]
        left+=1
        right-=1
    newNum="".join(org)
    return int(newNum)
def flip(number):
    num=str(number)
    lst=list(num)
    di=defaultdict(list)
    for i in range(len(lst)):
        di[lst[i]].append(i)
    lst.sort()
    i=len(lst)-1
    j=0
    left=flipN=-1
    while i>=0 and j<len(num):
        if lst[i]!=num[j]:
            left=j
            flipN=lst[i]
            break
        i-=1
        j+=1
    if flipN!=-1:
        maxi=float("-inf")
        for i in range(len(di[flipN])):
            new=list(num)
            newNum=reverse(new,left,di[flipN][i])
            maxi=max(maxi,newNum)
        return maxi
    else:
        return int(num)

print(flip(30477))
print(flip(37047))
print(flip(47037))
print(flip(74320))




# def check(subset,A,diff,i,tot):
  
#   for j in range(i+1,len(A)-1):
#     subset.append(A[j])
#     val=sum(subset)
#     diff=min(diff,abs((tot-val)-val))
#     diff=check(subset,A,diff,j,tot)
   
#   subset.pop()
#   return diff

#   def solution(A):
#   """Your solution goes here."""
#   #sys.stderr.write('Tip: Use sys.stderr.write() to write debug messages on the output tab.\n')
#   tot=sum(A)
#   diff=float("inf")
#   for i in range(len(A)-1):
#     subset=[A[i]]
#     val=sum(subset)
#     diff=min(diff,abs((tot-val)-val))
#     diff=check(subset,A,diff,i,tot)
#   return diff