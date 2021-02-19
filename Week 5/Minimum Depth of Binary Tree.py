# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue=[(root,1)]
        
        while(len(queue)!=0):
            
            node= queue.pop(0)
            # print(str(node[0].val)+ " "+ str(node[1]))
           
            
            if node[0].left:
                queue.append((node[0].left,node[1]+1))
                
                
            if node[0].right:
                queue.append((node[0].right,node[1]+1))
            
            
            if not node[0].left and not node[0].right:
                level=node[1]
                return level
                
            