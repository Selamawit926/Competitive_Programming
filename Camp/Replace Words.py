class TrieNode:
    def __init__(self,ch):
        self.ch=ch
        self.children={}
        self.endsHere=False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        
        sentence=sentence.split(" ")
        root=TrieNode("")
        
        
        for word in dictionary:
            current=root
            for letter in word:
                if letter not in current.children:
                    current.children[letter]=TrieNode(letter)
                    
                current=current.children[letter]
                
            current.endsHere=True
            
            
        # print(root.children["a"].children["a"].children["a"].children["a"].endsHere)
        for i in range(len(sentence)):
            current=root
            word=""
            for letter in sentence[i]:
                if letter in current.children:
                    
                    word+=letter
                    # print(word)
                    
                    current=current.children[letter]
                    
                    if current.endsHere==True:
                        sentence[i]=word
                        break
                    
                else:
                    break
    
                    
        return ' '.join(sentence)
        
                