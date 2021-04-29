class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        di1={}
        for i in range(len(pattern)):
            if pattern[i] in di1:
                di1[pattern[i]].append(i)
                di1[pattern[i]][0]+=1
                
            else:
                di1[pattern[i]]=[1,i]
                
        lst=di1.values()
        # print(list(lst))
        output=[]
        
        for i in words:
            di2={}
            for j in range(len(i)):
                if i[j] in di2:
                    di2[i[j]].append(j)
                    di2[i[j]][0]+=1
                    
                else:
                    di2[i[j]]=[1,j]
                    
            lst2=di2.values()
            # print(list(lst2))
            if list(lst)==list(lst2):
                output.append(i)
                # print(output)
        return output
        