class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        leader=[x for x in range(26)]
        di={}
        
        def find(a,count):
            
            if leader[a]==a:
                di[a]=count
                return a
            count+=1
            leader[a]=find(leader[a],count)
            
            return leader[a]
        
        def union(a,b):
            
            x=find(a,0)
            y=find(b,0)
            
            if di[x]>di[y]:
                leader[y]=leader[x]
                di[x]+=di[y]
                
            else:   
                leader[x]=leader[y]
                di[y]+=di[x]
            
        for equation in equations:
            x=ord(equation[0])-ord("a")
            y=ord(equation[-1])-ord("a")
            
            if equation[1]=="=":
                union(x,y)
            
        
        for equation in equations:
            x=ord(equation[0])-ord("a")
            y=ord(equation[-1])-ord("a")
            
            if equation[1]=="!" and find(x,0)==find(y,0):
                return False
            
            
        return True