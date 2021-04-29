"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        lst=[x for x in range(1,z+1)]
        output=[]
        
        for i in range(len(lst)):
            start=0
            end=len(lst)-1
                
            while start<=end:

                mid=(start+end)//2
            
                # print(customfunction.f(lst[i],lst[mid]))
                
                if customfunction.f(lst[i],lst[mid])==z:
                    output.append([lst[i],lst[mid]])
                    break

                elif customfunction.f(lst[i],lst[mid])<z:
                    start=mid+1

                else:
                    end=mid-1
                        
        return output
                