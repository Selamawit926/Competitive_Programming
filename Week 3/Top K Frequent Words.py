import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        heap = []
        dic = {}
        lst = []
        
        for i in words:
            if i in dic:
                dic[i] += 1
                
            else:
                dic[i] = 1
                
        
        for i in dic:
            heapq.heappush(heap,(-dic[i],i))
            
        for i in range(k):
            lst.append(heapq.heappop(heap)[1])
            
        return lst