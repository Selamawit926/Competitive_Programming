class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # print(answers)
        tot=0
        di={}
        for i in answers:
            if i in di:
                if di[i]+1 > i+1:
                    tot+=i+1
                    di[i]=1
                    
                else:
                    di[i]+=1
            else:
                di[i]=1
                tot+=i+1
                
        return tot