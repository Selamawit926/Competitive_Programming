class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        visited=deque()
        count=set()
        left=right=0
        maxLength=0
        
        while left<len(tree) and right<len(tree):
            
            if len(count)<2 or tree[right] in count:
                count.add(tree[right])
                visited.append(tree[right])
                right+=1
                  
            else:
               
                maxLength=max(right-left,maxLength)
                popped=visited.popleft()
                if popped not in visited:
                    count.remove(popped)
                left+=1

        maxLength=max(right-left,maxLength)
            
        return maxLength