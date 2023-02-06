class Solution:
    def racecar(self, target: int) -> int:
        queue=deque([[0,1,0]])
        while queue:
            curr=queue.popleft()
            # print(curr)
            if curr[0]==target:
                return curr[2]
            queue.append((curr[0]+curr[1],curr[1]*2,curr[2]+1))
            if curr[1]>0:
                if curr[0]+curr[1]>target:
                    queue.append((curr[0],-1,curr[2]+1))
            else:
                if curr[0]+curr[1]<target:
                    queue.append((curr[0],1,curr[2]+1))