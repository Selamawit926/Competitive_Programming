import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.heap=[]
        if len(self.nums)>=k:
            for i in range(len(self.nums)):
                if len(self.heap)<k:
                    heapq.heappush(self.heap,self.nums.pop(0))

                else:
                    first=self.nums.pop(0)
                    second=heapq.heappop(self.heap)
                    if first > second:
                        heapq.heappush(self.heap,first)
                    else:
                        heapq.heappush(self.heap,second)
                        
        else:
            for i in self.nums:
                heapq.heappush(self.heap,i)

    def add(self, val: int) -> int:
        if len(self.heap)==self.k:
            first=heapq.heappop(self.heap)
            if val>first:  
                heapq.heappush(self.heap,val)

            else:
                heapq.heappush(self.heap,first)

            return self.heap[0]

        else:
            heapq.heappush(self.heap,val)
            return self.heap[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)