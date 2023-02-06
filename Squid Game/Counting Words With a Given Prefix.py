class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for word in words:
            newWord=word[0:len(pref)]
            if newWord==pref:
                count+=1
        return count