from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsSet=set(words)
        memo=defaultdict(int)
        count=0
        for word in words:
            count=max(count,self.helper(word,wordsSet,count,memo))
        return count
    
    def helper(self,word,wordsSet,count,memo):
        if word in memo:
            return memo[word]
        count=1
        for j in range(len(word)):
            newWord=word[:j]+word[j+1:]
            if newWord in wordsSet:
                count=max(count,1+self.helper(newWord,wordsSet,count,memo))
        memo[word]=count
        return count