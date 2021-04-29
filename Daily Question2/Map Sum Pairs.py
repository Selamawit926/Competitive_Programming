class TrieNode:
    
    def __init__(self,ch):
        self.ch=ch
        self.children={}
        self.endsHere=False

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node=TrieNode("")
        self.di={}
        
    def insert(self, key: str, val: int) -> None:
        
        self.di[key]=val
        current=self.node
        for i in key:
            if i not in current.children:
                current.children[i]=TrieNode(i)
                
            current=current.children[i]
            
        current.endsHere=True
                
    def sum(self, prefix: str) -> int:
        tot=0
        if prefix[0] not in self.node.children:
            return 0
        
        for i in self.di:
            if len(prefix)>len(i):
                continue
            for j in range(len(prefix)):
                if i[j]!=prefix[j]:
                    break
                if j==len(prefix)-1:
                    tot+=self.di[i]
               
                    
             
        return tot


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)