class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode("")

    def addWord(self, word: str) -> None:
        
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode(i)
                
            current=current.children[i]
            

        current.endsHere=True
        
    def search(self, word: str) -> bool:
        
        current=self.root
        
        for i in range(len(word)):
            if word[i] in current.children:
                current=current.children[word[i]]
                
                
            elif word[i]=='.':
                if i!=len(word)-1:
                    for j in current.children:
                        ans1= self.dfs(current.children[j],i+1,word)
                        if ans1:
                            # print(ans1)
                            return True

                    return False
                
                else:
                    for j in current.children:
                        if current.children[j].endsHere:
                            return True
                        
                    return False

            
            else:
                return False
            
        
        if current.endsHere:
            return True
        
        return False
    
    
    
    def dfs(self,node,index,word):
        # print(index,word[index])
        
        if index==len(word)-1:
            if word[index] in node.children:
                if node.children[word[index]].endsHere==True:
                    return True
                
            elif word[index]=='.':
                for i in node.children:
                    if node.children[i].endsHere:
                        return True
                    
                return False
            
            else:
                return False
        
        # print(index, word[index])
        # print(word[index])
        if index<len(word):
            
            if word[index] in node.children:
                ans=self.dfs(node.children[word[index]],index+1,word)
                return ans

            elif word[index]=='.':
                for i in node.children:
                    ans=self.dfs(node.children[i],index+1,word)
                    if ans:
                        return True

                return False

            else:
                return False

class TrieNode:
    
    def __init__(self,ch):
        self.ch=ch
        self.children={}
        self.endsHere=False
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)