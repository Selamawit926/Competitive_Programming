def mergeSort(lst,start,end):
    if start<end:
        mid=(start+end)//2
        inp1=mergeSort(lst,start,mid)
        inp2=mergeSort(lst,mid+1,end)  
        return merge(inp1,inp2)

    return [lst[start]]

def merge(left,right):
    l=0
    r=0
    result=[]
    while l!=len(left) and r!=len(right):

        if left[l]>right[r]:
            result.append(right[r])
            r+=1

        elif left[l]<right[r]:
            result.append(left[l])
            l+=1

        else:
            result.append(right[r])
            r+=1
    
    if l==len(left):
        result=result+right[r:len(right)]

    elif r==len(right):
         result=result+left[l:len(left)]
    

    return result


print(mergeSort([5,3,1,0],0,3))
# print(merge([5,7,9],[3,6,7]))
# print(1)

