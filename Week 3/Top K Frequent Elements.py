import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#        Approach 1 using min heap
        lst = []
        heap = []
        dic = {}
        for i in range(0,len(nums)) :
            if nums[i] in dic:
                dic[nums[i]] += 1
                
            else:
                dic[nums[i]] = 1
            
        # print(dic)
        
        for i in dic:
            heapq.heappush(heap,(-dic[i],i))
            
            
            
        for i in range(k):
            lst.append(heapq.heappop(heap)[1])

            
        return lst



        # Approach 2 using max heap

        # print(dic)
        for i in dic:
            heapq.heappush(heap,(dic[i],i))
        # print(heap)
        
        heapq._heapify_max(heap)
        # print(heap)
        
        for i in range(k):
            lst.append(heapq.heappop(heap)[1])
            heapq._heapify_max(heap)
#             print(heap)
#             print(lst)
            
        return lst