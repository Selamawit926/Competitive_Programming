import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap=[]
        
        for i in stones:
            heapq.heappush(heap,-i)
            
        # heapq.heapify(heap)
        while len(heap)>1:
            first=heapq.heappop(heap)
            second=heapq.heappop(heap)
            if first!=second:
                heapq.heappush(heap,-(second-first))
                
        if len(heap)!=0:
            return -heap[0]
        else:
            return 0