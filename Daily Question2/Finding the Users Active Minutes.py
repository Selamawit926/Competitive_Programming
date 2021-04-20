class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        di={}
        answer=[0]*k
        # print(answer)
        for i in logs:
            if i[0] in di:
                answer[len(di[i[0]])-1]-=1
                di[i[0]].add(i[1])
                answer[len(di[i[0]])-1]+=1
                
            else:
                di[i[0]]={i[1]}
                answer[len(di[i[0]])-1]+=1
                        

        return answer