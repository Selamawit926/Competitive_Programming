import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
#         heap implementation
        if len(arr)==1:
            return arr
        heap=[]
        output=[]
        lst=[]
        j=0
        for i in range(k):
            if arr[j]-x<0:
                heap.append((arr[j]-x,arr[j]))
                
            else:
                heap.append((-(arr[j]-x),arr[j]))
                
            j+=1
            
        heapq.heapify(heap)
        
        for i in range(k,len(arr)):
            popped=heapq.heappop(heap)
            if -abs(arr[i]-x) > popped[0]:
                heapq.heappush(heap,(-abs(arr[i]-x),arr[i]))
                
            else:
                heapq.heappush(heap,popped)
                
        # print(heap)
        for i in range(len(heap)):
            output.append(heapq.heappop(heap)[1])
            
        heapq.heapify(output)
        
        for i in range(len(output)):
            lst.append(heapq.heappop(output))
            
        return lst