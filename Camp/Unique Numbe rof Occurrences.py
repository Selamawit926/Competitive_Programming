class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dic={}
        lst=[]
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
                
        print(dic)
        
        for i in dic:
            if dic[i] in lst:
                return False
            
            else:
                lst.append(dic[i])
                
        return True