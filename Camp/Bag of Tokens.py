class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        
        score=0
        
        heapq.heapify(tokens)

        for i in range(len(tokens)):
            popped= heapq.heappop(tokens)
            # print(tokens)
           
            if popped <=P:
                P-=popped
                score+=1
                # print(score)
                # print(P)
            else:
                if score>=1 and tokens:
                    heapq._heapify_max(tokens)
                    P+=heapq.heappop(tokens)
                    heapq.heapify(tokens)
                    # print(tokens)
                    heapq.heappush(tokens,popped)
                    # print(tokens)
                    score-=1
            
                else:
                    return score
          
        return score