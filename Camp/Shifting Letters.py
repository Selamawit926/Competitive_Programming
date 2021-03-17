class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        tot= sum(shifts)
        newWord=""
        for i in range(len(shifts)):
            if ord(S[i])+tot > 122:
                letter = (ord(S[i])+tot-122)%26 + 96
                
                if (ord(S[i])+tot-122)%26 ==0:
                    letter=122
                
            else:
                letter = ord(S[i])+tot
            
            newWord+= chr(letter)
            tot-=shifts[i]
            # print(newWord)
        
        
        
        
        return newWord
        