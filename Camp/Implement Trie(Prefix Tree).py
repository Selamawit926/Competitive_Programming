class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node= TrieNode("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current= self.node
        for i in range(len(word)):
            letter= word[i]
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            
            current=current.children[letter]
            
        current.endsHere=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current= self.getNode(word)
        
        if not current:
            return False
        
        return current.endsHere

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not self.getNode(prefix):
            return False
        
        return True
        
    def getNode(self,word:str):
        
        current= self.node
        for i in range(len(word)):
            letter= word[i]
            if letter not in current.children:
                return None
            
            current=current.children[letter]
        
        return current

class TrieNode:
    
    def __init__(self,ch):
        self.ch=ch
        self.endsHere=False
        self.children={}
        
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)