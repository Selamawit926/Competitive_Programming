# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue=deque()
        queue.append((root,1))
        di={1:root.val}
    
        while queue:
            popped=queue.popleft()
            if popped[1] in di:
                if popped[0].val>di[popped[1]]:
                    di[popped[1]]=popped[0].val
                    
            else:
                di[popped[1]]=popped[0].val
                
            if popped[0].left:
                queue.append((popped[0].left,popped[1]+1))
                
            if popped[0].right:
                queue.append((popped[0].right,popped[1]+1))
                
                
        return di.values()