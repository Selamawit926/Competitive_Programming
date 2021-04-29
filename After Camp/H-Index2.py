class Solution:
    def hIndex(self, citations: List[int]) -> int:
        print(citations)
        
        if len(citations)==1:
            if citations[0]==0:
                return 0 
            else: 
                return 1
        
        start=0
        end=len(citations)-1
        hindex=0
        while start<=end:
            mid=(start+end)//2
            
            index=len(citations)-mid
            
            if index<=citations[mid]:
                hindex=index
                end=mid-1
            
            else:
                start=mid+1
            
            
        
        return hindex