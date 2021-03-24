class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        lst=[]
        lst2=[]
        di={}
        
        for i in range(len(mat)):
            
            # di[i]=mat[i].count(1)
            count=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count+=1
                    
                else:
                    break
            
            lst.append((count,i))
                
          
        heapq.heapify(lst) 
        # print(lst)
        
        while k>=1:
            lst2.append(heapq.heappop(lst)[1])
            k-=1
            
        return lst2
    
#         while k>=1:
#             for i in di:
#                 if di[i]==min(di.values()):
#                     lst.append(i)
#                     di.pop(i)
#                     break
                    
#             k-=1
                
                
#         # print(lst)
#         return lst
                
        # print(min(di.values()))